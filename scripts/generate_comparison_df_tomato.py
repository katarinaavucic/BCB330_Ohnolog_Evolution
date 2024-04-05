#!/usr/bin/env python
# coding: utf-8

import pandas as pd

df = pd.read_csv("./combined_embeddings/distance_df_SlycHeinz4.0.pep.fa.csv")
#mapping = pd.read_csv("./combined_embeddings/tomato_Heinz_paralogs_classification.csv")
complete_mapping = pd.read_csv("./Slyc4_transposed_pairs.csv")

df_mut = df.copy()
df_mut['protein_ID'] = df_mut['protein_ID'].str.extract(r'([^\.]+)')[0].to_list()
df_mut = df_mut.set_index("protein_ID")
df_mut.columns = df_mut.columns.str.extract(r'([^\.]+)')[0].to_list()
df_mut = df_mut.reset_index()

merge = pd.merge(complete_mapping, df_mut, left_on = ['Gene1'], right_on = ['protein_ID'])
merge = merge.drop(['Unnamed: 0'], axis=1)
merge['distance'] = merge.apply(lambda row: float(row[row['Gene2']]) if not pd.isna(row[row['Gene2']]) else np.nan, axis=1)
merge['rank'] = merge.drop(['Gene1', 'Gene2', 'protein_ID'], axis=1).lt(merge['distance'], axis=0).sum(axis=1)
merge['rank'].replace(0, 1, inplace=True)

columns_to_copy = ['Gene1', 'Gene2', 'distance', 'rank']
final = merge.loc[:, columns_to_copy]
final.to_csv('heinz_tomato_transposed_paralog_dist_and_recip_rank.csv', index=False)

