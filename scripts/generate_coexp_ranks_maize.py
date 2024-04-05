#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import h5py

species = "maize"
data = h5py.File("coexp/" + species + "_AggNet.hdf5", 'r')
pairs = pd.read_csv('./combined_embeddings/' + species + '_conversion.csv')
assem = pd.read_csv("./combined_embeddings/maize_version_mapping.csv")

dataset = data['agg']
coexp = pd.DataFrame(dataset[:])
row = data['row']
rows = pd.DataFrame(row[:])
col = data['col']
cols = pd.DataFrame(col[:])
rows.iloc[:, 0] = [label.decode('utf-8') for label in rows.iloc[:, 0]]
cols.iloc[:, 0] = [label.decode('utf-8') for label in cols.iloc[:, 0]]

coexp.index = rows.iloc[:, 0]
coexp.columns = cols.iloc[:, 0]


merge1 = pd.merge(assem, coexp, left_on = ['Gene_IDs_v4'], right_index=True)
merge2 = pd.merge(pairs, merge1, left_on = ['Duplicate 1'], right_on=['Gene_IDs_v3'])
merge2 = merge2.drop(['Gene_IDs_v3', 'Gene_IDs_v5'], axis=1)
merge2 = merge2.rename({'Gene_IDs_v4': 'V4 1'}, axis=1)
merge3 = pd.merge(assem, merge2, left_on = ['Gene_IDs_v3'], right_on=['Duplicate 2'])
merge3 = merge3.drop(['Gene_IDs_v3', 'Gene_IDs_v5'], axis=1)
merge3 = merge3.rename({'Gene_IDs_v4': 'V4 2'}, axis=1)
merge = merge3


merge['coexp'] = merge.apply(lambda row: float(row[row['V4 2']]) if row["V4 2"] in merge.columns else np.nan, axis=1)
merge.dropna(inplace=True)
merge['coexp_rank'] = merge.drop(['Duplicate 1', 'Duplicate 2'], axis=1).lt(merge['coexp'], axis=0).sum(axis=1)

columns_to_copy = ['Duplicate 1', 'Duplicate 2', 'coexp', 'coexp_rank']
final = merge.loc[:, columns_to_copy]
final.to_csv('./combined_embeddings/' + species + '_WGD_paralog_coexp_and_rank_inv.csv', index=False)

dist = pd.read_csv('./combined_embeddings/' + species + "_paralog_dist_and_recip_rank.csv")
merge = pd.merge(final, dist, on=['Duplicate 1', 'Duplicate 2'])
merge.to_csv('./combined_embeddings/' + species + '_WGD_paralog_dist_and_coexp_ranks_inv.csv', index=False)