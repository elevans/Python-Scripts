import matplotlib
matplotlib.use('Agg')

import seaborn as sns; sns.set(color_codes=True)
import matplotlib.pyplot as plt
import numpy as np

from leven import levenshtein
from sklearn.metrics.pairwise import pairwise_distances
from functools import partial
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import linkage

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

# Reshape dataset into a column.  This is necessary for processing
dataset_reshape = np.arange(len(dataset)).reshape(-1,1)

dataset_pairwise = pairwise_distances(dataset_reshape, metric=partial(lev_distance, dataset))

print("Dataset Levenshtein output: \n", dataset_pairwise)

g = sns.clustermap(dataset_pairwise, figsize=(150,120))

plt.savefig("seaborn_test.png")