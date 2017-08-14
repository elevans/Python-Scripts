import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import dbscan, DBSCAN
from sklearn import metrics, cluster, datasets, mixture
from sklearn.metrics import silhouette_score
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import kneighbors_graph
from sklearn.metrics.pairwise import pairwise_distances
from leven import levenshtein
from functools import partial


# Read file method
def read_file (input_file):
    with open(input_file) as f:
        content = f.readlines()
        f.close()

    # Strip new line ('\n') 
    content = [line.strip('\n') for line in content]

    # Remove sequence names from list
    sequence_list = [""]
    concat_sequence = ""

    for line in content:
        if ">" in line:
            sequence_list.append(concat_sequence)
            concat_sequence = ""
        else:
            concat_sequence += line

    # Add last element to sequence_list
    sequence_list.append(concat_sequence)

    # Remove first two "" entries from seuqnce_list
    del sequence_list[:2]

    return sequence_list

# calculates levenshtein distance the dataset
def lev_distance_metric(x,y):
        i, j = int(x[0]), int(y[0])
        return levenshtein(dataset[i], dataset[j])

# Allows for user to define input file.
#user_file_path = input("Enter file path: ")
#dataset = read_file(user_file_path)

# Hard code test file.
dataset = read_file("Tat_alleles.fasta")

# Github bug suggestion: https://github.com/scikit-learn/scikit-learn/issues/3737
#dataset_pairwise = pairwise_distances(np.arange(len(dataset)).reshape(-1,1), metric=partial(lev_distance, dataset))
#dbscan_dataset = DBSCAN(eps=0.1, min_samples=5, metric='euclidean').fit(dataset_pairwise)


# Sample code from scikit-learn FAQ: http://scikit-learn.org/stable/faq.html
X = np.arange(len(dataset)).reshape(-1,1)

# Note: dbscan_dataset[0] are n_core_samples and dbscan_dataset[1] are labels
dbscan_dataset = dbscan(X, eps=5, min_samples=2, metric=lev_distance_metric, algorithm='brute')
core_sample_indicies = dbscan_dataset[0]
labels = dbscan_dataset[1]

print(dataset)

# alternative DBSCAN code
#dbscan_dataset = cluster.DBSCAN(eps=0.1, min_samples=5, metric='euclidean').fit_predict(X)