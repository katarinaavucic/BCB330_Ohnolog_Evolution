#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from scipy.stats import zscore
from scipy import sparse, stats
import re
from statsmodels.stats import multitest

exp = pd.read_csv('./combined_embeddings/tomato_expression_atlas_52_replicates.csv')
pairs = pd.read_csv('./Slyc4_WGD_pairs_single.csv')

# Extract prefix by removing the last character from each column name
prefixes = [col[:-1] for col in exp.columns]
# Group columns by prefixes and calculate mean for each group
aggregated_df = exp.groupby(prefixes, axis=1).mean()

z_scores = aggregated_df.apply(zscore, axis=1)
z_scores = z_scores.dropna()

filtered_pairs = pairs[pairs['Gene1'].isin(z_scores.index) & pairs['Gene2'].isin(z_scores.index)]

# Initialize an empty list to store the results
mean_rows = []
# Iterate over the filtered pairs
for index, row in filtered_pairs.iterrows():
    gene1, gene2 = row['Gene1'], row['Gene2']
    if gene1 in z_scores.index and gene2 in z_scores.index:
        gene1_data = z_scores.loc[gene1].values.reshape(1, -1)
        gene2_data = z_scores.loc[gene2].values.reshape(1, -1)
        # Create DataFrames for each gene's data and add gene names as columns
        gene1_df = pd.DataFrame(gene1_data, columns=z_scores.columns)
        gene1_df['Gene'] = gene1
        gene1_df['Pair'] = gene2
        gene2_df = pd.DataFrame(gene2_data, columns=z_scores.columns)
        gene2_df['Gene'] = gene2
        gene2_df['Pair'] = gene1
        mean_rows.extend([gene1_df, gene2_df])

# Concatenate the list of DataFrames outside the loop
means = pd.concat(mean_rows, ignore_index=True)
means.to_csv('tomato_exp_z_score_by_tissue.csv', index=False)