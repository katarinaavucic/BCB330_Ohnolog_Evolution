import pandas as pd
import numpy as np

species = "maize"
df = pd.read_csv("./combined_embeddings/distance_df_" + species + ".fasta.csv")

df_mut = df.copy()
df_mut['protein_ID'] = df_mut['protein_ID'].str.extract(r'(sp\|.+?|tr\|.+?)\|')[0].to_list()
df_mut['protein_ID'] = df_mut['protein_ID'].str[3:]
df_mut = df_mut.set_index("protein_ID")
df_mut.columns = df_mut.columns.str.extract(r'(sp\|.+?|tr\|.+?)\|')[0].to_list()
df_mut.columns = df_mut.columns.str[3:]
df_mut = df_mut.reset_index()

cols = pd.DataFrame(df_mut['protein_ID'])
cols.to_csv("./combined_embeddings/" + species + "_uniprot_ids.csv", index=False)