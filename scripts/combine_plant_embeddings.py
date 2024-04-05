#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import umap
import functools
import numpy as np
import os, fnmatch
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm
import random

# change line
species = "rice.pep"
embedding_file_path = './rice.pep_embeddings/'
result_file_path = './combined_embeddings/'
embedding_files = fnmatch.filter(os.listdir(embedding_file_path), species + '.embedding_all*.csv')

list_of_rows = list()
for embed_file_i in tqdm(embedding_files):
    embeddings = pd.read_csv(os.path.join(embedding_file_path, embed_file_i))
    list_of_rows.append(embeddings)


#%time 
all_embeddings = pd.concat(list_of_rows, ignore_index=True, copy=False)
all_embeddings.to_csv(os.path.join(result_file_path, 
                                   species + ".ProtT5.embeddings.csv.gz"), 
                      index=False, compression='gzip')
os.path.join(result_file_path, species + ".ProtT5.embeddings.csv.gz")
