import pandas as pd

import vdl_tools.shared_tools.project_config as pc
import vdl_tools.shared_tools.taxonomy_mapping.taxonomy_mapping as tm
from vdl_tools.shared_tools.tools.logger import logger


def add_one_earth_taxonomy(
    df,
    id_col,
    text_col,
    name_col='Organization',
    run_fewshot_classification=True,
    filter_fewshot_classification=True,
    use_cached_results=True,
    paths=None,
    max_workers=3,
):

    paths = paths or pc.get_paths()
    if filter_fewshot_classification and not run_fewshot_classification:
        raise ValueError("Cannot filter few shot classification if it is not run")

    pillar_df = pd.read_excel(paths["one_earth_taxonomy"], sheet_name="Pillars")
    sub_df = pd.read_excel(paths["one_earth_taxonomy"], sheet_name="SubPillars")
    soln_df = pd.read_excel(paths["one_earth_taxonomy"], sheet_name="Solutions")
    energy_term_df = pd.read_excel(paths["one_earth_taxonomy"], sheet_name="Energy").fillna(method='ffill')
    ag_term_df = pd.read_excel(paths["one_earth_taxonomy"], sheet_name="Regenerative Ag").fillna(method='ffill')
    nature_term_df = pd.read_excel(paths["one_earth_taxonomy"], sheet_name="Nature Conservation").fillna(method='ffill')

    # Concatenate sub-term sheets into a single subterm dataframe
    term_df = pd.concat([energy_term_df, ag_term_df, nature_term_df])

    term_df = term_df[term_df['Exclude'] != 1].copy()
    term_df.drop(columns=['Exclude'], inplace=True)

    taxonomy = [
        {'level': 0, 'name': 'Pillar', 'data': pillar_df, 'textattr': 'Definition'},
        {'level': 1, 'name': 'Sub-Pillar', 'data': sub_df, 'textattr': 'Definition'},
        {'level': 2, 'name': 'Solution', 'data': soln_df, 'textattr': 'Definition'},
        {'level': 3, 'name': 'ST_Name', 'data': term_df, 'textattr': 'ST_Description'}
    ]

    entity_embeddings = tm.get_or_compute_embeddings(
        org_df=df,
        id_col=id_col,
        text_col=text_col,
        max_workers=max_workers,
    )

    all_df, _ = tm.get_entity_categories(
        df,
        taxonomy,
        id_attr=id_col,
        name_attr=name_col,
        nmax=5,
        thr=90,
        pct_delta=1,
        entity_embeddings=entity_embeddings,
        max_workers=max_workers,
    )
    if run_fewshot_classification:
        all_df = tm.run_fewshot_classification(
            all_df=all_df,
            id_col=id_col,
            text_col=text_col,
            taxonomy=taxonomy,
            reranked_relevancy_col='reranked_relevancy',
            use_cached_results=use_cached_results,
            max_workers=max_workers
        )
        if filter_fewshot_classification:
            filtered_all_df = all_df[all_df['reranked_relevancy']].copy()
            filtered_all_df = tm.distribute_entity_funding(filtered_all_df, id_col)
            all_df = all_df.merge(
                filtered_all_df[['taxonomy_mapping_id', 'FundingFrac']],
                on='taxonomy_mapping_id',
                how='left',
                suffixes=('', '_filtered')
            )
            all_df['FundingFrac_filtered'].fillna(0, inplace=True)

    # reduce the number of columns in the output
    original_columns = set(df.columns)
    # Keep all the new columns
    new_columns = list(all_df.columns.difference(original_columns))
    keep_columns = [id_col, name_col, text_col] + new_columns
    all_df[keep_columns].to_json(paths["one_earth_taxonomy_mapping_results"], orient='records')

    # Remove this column from the output since it is calculated before re-ranking
    filtered_all_df.pop('FundingFrac')
    distributed_funding_df = tm.redistribute_funding_fracs(
        df=filtered_all_df,
        taxonomy=taxonomy,
        id_attr='id',
        keepcols=['Organization'],
    )
    distributed_funding_df.to_json(
        paths["oe_tax_mapping_distributed_funding_results"],
        orient='records'
    )

    cols = ['mapped_category', 'cat_level', 'level0', 'level1', 'level2', 'level3']
    new_cft_df = tm.add_mapping_to_orgs(df, filtered_all_df, id_col, cats=cols)

    return new_cft_df


def add_tailwind_taxonomy(
    df,
    id_col,
    text_col,
    name_col='Organization',
    run_fewshot_classification=True,
    filter_fewshot_classification=True,
    use_cached_results=True,
    paths=None,
    mapped_category_col='category',
    max_workers=3,
):

    paths = paths or pc.get_paths()
    if filter_fewshot_classification and not run_fewshot_classification:
        raise ValueError("Cannot filter few shot classification if it is not run")

    theme_df = pd.read_excel(paths["tailwind_taxonomy"], sheet_name="Themes")
    sector_df = pd.read_excel(paths["tailwind_taxonomy"], sheet_name="Sectors")
    examples_df = pd.read_excel(paths["tailwind_taxonomy"], sheet_name="Examples")

    #add prefix to the columns and combine sector-examples to be unique
    prefix = 'TW-'
    theme_df['Theme'] = prefix + theme_df['Theme']
    sector_df['Theme'] = prefix + sector_df['Theme']
    sector_df['Sector'] = prefix + sector_df['Sector']
    examples_df['Theme'] = prefix + examples_df['Theme']
    examples_df['Sector'] = prefix + examples_df['Sector']
    examples_df['Examples'] = examples_df['Sector'] + '-' + examples_df['Examples']

    taxonomy = [
        {'level': 0, 'name': 'Theme', 'data': theme_df, 'textattr': 'Theme Definition'},
        {'level': 1, 'name': 'Sector', 'data': sector_df, 'textattr': 'revised_definition'},
        {'level': 2, 'name': 'Examples', 'data': examples_df, 'textattr': 'gpt_definition'},
        ]

    entity_embeddings = tm.get_or_compute_embeddings(
        org_df=df,
        id_col=id_col,
        text_col=text_col,
    )

    all_df, _ = tm.get_entity_categories(
        df,
        taxonomy,
        id_attr=id_col,
        name_attr=name_col,
        nmax=5,
        thr=90,
        pct_delta=2,
        entity_embeddings=entity_embeddings,
        max_level=1
    )
    if run_fewshot_classification:
        all_df = tm.run_fewshot_classification(
            all_df=all_df,
            id_col=id_col,
            text_col=text_col,
            taxonomy=taxonomy,
            reranked_relevancy_col='reranked_relevancy',
            use_cached_results=use_cached_results,
            max_workers=max_workers,
            mapped_category_col=mapped_category_col,
        )
        if filter_fewshot_classification:
            filtered_all_df = all_df[all_df['reranked_relevancy']].copy()
            filtered_all_df = tm.distribute_entity_funding(filtered_all_df, id_col)
            all_df = all_df.merge(
                filtered_all_df[['taxonomy_mapping_id', 'FundingFrac']],
                on='taxonomy_mapping_id',
                how='left',
                suffixes=('', '_filtered')
            )
            all_df['FundingFrac_filtered'].fillna(0, inplace=True)
    # reduce the number of columns in the output
    original_columns = set(df.columns)
    # Keep all the new columns
    new_columns = list(all_df.columns.difference(original_columns))
    keep_columns = [id_col, name_col, text_col] + new_columns
    all_df.to_json(paths["tailwind_taxonomy_mapping_results"], orient='records')

    # Remove this column from the output since it is calculated before re-ranking
    filtered_all_df.pop('FundingFrac')
    distributed_funding_df = tm.redistribute_funding_fracs(
        df=filtered_all_df,
        taxonomy=taxonomy,
        max_level=1,
        id_attr='id',
        keepcols=['Organization', 'Stage_Category'],

    )
    distributed_funding_df.to_json(
        paths["tw_tax_mapping_distributed_funding_results"],
        orient='records'
    )

    cols = ['mapped_category', 'cat_level', 'level0', 'level1', 'level2']
    new_cft_df = tm.add_mapping_to_orgs(df, filtered_all_df, id_col, cats=cols)

    return new_cft_df