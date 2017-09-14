import matplotlib
matplotlib.use('Agg')

import scipy.cluster.hierarchy as sch
import scipy.spatial.distance
import matplotlib.pyplot as plt
import numpy as np

from ete3 import ClusterTree, TreeStyle
from itertools import combinations
from tqdm import *

class ConvertTree:
    
    def Newick (user_input_file):
        
        tree = ClusterTree(user_input_file)
        leaves = tree.get_leaf_names()
        ts = TreeStyle()
        ts.show_leaf_name=True
        ts.show_branch_length=True
        ts.show_branch_support=True

        leaf_dict = {}

        # Convert leaves (a list) into a dictionary
        for i in range(len(leaves)):
            leaf_dict[leaves[i]] = i
            i = i + 1
            
        # Cast dictionary attributes as list and create index labels
        k = list(leaf_dict.keys())
        v = list(leaf_dict.values())
        w = list(leaf_dict.items())
        leaf_labels = [k[v.index(j)] for j in range(0, len(w))]

        # Create a numpy array of zeros based on the number of taxa in the tree
        dmat = np.zeros((len(leaves),len(leaves)))

        print('Converting input tree:')

        # Compute distance matrix from newick tree (this is not yet a linked distance matrix)
        for l1,l2 in tqdm(combinations(leaves,2)):
            d = tree.get_distance(l1,l2)
            dmat[leaf_dict[l1],leaf_dict[l2]] = dmat[leaf_dict[l2],leaf_dict[l1]] = d

        # Convert dmat into a linkage distance matrix for scipy
        schlink = sch.linkage(scipy.spatial.distance.squareform(dmat),method='average',metric='euclidean')

        return dmat, schlink
 
class Dendrogram:

    def ExtractLeafLabelsNewick (user_input_file):

        tree = ClusterTree(user_input_file)
        leaves = tree.get_leaf_names()

        leaf_dict = {}

        # Convert leaves (a list) into a dictionary
        for i in range(len(leaves)):
            leaf_dict[leaves[i]] = i
            i = i + 1

        # Cast dictionary attributes as list and create index labels
        k = list(leaf_dict.keys())
        v = list(leaf_dict.values())
        w = list(leaf_dict.items())
        leaf_labels = [k[v.index(j)] for j in range(0, len(w))]

        return leaf_labels

    def SaveDendrogram (scipy_dmat, leaf_labels, output_file_name):
        plt.figure(figsize=(10,10))
        dendro = sch.dendrogram(scipy_dmat, labels=leaf_labels)
        plt.savefig(output_file_name)

        return