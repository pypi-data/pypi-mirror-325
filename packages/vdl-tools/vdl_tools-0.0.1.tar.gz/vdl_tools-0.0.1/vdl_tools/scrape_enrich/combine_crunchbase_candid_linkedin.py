#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:13:00 2021

@author: ericberlow
"""

import pandas as pd
from shared_tools import common_functions as cf
from LinkedIn.utils.linkedin_url import extract_linkedin_id
import shared_tools.cb_funding_calculations as fcalc
from shared_tools.tools.falsey_checks import coerced_bool

# %% COMBINE CRUNCHBASE, CANDID, AND LINKEDIN DATA

def combine_cb_cd(df_cb,  # processed crunchbase data
                  df_cd,  # processed candid data
                  out_name,  # json filename to write combined results
                  funding_type_map_path  # shared-data path to funding type mapping file
                  ):
    ##########################################
    # COMBINE CRUNCHBASE WITH CANDID AND WRITE CLEANED FILE

    print("\nCOMBINING CRUNCHBASE and CANDID")
    df_cb_cd = pd.concat([df_cb, df_cd], ignore_index=True)
    df_cb_cd['Org Type'] = df_cb_cd['Org Type'].str.replace("Non-profit", "Nonprofit", regex=True)
    # deduce org type in CB based on  last_funding_type


    # clean funding stage tags and add funding stage order and category

    # load manual mappings of raw CB funding types to create mapping dictionaries
    df_fund_type_mapping = pd.read_excel(funding_type_map_path/"funding_types_mapping.xlsx")
    fundingDict = dict(zip(df_fund_type_mapping['api_funding_type'],
                           df_fund_type_mapping['Cleaned_Funding_Type']))  # clean raw CB funding stages

    # cleaned most recent funding stage
    df_cb_cd['Funding Stage'] = df_cb_cd['Funding Stage'].apply(lambda x: fundingDict.get(x, x))

    # add clean raw funding types
    df_cb_cd['Funding Types'].fillna('', inplace=True)
    df_cb_cd['Funding Types'] = df_cb_cd['Funding Types'].apply(
        lambda x: [fundingDict.get(tag.strip(), tag) for tag in (x if isinstance(x, list) else [x])]
        )

    df_cb_cd['Stage_Category'] = df_cb_cd['Funding Stage'] #.map(stageCategoriesDict)  # map stages to broader categories
    df_cb_cd['Stage_Category'].fillna('', inplace=True)
    # add philanthropy versus venture
    df_cb_cd['P_vs_V'] = df_cb_cd.apply(lambda x: fcalc.p_vs_venture(company_row=x), axis=1)

    # TODO: dedupe by aggregating that are in both datasets
    # df_cb_cd.drop_duplicates(subset='Organization', keep='first', inplace=True)

    df_cb_cd.to_json(out_name, orient='records')
    return df_cb_cd


def combine_cb_cd_li(df_cb_cd, df_li_orgs_scraped):
    #####################################################################
    # COMBINE LINKEDIN RESULTS WITH CRUNCHBASE AND CANDID METADATA
    # df_cb_cd = processed and combined raw crunchbase and candid data
    # df_li_orgs_scraped = processed and cleaned linked in scraping results


    li_cb_size_map = {"51-100": "51-500", # CB category
               "101-250": "51-500", # CB category
               "251-500": "51-500", # CB category
               "51-200": "51-500", # LI category
               "201-500":"51-500",  # LI category
               "0-1": "1-10", # LI category
               "2-10": "1-10", # LI category
               "1 employee": "1-10", # LI category
               }

    print("\nADDING LINKEDIN METADATA")

    # We can merge on this because when using Coresignal bulk we can't map the EXACT
    # original linkedin url to the retrieved linkedin url and so when there are differences
    # in `http` vs `https` or trailing `/` we miss the merges
    # This is a workaround to merge on the extracted linkedin id
    df_cb_cd['extracted_linkedin_id'] = df_cb_cd['LinkedIn'].apply(
        lambda x: extract_linkedin_id(x)
        if coerced_bool(x) else None
    )
    df_li_orgs_scraped['extracted_linkedin_id'] = df_li_orgs_scraped['original_id'].apply(
        lambda x: extract_linkedin_id(x)
        if coerced_bool(x) else None
    )

    # add linkedin to original metadata
    df_cb_cd_li = df_cb_cd.copy()
    if df_li_orgs_scraped is not None:
        # add 'success' flag to scraped results
        df_li_orgs_scraped['li_scrape'] = "successfully scraped"
        # merge with cb cd
        df_cb_cd_li = df_cb_cd.merge(
            df_li_orgs_scraped,
            left_on="extracted_linkedin_id",
            right_on='extracted_linkedin_id',
            how='left',
            suffixes=("_cb_cd", "_li")
        )
    else:
        print('LinkedIn data is empty, skipping...')

    # COMBINE CB, CD, and LI metadata for Enrichment
    # combine HQ locations (fill empty LI locations with CB/CD hq)
    if 'Location' not in df_cb_cd_li:
        df_cb_cd_li['Location'] = None

    def _fill_hq_location(row):
        if coerced_bool(row['hq_location']):
            return row['hq_location']
        else:
            return row['hq_address']

    df_cb_cd_li['Location'] = df_cb_cd_li.apply(_fill_hq_location, axis=1)

    # combine li sector and cb/cd sector tags
    df_cb_cd_li['Sector'] = cf.join_strings_no_missing(df_cb_cd_li, ['sectors_cb_cd'], delim="|")
    df_cb_cd_li['Sector'] = cf.clean_tags(df_cb_cd_li, 'Sector', delimeter="|")
    df_cb_cd_li['Sector'] = df_cb_cd_li['Sector'].fillna('')
    # clean rare sector tags
    print("Removing rare sector tags")
    df_cb_cd_li['Sector'], _ntags = cf.keep_tags_w_min_count(df_cb_cd_li, 'Sector', minCount=2)

    # add cleaned sectors to description for kwd search
    df_cb_cd_li['Description'] = cf.join_strings_no_missing(df_cb_cd_li, ['Description', 'Sector'], delim=" // Sectors: ")
    df_cb_cd_li['Description'] = df_cb_cd_li['Description'].astype(str).str.replace("\|", "; ", regex=True)

    # combine li industry and cb/cd industry tags
    df_cb_cd_li['Industry'] = cf.join_strings_no_missing(df_cb_cd_li, ['industry', 'industries_cb_cd'], delim="|")
    df_cb_cd_li['Industry'] = df_cb_cd_li['Industry'].astype(str).str.lower()
    df_cb_cd_li['Industry'] = cf.clean_tags(df_cb_cd_li, 'Industry', delimeter="|")
    # fill missing 'name' with Org
    df_cb_cd_li['profile_name'] = df_cb_cd_li['profile_name'].fillna(df_cb_cd_li['Organization'])

    # clean li company size for combining
    df_cb_cd_li['company_size'].fillna("", inplace=True)
    df_cb_cd_li['company_size'] = df_cb_cd_li['company_size'].str.replace(" employees", "", regex=True).str.replace(",", "", regex=True)
    # fill missing LI size with CB / CD data - assumption is that LI is the most accurate.
    df_cb_cd_li['company_size'] = df_cb_cd_li.apply(lambda x: x['n_Employees'] if x['company_size']=='' else x['company_size'], axis=1)
    # map different size categories onto common scale
    df_cb_cd_li['company_size'] = cf.find_replace_multi_from_dict_col(df_cb_cd_li, 'company_size', li_cb_size_map)
    df_cb_cd_li['company_size'].fillna('', inplace=True)
    df_cb_cd_li['company_size'] = df_cb_cd_li['company_size'].apply(lambda x: "no data" if x == '' else x)

    # fill missing  LI logo image with candid  or crunchbase logo image url
    df_cb_cd_li['image_url'] = df_cb_cd_li['image'].fillna(df_cb_cd_li['logo'])
    df_cb_cd_li.drop(['image'], axis=1, inplace=True)

    # fill missing  LI website with CB / CD website
    df_cb_cd_li['Website'] = df_cb_cd_li['website'].fillna(df_cb_cd_li['Website_cb_cd'])
    df_cb_cd_li.drop(['website'], axis=1, inplace=True)

    # clean all tag columns of empty's and dupes
    tagCols = ['Investors',
               'Donors',
               'Funding Types',
               'Founders',
               'Executives',
               'Board',
               'Sector',
               'Industry']
    df_cb_cd_li[tagCols] = df_cb_cd_li[tagCols].fillna('')
    df_cb_cd_li[tagCols] = cf.clean_tag_cols(df_cb_cd_li, tagCols, delimeter="|")
    return df_cb_cd_li