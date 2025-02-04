import argparse
import pandas as pd
import numpy as np

# from common: commonly used functions
from vdl_tools.LinkedIn import org_loader as li
from vdl_tools.LinkedIn.utils.linkedin_url import extract_linkedin_id

import vdl_tools.scrape_enrich.geocode as geocode
import vdl_tools.scrape_enrich.process_images as images
import vdl_tools.scrape_enrich.tags_from_text as tft
from vdl_tools.scrape_enrich.scraper.scrape_websites import extract_website_name, scrape_websites_psql
from vdl_tools.shared_tools.all_source_organization_summarization import generate_summary_of_summaries
from vdl_tools.shared_tools import climatebert_adaptation as adp
from vdl_tools.shared_tools.climate_landscape.add_one_earth_taxonomy import add_one_earth_taxonomy
from vdl_tools.shared_tools.climate_landscape.diversity_keywords import DIVERSITY_BIPOC_DICT
import vdl_tools.shared_tools.common_functions as cf
from vdl_tools.shared_tools.database_cache.database_utils import get_session
from vdl_tools.shared_tools.geotagging_prompting import geotag_texts_bulk
import vdl_tools.shared_tools.gpt_relevant_for_thinning as gpt
from vdl_tools.shared_tools.tools.config_utils import get_configuration
from vdl_tools.shared_tools.tools.logger import logger
from vdl_tools.shared_tools.web_summarization.website_summarization_psql import summarize_scraped_df
from vdl_tools.shared_tools.tools.falsey_checks import coerced_bool


GLOBAL_CONFIG = get_configuration()


MIN_DESCRIPTION_LENGTH = 100
TEXT_FIELDS = ["Description", "Description_990", "Website Summary", "About LinkedIn"]


def get_website_summaries(
    df,
    website_column_scrape='Website_cb_cd',
    canonical_website_column='Website',
    skip_existing=True,
):
    df_web, df = get_scraped_df(
        df,
        website_column_scrape=website_column_scrape,
        canonical_website_column=canonical_website_column,
        skip_existing=skip_existing,
    )

    # Filter out short texts
    df_web = df_web[df_web['text'].apply(lambda x: len(x) > 50)].copy()
    # Summarize those sites
    with get_session(GLOBAL_CONFIG) as session:
        summaries = summarize_scraped_df(
            df_web,
            session=session,
            skip_existing=skip_existing,
        )

    summaries = {k.rstrip("/"): v for k, v in summaries.items()}
    df[website_column_scrape] = df[website_column_scrape].apply(lambda x: x.rstrip("/") if coerced_bool(x) else x)
    df[canonical_website_column] = df[canonical_website_column].apply(lambda x: x.rstrip("/") if coerced_bool(x) else x)

    return summaries, df


def get_scraped_df(
    df,
    website_column_scrape='Website_cb_cd',
    canonical_website_column='Website',
    linkedin_url_column='LinkedIn',
    skip_existing=True,
):

    if linkedin_url_column not in df.columns:
        df[linkedin_url_column] = None

    if canonical_website_column not in df.columns:
        df[canonical_website_column] = df[website_column_scrape]

    has_url_mask = df[website_column_scrape].notnull()

    with get_session() as session:
        df_web = scrape_websites_psql(
            # filter out null websites,
            urls=df[has_url_mask][website_column_scrape],
            session=session,
            skip_existing=skip_existing,
            subpage_type="about",
            n_per_commit=20,
            max_errors=1,
        )

    web_success_mask = df_web['response_status_code'] == 200
    df_web_success = df_web[web_success_mask].copy()

    failed_urls = df_web[~web_success_mask & df_web['type'] == 'PageType.INDEX']['source'].unique()

    has_linkedin_mask = df[linkedin_url_column].notnull()
    failed_urls_linkedin_urls = df[df[website_column_scrape].isin(failed_urls) & has_linkedin_mask][linkedin_url_column].tolist()

    no_web_url_has_linkedin = df[~has_url_mask & has_linkedin_mask][linkedin_url_column].tolist()
    linkedin_urls = no_web_url_has_linkedin + failed_urls_linkedin_urls

    # Scrape LinkedIn for those that didn't have a url or their LinkedIn url didn't work
    if linkedin_urls:
        with get_session(GLOBAL_CONFIG) as session:
            df_linkedin = li.scrape_organizations_psql(
                linkedin_urls,
                session=session,
                api_key=GLOBAL_CONFIG['linkedin']['coresignal_api_key'],
                max_errors=1,
            )

        original_li_id_to_website_url = {
            extract_linkedin_id(x['original_id']): x['website']
            for _, x in df_linkedin.iterrows()
            if x['website']
        }

        # Guard against the case where the LinkedIn url from original and from coresignal differ by
        # http vs https or or trailing slash
        df['extracted_linkedin_id'] = df[linkedin_url_column].apply(
            lambda x: extract_linkedin_id(x) if coerced_bool(x) else None
        )
        df[canonical_website_column] = df.apply(
            lambda x: original_li_id_to_website_url.get(
                x['extracted_linkedin_id'], x[canonical_website_column]
            ),
            axis=1,
        )

        # Now scrape them based on the websites we just got
        df_web_for_scraping = df[df[linkedin_url_column].isin(linkedin_urls) & df[canonical_website_column].notnull()]
        with get_session() as session:
            df_web_linkedin = scrape_websites_psql(
                # filter out null websites,
                urls=df_web_for_scraping[canonical_website_column],
                session=session,
                skip_existing=skip_existing,
                subpage_type="about",
                n_per_commit=20,
                max_errors=1,
            )
        
        if df_web_for_scraping.shape[0] > 0:
            df_web_linkedin_success = df_web_linkedin[df_web_linkedin['response_status_code'] == 200]
            df_web_success = pd.concat([df_web_success, df_web_linkedin_success])
    
    return df_web_success, df


def _missing_description_mask(df, min_description_length=MIN_DESCRIPTION_LENGTH):
    """returns a filtering mask when the description is missing or too short"""
    return (
        (df['Description'].isnull()) |
        (df['Description'].str.len() < min_description_length)
    )


def prepare_for_relevance_model(df):
    """The relevance models require descriptive text.
    CB and Candid descriptions have shown to be enough text for the models to work.
    However, sometimes we are missing the descriptions from the original source.

    In this case, we will use summaries from their scraped websites.
    
    If the website urls are are missing, we will scrape LinkedIn for their website urls and descriptions.
    Then we
    """
    # Determine which organizations have missing descriptions or their descriptions are too short
    missing_descriptions_mask = _missing_description_mask(
        df,
        min_description_length=MIN_DESCRIPTION_LENGTH,
    )

    # Scrape websites for those missing descriptions
    df_missing_descriptions = df[missing_descriptions_mask].copy()

    if df_missing_descriptions.shape[0] > 0:
        # Add the website summaries but only for those missing descriptions
        summaries_for_missing_desc, df_missing_descriptions = get_website_summaries(
            df_missing_descriptions,
            skip_existing=True
        )
    else:
        summaries_for_missing_desc = {}
        df_missing_descriptions = pd.DataFrame()

    df['text_for_relevance_model'] = df['Description']
    df['Website'] = None

    # df_missing_descriptions will have a Website either from Website_cb_cd or LinkedIn
    if df_missing_descriptions.shape[0] > 0:
        df['Website'].fillna(df_missing_descriptions['Website'], inplace=True)
    df['Website'].fillna(df['Website_cb_cd'], inplace=True)
    df['Website Summary'] = df['Website'].map(summaries_for_missing_desc, None)
    df['text_for_relevance_model'].fillna(df['Website Summary'], inplace=True)

    # TO DO: Fix what happens when there is no website text
    # LinkedIn text? 990?
    return df


def run_relevance_model(
    df,
    model_name,
    idn,
    save_path,
):

    model_name_safe = model_name.replace("-", "_").replace(":", "_")

    # Rename the save path to include the model name so we know exactly which model made the predictions
    save_path = save_path.with_name(save_path.name.replace("MODEL_NAME_HOLDER", model_name_safe))
    predictions = gpt.generate_predictions(
        df,
        500,
        'text_for_relevance_model',
        save_path=save_path,
        model=model_name,
        idn=idn,
    )

    df['prediction_relevant'], df['probability_relevant'] = (
        zip(*df[idn].map(lambda x: predictions.get(x, (None, None))))
    )
    good_predictions_mask = df["prediction_relevant"].isin([0, 1])
    errors = df[~good_predictions_mask].copy()
    df = df[good_predictions_mask].copy()
    return df, errors


def add_geotags(df, text_fields=TEXT_FIELDS):
    ids_texts = []
    for _, row in df[["id"] + text_fields].iterrows():
        text = "\n".join([row[col] for col in text_fields if row[col] and isinstance(row[col], str)])
        ids_texts.append((row['id'], text))

    with get_session(GLOBAL_CONFIG) as session:
        ids_to_geotags = geotag_texts_bulk(
            ids_texts=ids_texts,
            session=session,
            use_cached_result=True
        )

    df['Geo_Tags_Dicts'] = df['id'].map(ids_to_geotags)
    df['Geo_Tags'] = df['Geo_Tags_Dicts'].apply(
        lambda geo_dicts_list: "|".join(
            [v for geo_dict in geo_dicts_list for v in geo_dict.values() if v]
            ) if isinstance(geo_dicts_list, list) else ""
    )
    return df


def add_climate_keywords(
    df,
    keyword_path,
    paths,
    id_col='id',
    df_climate_kwds=None,
    text_fields=TEXT_FIELDS,
):
    # load kwd mapping table (here it is master_term: [list of search terms])
    # terms used in database search
    if df_climate_kwds is None:
        df_climate_kwds = pd.read_excel(keyword_path, engine='openpyxl')
        cf.string2list(
            df_climate_kwds,
            ['broad_tags', 'bigram', 'unigram', 'search_terms'] # format as lists
        )

    df = tft.add_kwd_tags(
        df,
        df_climate_kwds,  # kwd mapping corpus gropued by tag
        # output filename for orgs with tags
        paths['orgs_w_climate_kwds'],
        # where to store tagged results
        paths['local_kwds'],
        kwds='climate_kwds',  # column to store tags
        idCol=id_col,  # unique id column
        # text columns to search
        textcols=text_fields,
        format_tagmap=True,  # explode search terms
        master_term='tag',  # name col with master term
        search_terms='search_terms',  # name of col with list of search terms
        add_related='broad_tags',  # name of col with manual list of add_related
        # add unigrams within 2 or more grams.
        add_unigrams=True,
        add_bigrams=True,  # add bigrams within 3 or more grams
        loadexisting=False,  # True = don't run search just load prior results
    )
    return df


def add_summary_of_summaries(
    df,
    text_fields=TEXT_FIELDS,
    id_col='id',
    use_cached_results=True,
):

    # Remove all the rows that are missing all the text fields
    contains_at_least_one_text = (
        np.logical_or
        .reduce(
            [df[field].apply(coerced_bool) for field in text_fields]
        )
    )
    if not contains_at_least_one_text.all():
        logger.info(
            "Dropping %s rows that are missing all text fields for summarization",
            (~contains_at_least_one_text).sum()
        )
    df_for_summary = df[contains_at_least_one_text].copy()

    df_for_summary.fillna({col: "" for col in text_fields}, inplace=True)

    ids_text_lists = zip(
        df_for_summary[id_col].values,
        df_for_summary[text_fields].values.tolist()
    )
    ids_to_summaries = generate_summary_of_summaries(
        ids_text_lists,
        use_cached_results=use_cached_results,
    )

    df['Summary'] = df[id_col].map(ids_to_summaries, None)
    return df


def _log_major_step(text):
    full_text = "\n" + "*" * 100 + f"\n{text}\n" + "*" * 100
    logger.info(full_text)


def run_pipeline(
    paths,
    relevance_model_name=gpt.cb_cd_model_4omini,
    adaptation_model_id=adp.CPI_ADAPTATION_MODEL_2024_ID,
    num_records=None,
    run_process_images=False,
    id_col='id',
    run_one_earth_taxonomy=True,
    text_fields=TEXT_FIELDS,
):

    _log_major_step("loading pre-processed combined crunchbase + candid data")
    df_cb_cd_full = pd.read_excel(paths['enrich_input_file'])
    logger.info("Loaded %s organizations", len(df_cb_cd_full))

    if num_records:
        _log_major_step(f"Filtering down to {num_records} records")
        n_per_source = round(num_records // 2)
        df_cb_cd = pd.concat([
            df_cb_cd_full[df_cb_cd_full['Data Source'] == "Crunchbase"].iloc[:n_per_source],
            df_cb_cd_full[df_cb_cd_full['Data Source'] == "Candid"].iloc[:n_per_source],
        ])
    else:
        df_cb_cd = df_cb_cd_full

    _log_major_step("Preparing DF for relevance model")
    df_cb_cd = prepare_for_relevance_model(df_cb_cd)

    # Run Model for CB
    _log_major_step("Running relevance model")
    df_cb_cd, df_cb_cd_errors = run_relevance_model(
        df=df_cb_cd,
        model_name=relevance_model_name,
        idn=id_col,
        save_path=paths['relevance_model_predictions_path'],
    )
    df_cb_cd.to_json(paths['relevance_model_results'], orient='records')

    df_relevant = df_cb_cd[df_cb_cd['prediction_relevant'] == 1].copy()
    logger.info(
        "Filtered to relevant orgs. Went from %s to %s orgs",
        df_cb_cd.shape[0],
        df_relevant.shape[0],
    )

    _log_major_step("Generating website summaries")

    # Reset the canonical website column and let `get_website_summaries` fill it in
    if 'Website' in df_relevant.columns:
        df_relevant.pop('Website')
    summaries, df_relevant = get_website_summaries(
        df_relevant,
        skip_existing=True,
    )

    df_relevant['extracted_website_key'] = df_relevant['Website'].apply(
        lambda x: extract_website_name(x)
        if coerced_bool(x) else None
    )
    summaries = {extract_website_name(k): v for k, v in summaries.items()}
    df_relevant['Website Summary'] = df_relevant['extracted_website_key'].map(summaries, None)

    # LinkedIn
    _log_major_step("Scraping LinkedIn")
    with get_session() as session:
        df_linkedin = li.scrape_organizations_psql(
            urls=df_relevant[df_relevant['LinkedIn'].notnull()]["LinkedIn"],
            session=session,
            api_key=GLOBAL_CONFIG["linkedin"]["coresignal_api_key"],
            skip_existing=True,
            max_errors=1,
            n_per_commit=10,
        )

    df_linkedin.drop(columns=['summary'], inplace=True)
    df_linkedin.rename(
        columns={"about": "About LinkedIn", "name": "profile_name"},
        inplace=True,
    )
    # Combine the LinkedIn data
    df_relevant = cf.combine_cb_cd_li(df_relevant, df_linkedin)
    # Now if the LinkedIn data from Coresignal is missing, assume it's a dead link
    # `datasource` is a column that is only present in the LinkedIn data

    # FIXME (ztawil): Better column naming patterns to know what is coming from where
    # https://airtable.com/appyWHEF7oCMjw6zR/tblvnllSFsnMOQrA1/viw8A93szuWwwCSjo/recf7V9RBN3CB0Sw6?blocks=hide
    df_relevant['Original LinkedIn'] = df_relevant['LinkedIn']
    df_relevant['LinkedIn'] = df_relevant.apply(
        lambda x: x['Original LinkedIn'] if coerced_bool(x['Original LinkedIn']) and coerced_bool(x['datasource']) else None,
        axis=1,
    )

    _log_major_step("Cleaning Text Fields")
    # Clean Text of Line Breaks, Tabs, Double Spaces
    for col in text_fields:
        condition = ~df_relevant[col].isna()
        if len(df_relevant[condition]) == 0:
            continue
        cf.clean_spaces_linebreaks_col(df_relevant, col)

    _log_major_step("Running Adaptation/Mitigation Model")
    # Adaptation/Mitigation/Dual
    df_relevant['text'] = cf.join_strings_no_missing(df_relevant, text_fields)

    adaptation_model_path = paths['adaptation_mitigation_results_path']
    adapt_model_name_safe = adaptation_model_id.replace("-", "_").replace(":", "_")
    adaptation_model_path = adaptation_model_path.with_name(
        adaptation_model_path.name.replace("MODEL_NAME_HOLDER", adapt_model_name_safe)
    )
    preds_adapt = adp.generate_predictions_adapt_mit_remote(
        df_relevant,
        50,
        'id',
        'text',
        adaptation_model_path,
        api_key=GLOBAL_CONFIG['baseten']['api_key'],
        model_id=adaptation_model_id,
    )
    df_relevant["predictions_adapt"] = df_relevant["id"].map(preds_adapt)
    df_relevant = df_relevant[df_relevant["predictions_adapt"].isin(["adaptation", "mitigation", "both"])]

    _log_major_step("Removing any organizations without Description, Website Summary, or LinkedIn About")
    df_relevant = df_relevant[
        df_relevant['Description'].notnull() |
        df_relevant['Website Summary'].notnull() |
        df_relevant['About LinkedIn'].notnull()
    ].copy()

    # ADD SUMMARY OF SUMMARIES
    _log_major_step("Adding summary of summaries")
    df_relevant = add_summary_of_summaries(
        df_relevant,
        text_fields=text_fields,
        id_col='id',
        use_cached_results=True,
    )

    df_relevant['missing_all_texts'] = df_relevant.apply(
        lambda x: all([not(coerced_bool(x[col])) for col in text_fields],),
        axis=1,
    )
    df_relevant = df_relevant[~df_relevant['missing_all_texts']].copy()

    # OneEarth
    _log_major_step("Adding One Earth Taxonomy")

    def choose_longer_text(row):
        website_summary = row['Website Summary']
        if pd.isnull(website_summary):
            website_summary = ""
        general_summary = row['Summary']
        if pd.isnull(general_summary):
            general_summary = ""
        if len(general_summary) >= len(website_summary):
            return general_summary
        return website_summary

    df_relevant['text_for_one_earth'] = df_relevant.apply(choose_longer_text, axis=1)
    df_relevant.to_json(paths['results_path'] / "df_relevant_pre_taxonomy.json", orient='records')

    if run_one_earth_taxonomy:
        df_relevant = add_one_earth_taxonomy(df_relevant, 'id', 'text_for_one_earth', use_cached_results=True)

    # PROCESS DIVERSITY TAGS
    _log_major_step("Adding Diversity Tags")
    cf.string2list(df_relevant, ['diversity'])  # format as lists
    df_relevant['diversity'] = df_relevant['diversity'].apply(lambda x: "|".join(x) if isinstance(x, list) else "")
    df_relevant['diversity'] = df_relevant['diversity'].apply(lambda x: cf.rename_tags(x, DIVERSITY_BIPOC_DICT))
    df_relevant['diversity'] = df_relevant['diversity'].apply(lambda x: "|".join(list(set(x.split("|")))))

    # Run Geotagging
    _log_major_step("Geotagging")
    # fill missing values in TEXT_FIELDS with empty strings
    df_relevant.fillna({col: "" for col in text_fields}, inplace=True)
    df_relevant = add_geotags(df_relevant, text_fields=text_fields)

    # Geocode the HQ
    _log_major_step("Geocoding")
    df_relevant = geocode.add_geo_lat_long(
        df_relevant,  # use file trimmed of <min search terms
        paths['geocode_name_orgs'],
        paths['geopath'],
        idCol="id",  # unique id column
        address="Location",  # address column
    )
    df_relevant = geocode.clean_geo(df_relevant, summarize_new_geo=False)

    # ADD CLIMATE KEYWORDS
    _log_major_step("Adding climate keywords using simple n-gram match")
    # load kwd mapping table (here it is master_term: [list of search terms])
    # terms used in database search
    df_climate_kwds = pd.read_excel(
        paths['common_kwds'] / "climate_kwd_map_byTag.xlsx", engine='openpyxl'
    )
    cf.string2list(
        df_climate_kwds,
        ['broad_tags', 'bigram', 'unigram', 'search_terms'] # format as lists
    )
    df_relevant = add_climate_keywords(
        df=df_relevant,
        keyword_path=paths['common_kwds'] / "climate_kwd_map_byTag.xlsx",
        paths=paths,
        df_climate_kwds=df_climate_kwds,
        text_fields=text_fields,
    )

    # SEPARATE EQUITY AND APPROACH TAGS
    _log_major_step("Separating 'climate equity' and 'approach' tags.")
    tag_attr = 'climate_kwds'
    equity = "Equity-Justice Mentions"

    equity_list = df_climate_kwds[df_climate_kwds.equity == 1].tag.tolist()
    approach_list = df_climate_kwds[df_climate_kwds.strategy == 1].tag.tolist()

    df_relevant[tag_attr].fillna("", inplace=True)
    df_relevant[equity] = df_relevant[tag_attr].apply(
        lambda x: "|".join([tag for tag in x.split("|") if tag in equity_list])
    )

    df_relevant["Approach Tags"] = df_relevant[tag_attr].apply(
        lambda x: "|".join([tag for tag in x.split("|") if tag in approach_list])
    )

    # strip equity and approach from main tags (minus tags flagged to keep with main tags)
    keep_list = df_climate_kwds[df_climate_kwds['eq_strat_keep'] == 1].tag.tolist()
    # set of tags to remove from main tags
    strip_tags = set(equity_list+approach_list) - set(keep_list)
    # remove weighted tags and renormalize weights
    tft.blacklist_wtd_tags(df_relevant, tag_attr, strip_tags)
    # remove also from pipe-separated tags
    df_relevant[tag_attr] = df_relevant[tag_attr].apply(
        lambda x: "|".join([tag for tag in x.split("|") if tag not in strip_tags])
    )

    # add 'climate equity' yes/no
    df_relevant[equity].fillna("", inplace=True)
    df_relevant["Any Equity-Justice Mention"] = df_relevant[equity].apply(
        lambda x: "no equity-justice mention" if x == "" else "equity-justice mention"
    )

    # ADD GRANT VS VENTURE
    # load mapping dictionaries
    df_funding_types = pd.read_excel(
        paths['common_kwds']/'funding_types_mapping.xlsx',
        engine='openpyxl',
    )
    venture_dict = dict(
        zip(df_funding_types.Cleaned_Funding_Type, df_funding_types.Grant_Venture)
    )
    df_relevant['Philanthropy vs Venture'] = df_relevant['Funding Stage'].map(venture_dict)
    # correct venture backed companies with grants
    df_relevant['Philanthropy vs Venture'] = (
        df_relevant
        .apply(
            lambda x: 'Venture'
            if (x['Philanthropy vs Venture'] == 'Philanthropy' and x['Type'] == "Private Company")
            else x['Philanthropy vs Venture'],
            axis=1,
        )
    )

    if run_process_images:
        # Add Logos
        _log_major_step("Adding Logos")
        df_relevant = images.add_profile_images(
            df_relevant,
            # name of file to store image urls
            paths['images_name'],
            paths['images_errors_name'],
            id_col='id',  # col for merging
            # local folder to hold image metadata files
            images_meta_path=paths['images_path'],
            name_col='Organization',  # use for image filename
            image_url='image_url',  # image source url
            # local directory to store image files
            image_directory=str(paths['images_path']) + "/image_files",
            # s3 bucket to store images
            bucket=paths['images_bucket'].stem,
            grayscale=False,  # convert to BW image
            load_existing=True,
        )
    else:
        df_relevant['Image_URL'] = ""

    df_relevant['uid'] = df_relevant.id

    logger.info(
        "\nWriting final file of %s US-based organizations enriched with metadata",
        len(df_relevant),
    )
    logger.info('\n df_relevant final\n%s', df_relevant['Data Source'].value_counts())
    cf.write_excel_no_hyper(df_relevant, paths['results_path']/'cb_cd_li_meta.xlsx')
    df_relevant.to_json(paths['results_path'] / "cb_cd_li_meta.json", orient='records')

    return df_relevant
