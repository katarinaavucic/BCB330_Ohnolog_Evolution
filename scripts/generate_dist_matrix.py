import pandas as pd
import umap
import functools
import numpy as np
import os, fnmatch

from scipy.spatial.distance import pdist, squareform
from scipy.spatial import distance_matrix
from sklearn.metrics import pairwise_distances

from datetime import datetime
#from google.colab import drive
#import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

from tqdm import tqdm
import random


# change this line
embedding_file_path = './combined_embeddings/'
species = 'rice.pep'

# change this line
proteins_df = pd.read_csv(os.path.join(embedding_file_path, species + ".ProtT5.embeddings.csv.gz"))

proteins_df = proteins_df.set_index("protein_ID")

distance_matrix = pairwise_distances(proteins_df, proteins_df, metric='cityblock', n_jobs = -1)

# convert the full distance matrix to a Pandas dataframe
distance_df = pd.DataFrame(distance_matrix, index=proteins_df.index, columns=proteins_df.index)

distance_df.to_csv(embedding_file_path + "distance_df_" + species + ".csv")