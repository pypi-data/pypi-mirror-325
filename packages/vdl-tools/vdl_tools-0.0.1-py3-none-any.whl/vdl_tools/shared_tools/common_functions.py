#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:13:00 2021

@author: ericberlow
"""

from ast import literal_eval
from typing import List
import os
import pathlib as pl
import pandas as pd
import numpy as np
from collections import OrderedDict, Counter
from functools import reduce
from operator import add

from vdl_tools.LinkedIn.utils.linkedin_url import extract_linkedin_id
import vdl_tools.shared_tools.cb_funding_calculations as fcalc
from vdl_tools.shared_tools.tools.falsey_checks import coerced_bool

import regex
from url_normalize import url_normalize


def str_converter(val):
    if type(val) == list:
        return val
    
    if val != '':
        return literal_eval(val)
    
    return []


def string2list(df, cols):
    # for df read from csv or excel that has list columns
    # convert list columns to lists (instead of strings of lists)
    for col in cols:
        df[col] = df[col].fillna('')
        df[col] = df[col].apply(str_converter)


def read_excel(fname, cols, sheet_name=0):
    """
    Read and excel and convert string columns that are python literals

    Parameters
    ----------
    fname : string
        name of an excel file.
    cols : list[str]
        list of columns ot convert.

    Returns
    -------
    df : pandas.DataFrame
        DataFrame read from file and with columns converted.

    """
    df = pd.read_excel(fname, sheet_name=sheet_name)
    string2list(df, cols)
    return df

def read_excel_wLists(fname, sheet_name=0):
    """
    Read and excel, detect string cols that are python literals and convert

    Parameters
    ----------
    fname : string
        name of an excel file.

    Returns
    -------
    df : pandas.DataFrame
        DataFrame read from file and with columns converted.

    """
    df = pd.read_excel(fname, sheet_name=sheet_name)
    list_cols = [col for col in df.columns if all('[' in str(x) for x in df[col])]
    string2list(df, list_cols)
    return df


def join_list_no_missing(df, cols):
    # cols is list of string columns to concatenate - and ignore missing values
    # returns a series
    df[cols] = df[cols].fillna("")
    df[cols] = df[cols].replace(
        r"^\s*$", np.nan, regex=True
    )  # replace empty string with nan
    joined_list = df[cols].apply(
        lambda x: list(x.dropna()), axis=1
    )  # join as a list without missing values
    return joined_list


def rename_tags(x, tag_dict):
    """
    Rename tags in list using a dictionary of new names.

    x is a list of tags
    Rename tags from a renaming dictionary
    If the tag is not in the dictionary, keep the old one
    Returns a new list of renamed tags
    """
    oldtaglist = x if type(x) is list else x.split("|")
    newtaglist = []
    for tag in oldtaglist:
        if tag.strip() in tag_dict:
            newtaglist.append(tag_dict[tag.strip()])
        else:
            newtaglist.append(tag)
    newtags = "|".join(t for t in newtaglist if type(t) == str)
    return newtags


def add_related_tags(x, add_tag_dict):
    """
    Add related tags from dictionary.

    x is a list of tags
    if tag is present, add related tags from dictionary
    Returns a new list of original tags with add related tags
    """
    taglist = x.split("|")
    for tag in taglist:
        if tag in add_tag_dict:
            addlist = add_tag_dict[tag].split(
                ", "
            )  # split comma separated list if more than one
            taglist.extend(addlist)
    newtags = "|".join(taglist)
    return newtags


def find_replace_multi_from_dict_col(df, col, replace_dict):
    # dictionary is mapping of existing strings to replacement strings
    # col is the column or strings to search and replace within
    for (
        string1,
        string2,
    ) in replace_dict.items():  # spell corrections dictionary for all TOG
        df[col] = df[col].str.replace(string1, string2)
    return df[col]  # return cleaned spelling


def find_replace_multi_from_dict(x, replace_dict):
    # dictionary is mapping of existing strings to replacement strings
    # x is string in a record
    for (
        string1,
        string2,
    ) in replace_dict.items():  # spell corrections dictionary for all TOG
        if x == string1:
            x = string2  # replace with string 2
    return x  # return cleaned spelling


def clean_empty_tags(df, col):
    # clean column of pipe-separated tags to remove blank ones
    tagseries = df[col].apply(lambda x: str(x).split("|"))
    tagseries = tagseries.apply(
        lambda x: [s.strip() for s in x if s]
    )  # strip empty spaces
    tagseries = tagseries.apply(lambda x: [s for s in x if s])  # keep if not empty
    tagseries = tagseries.apply(
        lambda x: [s for s in x if s != ""]
    )  # keep if not empty string
    tagseries = tagseries.apply(lambda x: "|".join(x))  # rejoin into liststring
    tagseries = tagseries.apply(
        lambda x: None if ((x == "") or (x == "nan")) else x
    )  # replace empty string with none
    return tagseries


def split(delimiters, string, maxsplit=0):
    # split on list of many delimeters
    regexPattern = "|".join(map(regex.escape, delimiters))
    return regex.split(regexPattern, string, maxsplit)


def striplist(lst):
    # strip empty spaces from a list of strings (e.g. list of tags after splitting)
    return [x.strip() for x in lst]


def compile_search_terms(df, col):
    # parse manually provided search terms, and compile unique ones into csv file
    # col is columns with free text search terms
    # return df with unique terms, counts, percents
    print("\nCompiling manual search terms and writing results")
    delimiters = [",", "/", "|", ":", ";", ".", "&", " and ", " or "]  # " as well as "]
    df[col].fillna("", inplace=True)
    df["term_list"] = df[col].apply(
        lambda x: split(delimiters, str(x).lower())
    )  # split on characters into list
    df["term_list"] = df["term_list"].apply(
        lambda x: striplist(x)
    )  # strip elements of empty spaces
    df["terms"] = df["term_list"].apply(lambda x: "|".join(x))  # join into tags
    # generate tag distribution  file
    df_searchterms = build_tag_hist_df(df, "terms")
    return df_searchterms


def build_tag_hist_df(df, col, delimiter="|", blacklist=[], mincnt=0):
    # generate dictionary of tags and tag counts for a column, exclude rows with no data
    # trim each dataset to tags with more than x nodes
    # blacklist = list of tags to ignore in counting
    # mincnt = min tag frequency to include
    print("generating tag histogram for %s" % col)
    total = len(df)
    tagDict = {}
    df[col].fillna("", inplace=True)
    # convert to list and strip empty spaces for each item in each list
    tagLists = df[col].str.split(delimiter).apply(lambda x: [ss.strip(" ") for ss in x])
    # remove any blacklisted tags
    tagLists = tagLists.apply(lambda x: [t for t in x if t not in blacklist])
    tagHist = OrderedDict(
        Counter([t for tags in tagLists for t in tags if t != ""]).most_common()
    )
    tagDict[col] = list(tagHist.keys())
    tagDict["count"] = list(tagHist.values())
    tagdf = pd.DataFrame(tagDict)
    tagdf["percent"] = tagdf["count"].apply(lambda x: np.round((100 * (x / total)), 2))
    tagdf = tagdf[tagdf["count"] > mincnt]  # remove infrequent tags
    return tagdf


def clean_tagseries(tagseries, delimeter="|"):
    # remove empty tags and duplicates reformat as pipe-separated string of unique tags
    tagseries = tagseries.astype(str).str.split(delimeter)  # convert tag string to list
    tagseries = tagseries.apply(
        lambda x: [s.strip() for s in x if len(s) > 0]
    )  # remove spaces and empty elements - list comprehension
    tagseries = tagseries.apply(
        lambda x: delimeter.join(list(set(x)))
    )  # get unique tags, and join back into string of tags
    return tagseries


def clean_tags(df, tagCol, delimeter="|"):
    # remove empty tags and duplicates reformat as pipe-separated string of unique tags
    # returns tag column
    df[tagCol] = df[tagCol].astype(str).str.split(delimeter)  # convert tag string to list
    df[tagCol] = df[tagCol].apply(
        lambda x: [s.strip() for s in x if len(s) > 0]
    )  # remove spaces and empty elements - list comprehension
    df[tagCol] = df[tagCol].apply(
        lambda x: delimeter.join(list(set(x)))
    )  # get unique tags, and join back into string of tags
    return df[tagCol]


def clean_tag_cols(df, tagCols, delimeter="|"):
    # for a list of multiple tag columns (tagCols)
    # remove empty tags and duplicates reformat as pipe-separated string of unique tags
    # returns cleaned tag columns
    for col in tagCols:
        df[col] = clean_tags(df, col, delimeter)
    return df[tagCols]


def merge_dupes(df, groupVars, pickOneCols, tagCols, stringCols):
    # merge records of duplicate entities
    # pickOneCols - select first answer
    # tagCols - join as pipe-separated list of tags
    # stringCols - join strings with comma
    print("\nMerging duplicates")

    # clean a text columsn missing values
    df[stringCols + tagCols] = df[stringCols + tagCols].fillna("").astype(str)

    # build aggregation operations
    agg_data = {
        col: (lambda x: "|".join(x)) for col in tagCols
    }  # join as 'tags' separated by pipe
    agg_data.update({col: "first" for col in pickOneCols})
    agg_data.update({col: (lambda x: ", ".join(x)) for col in stringCols})
    agg_data.update({"count": "sum"})
    # group and aggregate
    df_merged = df.groupby(groupVars).agg(agg_data).reset_index()
    # clean tags
    df_merged[tagCols] = clean_tag_cols(df_merged, tagCols, delimeter="|")
    df_merged[stringCols] = clean_tag_cols(df_merged, stringCols, delimeter=", ")

    return df_merged


def blacklist_tags_old_slow(df, tagcol, blacklist):
    """ this function removes a list of tags from a string of pipe-separated tags
    'tagcol' = column with pipe-separated strings
    'blacklist' = list of tags to remove
    """
    tagset = tagcol + "_set"  # name new column of tag attribute converted into set
    # convert pipe-separated string to set of tags
    df[tagset] = df[tagcol].apply(lambda x: set(x.split("|") if isinstance(x,str) else {}))
    # remove blacklist tags
    df[tagset] = df[tagset].apply(
        lambda x: x - set(blacklist)
    )
    # update tag counts with length of new set
    df["n_" + tagcol] = df[tagset].apply(lambda x: len(x) if x and list(x)[0] != "" else 0)
    # rejoin tags into string with blacklist removed
    df[tagcol] = df[tagset].apply(lambda x: "|".join(list(x)) if len(x) > 0 else "")
    return df[tagcol], df["n_" + tagcol]

def blacklist_tags(df, tagcol, blacklist):
    """
    This function removes a list of tags from a string of pipe-separated tags
    'tagcol' = column with pipe-separated strings
    'blacklist' = list of tags to remove
    """
    blacklist_set = set(blacklist)  # Convert blacklist to set for faster lookup

    # Split the pipe-separated strings into lists
    tags_lists = df[tagcol].fillna("").str.split("|")

    # Remove blacklist tags from each list
    filtered_tags_lists = tags_lists.apply(lambda tags: [tag for tag in tags if tag not in blacklist_set])

    # Calculate the number of remaining tags
    n_tags = filtered_tags_lists.str.len()

    # Join the filtered tags back into pipe-separated strings
    filtered_tags = filtered_tags_lists.apply(lambda tags: "|".join(tags))

    # Update the DataFrame with the new tags and tag counts
    df[tagcol] = filtered_tags
    df["n_" + tagcol] = n_tags

    return df[tagcol], df["n_" + tagcol]

def blacklist_wtd_tags(df, tagcol, blacklist):
    # make tuple lists from _list and _wts columns
    kwd_wts = df.apply(lambda x: list(zip(x[tagcol + '_list'], x[tagcol + '_wts'])), axis=1)
    # update keyword list
    df[tagcol + '_list'] = kwd_wts.apply(lambda x: [val[0] for val in x if val[0] not in blacklist])
    # update weights by removing and then renormalizing
    df[tagcol + '_wts'] = kwd_wts.apply(lambda x: np.array([val[1] for val in x if val[0] not in blacklist]))
    df[tagcol + '_wts'] = df[tagcol + '_wts'] .apply(lambda x: list(x / x.sum()))
    # rebuild pipe-separated list
    df[tagcol] = df[tagcol + '_list'].apply(lambda x: "|".join(x))
    # recompute counts after thinning
    df['n_' + tagcol] = df[tagcol + '_list'].apply(lambda x: len(x))

def write_excel_no_hyper(df, outname):
    '''
    write to excel without converting strings to hyperlinks
    '''
    # make sure folders exist
    create_folders(outname)
    # write to excel without converting strings to hyperlinks
    writer = pd.ExcelWriter(outname, engine="xlsxwriter")  # ,
    # Don't convert url-like strings to urls.
    writer.book.strings_to_urls = False
    df.to_excel(writer, index=False)
    writer.close()


def add_nodata(df, col_list, filltext="no data"):
    # fill empty tags with 'no data'
    for col in col_list:
        df[col].fillna("no data", inplace=True)
        df[col] = df[col].apply(lambda x: filltext if x == "" else x)


def rename_strings(df, col, renameDict):
    # find and replace for multiple strings from dictionary
    for string1, string2 in renameDict.items():  # renaming dictionary
        df[col] = df[col].str.replace(string1, string2)
    return df[col]  # return cleaned recipient spelling


def normalize_linkedin_urls(df, li_url, li_fix_dict={}):
    # li_url = column that has linkedin url
    # li_fix_dict = optional manual dictionary of spelling corrections
    # returns columns of cleaned urls

    # remove long suffix
    df[li_url] = df[li_url].apply(lambda x: x.split("?")[0])
    df[li_url] = (
        df[li_url].str.lower().str.strip()
    )  # make all lower case, remove any trailing space
    # normlize url format
    df[li_url] = df[li_url].apply(
        lambda x: url_normalize(x)
    )  # automated url normalizer
    df[li_url] = df[li_url].fillna("")
    df[li_url] = df[li_url].apply(
        lambda x: ("https://www.linkedin" + x.split("linkedin")[-1]) if x != "" else ""
    )  # standardize prefixc
    df[li_url] = df[li_url].str.replace(
        "https://linkedin", "https://www.linkedin", regex=True
    )  # add www for consistency
    df[li_url] = df[li_url].str.lower()  # make all lowercase
    df[li_url] = df[li_url].str.replace(
        "company/company", "company", regex=True
    )  # remove duplicates (candid data error)
    df[li_url] = df[li_url].apply(lambda x: x.split("mycompany")[0])
    df[li_url] = df[li_url].apply(
        lambda x: "" if x == "" else x + "/" if x[-1] != "/" else x
    )  # make sure all end with "/"
    df[li_url] = df[li_url].str.replace(
        "/about/", "/", regex=True
    )  # remove 'about' from company urls
    # fix known bad url spellings
    df[li_url] = find_replace_multi_from_dict_col(df, li_url, li_fix_dict)
    # remove mobile app indicator
    df[li_url] = df[li_url].str.replace("mwlite/", "")
    return df[li_url]


def get_keywords_path():
    _dir, _filename = os.path.split(__file__)
    return pl.Path(_dir) / ".." / "keywords"


def create_folders(fname):
    pl.Path(fname).parent.mkdir(parents=True, exist_ok=True)


def join_strings_no_missing(df: pd.DataFrame, cols: List[str], delim="|"):
    # cols is list of string columns to concatenate - and ignore missing values
    # returns a series
    df = df.copy()

    df[cols] = df[cols].fillna("")
    df[cols] = df[cols].replace(
        r"^\s*$", np.nan, regex=True
    )  # replace empty string with nan
    joined_strings = df[cols].apply(
        lambda x: delim.join(x.dropna().astype(str)), axis=1
    )
    return joined_strings


def build_custom_list_from_tags(x, tagDict):
    '''
    x is a list of tags
    Rename tags from a renaming dictionary
    If the tag is not in the dictionary, DON'T KEEP IT
    Returns a new list of replaced tags
    '''
    oldtaglist = x.split("|")
    newtaglist = []
    for tag in oldtaglist:
        if tag in tagDict:
            newtaglist.append(tagDict[tag])
    # newtags = "|".join(newtaglist)
    return newtaglist


def clean_empty_list_elements(df, listcol):
    # clean list of empty elements
    df[listcol] = df[listcol].apply(lambda x: [s.strip() for s in x if s])  # strip empty spaces
    df[listcol] = df[listcol].apply(lambda x: [s for s in x if s])  # keep if not empty
    df[listcol] = df[listcol].apply(lambda x: [s for s in x if s != ''])  # keep if not empty string
    df[listcol] = df[listcol].apply(lambda x: list(set(x)))  # remove duplicates
    df[listcol] = df[listcol].apply(lambda x: None if x == '' else x)  # replace empty string with none
    return df[listcol]


def keep_tags_w_min_count(df, tag_attr, minCount=2):
    print("Keeping tags that occur at least %s times" % str(minCount))
    # trim tags to ones that occur at least n times in the entire dataset
    # udpate tag counts for each row

    # across entire dataset, count tag hist and remove singleton tags
    df[tag_attr].fillna('', inplace=True)
    taglists = df[tag_attr].apply(lambda x: x.split("|"))
    # build master histogram of tags that occur at least min count times
    tagHist = dict([item for item in
                    Counter([k for kwList in taglists for k in kwList]).most_common() if item[1] >= minCount])
    # filter tags in each row to ones that are in this global 'active' tags set
    taglists = taglists.apply(lambda x: [k for k in x if k in tagHist])
    # join list back into string of unique pipe-sepparated tags
    taglists = taglists.apply(lambda x: "|".join(list(set(x))))
    # update tag counts
    nTags = taglists.apply(lambda x: len(x.split("|")) if x else 0)
    return taglists, nTags


def clean_spaces_linebreaks_all(df):
    # remove any line breaks, tabs, carriage returns
    try:
        df.replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["", ""], regex=True, inplace=True)
        df.replace('\s+', ' ', regex=True, inplace=True)  # replace repeated spaces with one
    except Exception as ex:
        print(ex)
        raise ex


def clean_spaces_linebreaks_col(df: pd.DataFrame, col: str):
    # remove any line breaks, tabs, carriage returns
    df[col].replace(to_replace=[r"\\t|\\n|\\r", "\t|\n|\r"], value=["", ""], regex=True, inplace=True)
    df[col].replace('\s+', ' ', regex=True, inplace=True)  # replace repeated spaces with one


def write_network_to_excel(ndf, ldf, outname):
    writer = pd.ExcelWriter(outname, engine='openpyxl')
    # Don't convert url-like strings to urls.
    writer.book.strings_to_urls = False
    ndf.to_excel(writer, 'Nodes', index=False)
    ldf.to_excel(writer, 'Links', index=False)
    writer.close()


def write_network_to_excel_simple(ndf, ldf, outname):
    writer = pd.ExcelWriter(outname)
    ndf.to_excel(writer, 'Nodes', index=False)
    ldf.to_excel(writer, 'Links', index=False)
    writer.close()


def normalized_difference(df, attr):
    # compute normalizd difference relative to the mean
    avg_attr = df[attr].mean()
    normalized_diff = ((df[attr]-avg_attr)/(df[attr]+avg_attr)).round(4)
    return normalized_diff


def max_min_normalize(df, attr):
    max_min = (df[attr]-df[attr].min())/(df[attr].max()-df[attr].min())
    return max_min


def explode_chunks(df, chunk_col, chunk='chunk'):
    # explode chunks into separate rows
    print("exploding chunks")
    df_chunked = df[['id', chunk_col]].explode(chunk_col)
    df_chunked.columns = ['id', chunk]
    empty = ((df_chunked[chunk] == '') | (df_chunked[chunk] == ' ')
             | (df_chunked[chunk] == '  ') | (df_chunked[chunk] == '   '))
    df_chunked = df_chunked[~empty].reset_index(drop=True)
    # add global id and ordered id for each chunk wthin each person
    df_chunked[chunk + '_id'] = range(0, len(df_chunked))  # unique id for each chunk
    df_chunked[chunk + '_order'] = df_chunked.groupby(['id']).cumcount()  # numbered id within each person
    return df_chunked


def generate_sponsor_tuples(df, sponsors):
    # create list of sponsor logos etc
    # as list of tuples [(link_title, icon_url, link_url)]
    # df: spreadsheet with sponsor info
    # sponsors: list of sponsor names
    sponsor_tuple_list = []
    for sponsor in sponsors:
        sponsor_tuple = (df.loc[df['link_title'] == sponsor]['link_title'].tolist()[0],
                         df.loc[df['link_title'] == sponsor]['icon_url'].tolist()[0],
                         df.loc[df['link_title'] == sponsor]['link_url'].tolist()[0])
        sponsor_tuple_list.append(sponsor_tuple)
    return sponsor_tuple_list


def sort_weighted_kwds(df, attr):
    li_attr = attr + '_list'
    wt_attr = attr + '_wts'

    def sort_row(row):
        kwd_idx = np.argsort(np.array(row[wt_attr]))[::-1]
        row[li_attr] = np.array(row[li_attr])[kwd_idx].tolist()
        row[wt_attr] = np.array(row[wt_attr])[kwd_idx].tolist()
    df.apply(sort_row, axis=1)


def threshold_weighted_kwds(df, attr, min_relative_wt=0.1, min_cnt=10):
    li_attr = attr + '_list'
    wt_attr = attr + '_wts'

    def threshold_row(row):
        wts = np.array(row[wt_attr])
        if len(wts) > 0:
            # keep if bigger than relative threshold
            keep = (wts / wts[0]) > min_relative_wt
            # keep at least min count
            keep[0:min(10, len(keep))] = True
            # mask to get kept values
            row[wt_attr] = wts[keep].tolist()
            row[li_attr] = np.array(row[li_attr])[keep].tolist()
        else:
            print(f"{row['name']} has no keywords")
    if min_relative_wt > 0 and min_cnt > 0:
        df.apply(threshold_row, axis=1)



def aggregate(df,
              groupCols,         # list of columns to grouby
              tagCols=[],        # list of columns to aggregate as tags
              txtCols=[],        # list of text columns to concatenate with " // " delimeter
              pickFirstCols=[],  # list of columns to just pick first one
              sumCols=[],        # list of columns to get sum
              maxCols=[],        # list of columns to get max
              meanCols=[],       # list of columns to get mean
              countCols=[],       # list of columns to get count
              ):
    # build aggregation operations
    agg_data = {col: (lambda x: '|'.join(x)) for col in tagCols}  # join as 'tags' separated by pipe
    agg_data.update({col: (lambda x: ' // '.join(x)) for col in txtCols})  # join as 'tags' separated by pipe
    agg_data.update({col: 'first' for col in pickFirstCols})
    agg_data.update({col: 'sum' for col in sumCols})
    agg_data.update({col: 'max' for col in maxCols})
    agg_data.update({col: 'mean' for col in meanCols})
    agg_data.update({col: 'count' for col in countCols})

    # fill empty tags
    for col in tagCols:
        df[col].fillna('', inplace=True)
    # group and aggregate
    df_agg = df.groupby(groupCols).agg(agg_data).reset_index()
    # clean tags
    df_agg[tagCols] = clean_tag_cols(df_agg, tagCols, delimeter="|")
    df_agg[txtCols] = clean_tag_cols(df_agg, txtCols, delimeter=" // ")
    return df_agg


def aggregate_cat_fracs(df,
                        groupCols,  # list of columns to groupby
                        attr,  # column with value compute % (e.g. 'org typ')
                        value,  # value to tally if present (e.g. 'non-profit')
                        ):
    """creates fractions of values occurrence of strings/ categories within columns for groupby summaries"""
    df[attr].fillna('', inplace=True)
    df_count = df.groupby(groupCols).agg(
        {attr: [('Count_total', 'count'), (value + '_Count', lambda x: sum(x.str.contains(value)))]}).reset_index()
    df_count.columns = ['_'.join(col) for col in df_count.columns.values]
    df_count[value + '_frec'] = df_count[attr + '_' + value + '_Count'] / df_count[attr + '_Count_total']
    for i in range(len(groupCols)):
        col = df_count.columns[i]
        df_count.rename(columns={col: col.rstrip(col[-1])}, inplace=True)
    df_count = df_count.drop(columns=[attr + '_' + value + '_Count', attr + '_Count_total'])
    return df_count


def aggregate_and_fracs(df,
                        groupCols,  # list of columns to grouby
                        tagCols=[],  # list of columns to aggregate as tags
                        txtCols=[],  # list of text columns to concatenate with " // " delimeter
                        text_delim=" // ",  # custom delimeter for text concatenation
                        pickFirstCols=[],  # list of columns to just pick first one
                        sumCols=[],  # list of columns to get sum
                        maxCols=[],  # list of columns to get max
                        meanCols=[],  # list of columns to get mean
                        countCols=[],  # list of columns to get count
                        fracList=[],  # list of tuples with attr and value to get fractions
                        wtd_kwds=None  # tag that has associated weights that need to be aggregated
                        ):
    """similar to aggregate, but with added fractions of values occurrence within columns for groupby summaries"""
    # build aggregation operations
    # join as 'tags' separated by pipe
    agg_data = {col: (lambda x: '|'.join(x)) for col in tagCols}
    # join as 'tags' separated by custom delimeter
    agg_data.update({col: (lambda x: text_delim.join(x)) for col in txtCols})
    agg_data.update({col: 'first' for col in pickFirstCols})
    agg_data.update({col: 'sum' for col in sumCols})
    agg_data.update({col: 'max' for col in maxCols})
    agg_data.update({col: 'mean' for col in meanCols})
    agg_data.update({col: 'count' for col in countCols})

    for col in tagCols:
        df[col].fillna('', inplace=True)

    # group and aggregate
    grps = df.groupby(groupCols[0] if len(groupCols) == 1 else groupCols)
    df_agg = grps.agg(agg_data).reset_index()
    # clean tags
    df_agg[tagCols] = clean_tag_cols(df_agg, tagCols, delimeter="|")
    df_agg[txtCols] = clean_tag_cols(df_agg, txtCols, delimeter=text_delim)

    # add fractions from fracList tuples
    for x in fracList:
        (attr, value) = x[0], x[1]
        df_frac = aggregate_cat_fracs(df, groupCols, attr, value)
        df_agg = df_agg.merge(df_frac, on=groupCols, how='left')

    # aggregate weighted keywords across each group
    def sum_dict_list(li):
        agg_vals = reduce(add, (map(Counter, li)))
        vals = np.array(list(agg_vals.values()))
        norm_vals = vals / vals.sum()
        return list(zip(agg_vals.keys(), norm_vals))

    if wtd_kwds is not None:
        li_attr = wtd_kwds + '_list'
        wt_attr = wtd_kwds + '_wts'
        results = {}
        for idx, _df in grps:
            if len(_df) == 1:
                results[idx] = list(zip(_df[li_attr].iloc[0], _df[wt_attr].iloc[0]))
            else:
                # print(idx)
                kwd_wts = _df.apply(lambda x: dict(zip(x[li_attr], x[wt_attr])), axis=1)
                results[idx] = sum_dict_list(kwd_wts.values.tolist())
        if len(groupCols) > 1:
            df_frac = pd.DataFrame([({gc: k[idx] for idx, gc in enumerate(groupCols)} | {'kwd_wts': v})
                                    for k, v in results.items()])
        else:
            df_frac = pd.DataFrame([{groupCols[0]: k, 'kwd_wts': v} for k, v in results.items()])
        df_frac[li_attr] = df_frac['kwd_wts'].apply(lambda x: [val[0] for val in x])
        df_frac[wt_attr] = df_frac['kwd_wts'].apply(lambda x: [val[1] for val in x])
        df_agg = df_agg.merge(df_frac.drop(columns=['kwd_wts']), on=groupCols, how='left')
        sort_weighted_kwds(df_agg, wtd_kwds)
    return df_agg


# %% COMMON FUNCTIONS TO COMBINE CRUNCHBASE, CANDID, AND LINKEDIN DATA
# NOTE THIS WAS MOVED TO: scrape_enrich/combine_crunchbase_candid_linkedin.py and should be removed from here
'''
def combine_cb_cd(df_cb, df_cd, outname, common_kwds_path, use_api_funding_type=False):
    ##########################################
    # COMBINE CRUNCHBASE WITH CANDID AND WRITE CLEANED FILE
    # df_cb = processed crunchbase data
    # df_cd = processed candid data
    # returns combined results
    # outname = filename to write combined results
    print("\nCOMBINING CRUNCHBASE and CANDID")
    df_cb_cd = pd.concat([df_cb, df_cd], ignore_index=True)
    df_cb_cd['Org Type'] = df_cb_cd['Org Type'].str.replace("Non-profit", "Nonprofit", regex=True)
    # deduce org type in CB based on  last_funding_type


    # clean funding stage tags and add funding stage order and category

    # load manual mappings of raw CB fundinng types to create mapping dictionaries
    df_fundtype_mapping = pd.read_excel(common_kwds_path/"funding_types_mapping.xlsx", engine='openpyxl')
    fundingDict = dict(zip(df_fundtype_mapping['api_funding_type' if use_api_funding_type else 'CB_Funding_Type'],
                           df_fundtype_mapping['Cleaned_Funding_Type']))  # clean raw CB funding stages

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
    # add non-equity funding

    # TODO: dedupe by aggregating that are in both datasets
    # df_cb_cd.drop_duplicates(subset='Organization', keep='first', inplace=True)

    write_excel_no_hyper(df_cb_cd, outname)
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
               "2-10": "1-10" # LI category
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
    df_cb_cd_li['Sector'] = join_strings_no_missing(df_cb_cd_li, ['sectors_cb_cd'], delim="|")
    df_cb_cd_li['Sector'] = clean_tags(df_cb_cd_li, 'Sector', delimeter="|")
    df_cb_cd_li['Sector'] = df_cb_cd_li['Sector'].fillna('')
    # clean rare sector tags
    print("Removing rare sector tags")
    df_cb_cd_li['Sector'], _ntags = keep_tags_w_min_count(df_cb_cd_li, 'Sector', minCount=2)

    # add cleaned sectors to description for kwd search
    df_cb_cd_li['Description'] = join_strings_no_missing(df_cb_cd_li, ['Description', 'Sector'], delim=" // Sectors: ")
    df_cb_cd_li['Description'] = df_cb_cd_li['Description'].astype(str).str.replace("\|", "; ", regex=True)

    # combine li industry and cb/cd industry tags
    df_cb_cd_li['Industry'] = join_strings_no_missing(df_cb_cd_li, ['industry', 'industries_cb_cd'], delim="|")
    df_cb_cd_li['Industry'] = df_cb_cd_li['Industry'].astype(str).str.lower()
    df_cb_cd_li['Industry'] = clean_tags(df_cb_cd_li, 'Industry', delimeter="|")
    # fill missing 'name' with Org
    df_cb_cd_li['profile_name'] = df_cb_cd_li['profile_name'].fillna(df_cb_cd_li['Organization'])

    # clean li company size for combining
    df_cb_cd_li['Company size'] = df_cb_cd_li['company_size'].astype(str)\
        .str.replace(" employees", "", regex=True).str.replace(",", "", regex=True)
    df_cb_cd_li.drop(['company_size'], axis=1, inplace=True)
    # fill missing LI with CB / CD categories
    df_cb_cd_li['Company size'].fillna(df_cb_cd_li['n_Employees'], inplace=True)
    # map different size categories onto common scale
    df_cb_cd_li['Company size'] = find_replace_multi_from_dict_col(df_cb_cd_li, 'Company size', li_cb_size_map)
    df_cb_cd_li['Company size'].fillna('', inplace=True)
    df_cb_cd_li['Company size'] = df_cb_cd_li['Company size'].apply(lambda x: "no data" if x == '' else x)

    # fill missing  LI logo image with candid logo image url
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
    df_cb_cd_li[tagCols] = clean_tag_cols(df_cb_cd_li, tagCols, delimeter="|")
    return df_cb_cd_li
'''