import matplotlib
matplotlib.use('Agg')

import seaborn as sns; sns.set(color_codes=True)
import matplotlib.pyplot as plt
import numpy as np

from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import linkage
from scipy.spatial import distance
from treetools import ConvertTree, Dendrogram

# Allows for user to define input file.
user_tree_file = input("Enter tree file: ")

# Convert input newick tree to a distance matrix (dmat) and a scipy linked matrix (schlink).
tree_dmat, tree_schlink = ConvertTree.newick(user_tree_file)
tree_labels = Dendrogram.extract_leaf_labels_newick(user_tree_file)

# Plot the dendrogram - use this to check if the input tree has the same topology as
# the conveted tree.
dendro_output_file_name = input("Enter output dendrogram file name: ")
Dendrogram.save_dendrogram(tree_schlink, tree_labels, dendro_output_file_name)

# Print distance matrix and scipy matrix to confirm successful converstion
print('Tree distance matrix: ')
print(tree_dmat)
print('Tree distance matrix (scipy linkage): ')
print(tree_schlink)

# Plot the cluster graph.
clustergraph = sns.clustermap(tree_dmat, robust=True, metric='euclidean', row_linkage = tree_schlink, col_linkage = tree_schlink, figsize=(15,12))

user_filename = input("Enter output clustermap file name: ")

plt.savefig(user_filename + '.png')