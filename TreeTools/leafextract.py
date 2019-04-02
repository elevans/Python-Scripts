from ete3 import ClusterTree, TreeStyle

def extract_taxa (input_tree):
    tree = ClusterTree(input_tree)
    leaves = tree.get_leaf_names()

    return leaves

input_file = input("Enter tree file: ")
taxa = extract_taxa(input_file)

with open("taxa_names.txt", 'w') as f:
    for item in taxa:
        f.write("%s\n" % item)

print ("Done!")