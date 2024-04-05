#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np

coexp = pd.read_csv("combined_embeddings/Slyc4_coexp_network.csv")
exp = pd.read_csv("combined_embeddings/tomato_expression_atlas_52_replicates.csv")

df = pd.read_csv("heinz_tomato_tandem_paralog_dist_and_recip_rank.csv")

common_rows = exp.index.intersection(df['Gene1'])
exp_select = exp.loc[common_rows]

df["coexpression"] = df.apply(lambda row: coexp.loc[row["Gene1"], row["Gene2"]] if row["Gene1"] in coexp.index and row["Gene2"] in coexp.columns else np.nan, axis=1)

df["mean_expression"] = df.apply(lambda row: exp_select.loc[row["Gene1"]].mean() if row["Gene1"] in exp_select.index else np.nan, axis=1)

df.to_csv("heinz_tomato_tandem_paralog_df.csv", index=False)