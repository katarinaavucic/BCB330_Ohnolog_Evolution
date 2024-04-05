#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

species = "potato"
df = pd.read_csv("./combined_embeddings/distance_df_" + species + ".fa.csv")
complete_mapping = pd.read_csv("./combined_embeddings/" + species + "_pairs.csv")

df_mut = df.copy()
df_mut['protein_ID'][1]
df_mut['protein_ID'] = df_mut['protein_ID'].str.extract(r'(\S+)')[0].to_list()
df_mut = df_mut.set_index("protein_ID")
df_mut.columns = df_mut.columns.str.extract(r'(\S+)')[0].to_list()
df_mut = df_mut.reset_index()

merge = pd.merge(complete_mapping, df_mut, left_on = ['Duplicate 1'], right_on = ['protein_ID'])

if 'Unnamed: 0' in merge.columns:
    merge = merge.drop(['Unnamed: 0'], axis=1)
merge['distance'] = merge.apply(lambda row: float(row.get(row['Duplicate 2'], np.nan)) if ('Duplicate 2' in row) and not pd.isna(row['Duplicate 2']) else np.nan, axis=1)
merge['rank'] = np.where(merge['distance'].isna(), np.nan, merge.drop(['Duplicate 1', 'Duplicate 2', 'protein_ID'], axis=1).lt(merge['distance'], axis=0).sum(axis=1))
merge['rank'].replace(0, 1, inplace=True)

columns_to_copy = ['Duplicate 1', 'Duplicate 2', 'distance', 'rank']
final = merge.loc[:, columns_to_copy]
final.to_csv("./combined_embeddings/" + species + "_paralog_dist_and_recip_rank.csv", index=False)
