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

def lev_distance(s, u, v):
    return levenshtein(s[int(u)], s[int(v)])

# Allows for user to define input file.
user_file_path = input("Enter file path: ")
dataset = read_file(user_file_path)

# Take user input values for epsilon and minimum sample number
eps_user_in = int(input("Enter epsilon value: "))
min_samples_user_in = int(input("Enter minimum sample number: "))

# Reshape dataset into a column.  This is necessary for processing
dataset_reshape = np.arange(len(dataset)).reshape(-1,1)

# Compute DBSCAN
dataset_pairwise = pairwise_distances(dataset_reshape, metric=partial(lev_distance, dataset))
dbscan_model = cluster.DBSCAN(eps=eps_user_in, min_samples=min_samples_user_in, metric='euclidean', algorithm='brute').fit(dataset_pairwise)

# Print parameters and DBSCAN output values
print("Dataset Levenshtein output: \n", dataset_pairwise)
print("DBSCAN Model: ", dbscan_model)
print("DBSCAN Core indicies: ", dbscan_model.core_sample_indices_)
print("DBSCAN Labels: ", dbscan_model.labels_)

# Plot output
plot_title_user_in = input("Enter plot title: ")
plot_file_name_user_in = input("Enter output file name: ")
fig, ax = plt.subplots(figsize=(10,8))
ax.set_title(plot_title_user_in, fontsize=14)
ax.scatter(dataset_pairwise[:,0], dataset_pairwise[:,1], c=dbscan_model.labels_, s=25, alpha=0.9, cmap=plt.cm.Set1)
plt.savefig(plot_file_name_user_in + ".png")