import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
import decimal

from sklearn.cluster import dbscan, DBSCAN
from sklearn import metrics, cluster, datasets, mixture
from sklearn.metrics import silhouette_score
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import kneighbors_graph
from sklearn.metrics.pairwise import pairwise_distances
from leven import levenshtein
from functools import partial
from readseq import ReadSequenceFile
from treetools import ConvertTree

def lev_distance(s, u, v):
    return levenshtein(s[int(u)], s[int(v)])


# Allows for user to define input file.
#user_file_path = input("Enter file path: ")
#dataset = ReadSequenceFile.fasta(user_file_path)

user_tree = input("Enter newick file: ")
tree_dmat = ConvertTree.ConvertNewick(user_tree)

# Take user input values for epsilon and minimum sample number
eps_user_in = decimal.Decimal(input("Enter epsilon value: "))
min_samples_user_in = int(input("Enter minimum sample number: "))

# Reshape dataset into a column.  This is necessary for processing
#dataset_reshape = np.arange(len(dataset)).reshape(-1,1)

# Compute DBSCAN
#dataset_pairwise = pairwise_distances(dataset_reshape, metric=partial(lev_distance, dataset))
#dbscan_model = cluster.DBSCAN(eps=eps_user_in, min_samples=min_samples_user_in, metric='euclidean', algorithm='brute').fit(dataset_pairwise)

# Compute DBSCAN on input tree
dbscan_model = cluster.DBSCAN(eps=eps_user_in, min_samples=min_samples_user_in, metric='euclidean', algorithm='brute').fit(tree_dmat)

# Print parameters and DBSCAN output values

print("Dataset Levenshtein output: \n", tree_dmat)
print("DBSCAN Model: ", dbscan_model)
print("DBSCAN Core indicies: \n", dbscan_model.core_sample_indices_)
print("DBSCAN Labels: \n", dbscan_model.labels_)


# Plot output
plt.style.use('ggplot')
plot_title_user_in = input("Enter plot title: ")
plot_file_name_user_in = input("Enter output file name: ")
fig, ax = plt.subplots(figsize=(15,12))
ax.set_title(plot_title_user_in, fontsize=14)
plt.savefig(plot_file_name_user_in + ".png")

