#Note - installation of bioembeddings on narval required some edits of the bio embedding library requirements:
#pip install -U "bio-embeddings[all] @ git+https://github.com/leonfrench/bio_embeddings.git"
#https://github.com/leonfrench/bio_embeddings
import functools
import pandas as pd
from Bio import SeqIO
import numpy as np
import os
from datetime import datetime

import bio_embeddings
from bio_embeddings.embed import ProtTransT5XLU50Embedder

base_directory = "/home/vucickat/projects/def-jagillis/vucickat/plants/extract_embeddings"

#this may need to be ran while online first to download weights (instead of on an offline worker node)
embedder = ProtTransT5XLU50Embedder()

#change fasta file
fasta_file_base_name = "rice.pep"
sequence_list = list(SeqIO.parse(base_directory + '/proteomes/' + fasta_file_base_name, "fasta"))

print(len(sequence_list))

#sort by length
def compare(item1, item2):
    return len(item1.seq) - len(item2.seq)

#sort by sequence length so it will fail at the largest it can handle
sequence_list = sorted(sequence_list, key=functools.cmp_to_key(compare))
sequences_strings = [str(x.seq) for x in sequence_list]
sequences_ids = [x.description for x in sequence_list]

batch_size = 100
i = 0

while i <= len(sequence_list):
    print(i)
    current_time = datetime.now().strftime("%H:%M:%S")
    print("Current Time =", current_time)
    batch_ids = sequences_ids[i:i+batch_size]
    batch_sequences_strings = sequences_strings[i:i+batch_size]
    embedding_many = embedder.embed_batch(batch_sequences_strings)
    embedding_many = [embedder.reduce_per_protein(x) for x in list(embedding_many)]
    embedding_df = pd.DataFrame(embedding_many)
    embedding_df["protein_ID"] = batch_ids
    first_column = embedding_df.pop('protein_ID')
    embedding_df.insert(0, 'protein_ID', first_column)
    embedding_df.to_csv(path_or_buf= base_directory + "/rice.pep_embeddings/" + fasta_file_base_name + ".embedding_all." + str(i) + ".csv", index=False)
    i += batch_size
    if i >= len(sequence_list)*0.95:
        batch_size = 1
    elif i  >= len(sequence_list)*0.9:
        batch_size = 50
    elif i  >= len(sequence_list)*0.3:
        batch_size = 100
    else:
        batch_size = 500



