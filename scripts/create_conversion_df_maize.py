#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

species = "maize"
complete_mapping = pd.read_csv("./combined_embeddings/" + species + "_pairs.csv")
ids = pd.read_csv("./combined_embeddings/" + species + "_uniprot_conversion.tsv", sep = "\t")
pairs = complete_mapping
assem_ids = pd.read_csv("./combined_embeddings/" + species + "_version_mapping.csv")

merge = pd.merge(ids, assem_ids, left_on = ['To'], right_on = ['Gene_IDs_v5'])
merge = merge.dropna()

conv = pd.merge(merge, pairs, left_on = ['Gene_IDs_v3'], right_on = ['Duplicate 1'])
conv = conv.drop(['To', 'Gene_IDs_v4', 'Gene_IDs_v3', 'Gene_IDs_v5', 'Unnamed: 0'], axis = 1)
conv = conv.rename({'From': 'Uniprot 1'}, axis=1)
conv = pd.merge(conv, merge, left_on = ['Duplicate 2'], right_on = ['Gene_IDs_v3'])
conv = conv.drop(['To', 'Gene_IDs_v4', 'Gene_IDs_v3', 'Gene_IDs_v5'], axis = 1)
conv = conv.rename({'From': 'Uniprot 2'}, axis=1)

conv.to_csv("./combined_embeddings/" + species + "_conversion.csv", index=False)