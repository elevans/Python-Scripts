import matplotlib
matplotlib.use('Agg')

import seaborn as sns; sns.set(color_codes=True)
import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics.pairwise import pairwise_distances
from functools import partial
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import linkage
from treetools import ConvertTree, Dendrogram


# Allows for user to define input file.
user_tree_file = input("Enter tree file: ")

tree_dmat = ConvertTree.ConvertNewick(user_tree_file)
tree_labels = ConvertTree.ExtractLeafLabelsNewick(user_tree_file)

dendro_output_file_name = input("Enter output dendrogram file name: ")
Dendrogram.SaveDendrogram(tree_dmat,tree_labels,dendro_output_file_name)

print('Tree distance matrix: ')
print(tree_dmat)

g = sns.clustermap(tree_dmat, figsize=(15,12))

user_filename = input("Enter output clustermap file name: ")

plt.savefig(user_filename + '.png')