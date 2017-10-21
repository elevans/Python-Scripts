Python-Scripts
===

Several python scripts that perfrom various tasks such as:

- Sequence parsing (seqtools)
- Phylogeny manipulation (treetools)
- Machine Learning (sklearn_dbscan)
- Heat map generation via seaborn (seq_pheno_clustering)
- Protein homology modeling via modeller (homology_prediction)
- Flow cytometry (flow_analysis)

# Sequence parsing and analysis (seqtools.py)

## Dependencies:

seqtools.py uses progressbar.py which is included in this repo.

## Usage:

Prepare your workspace.

```
>>> import seqtools as st
>>> reader = st.ReadSequenceFile()
>>> writer = st.WriteSequenceFile()
>>> parser = st.ParseSequences()
```

Read in a fasta file:

```
>>> data = reader.fasta("test.fasta")
```

Parse the data (for example remove sequences that contain 'X'):

```
>>> data_clean = parser.remove_bad_seqs_protein(data)
Enter characters to remove: X
---
1030 protein sequences remove
Sequences in dataset:  5166
```

### Parsing functions available:

- **remove_bad_seqs_DNA**:  Remove user defined bad sequences from DNA data.
- **remove_bad_seqs_protein**: Remove user defined bad seuences from protein data.
- **site_count_DNA**: Calculates the percentage of A/G/T/C at a user defined site.
- **remove_duplicates**: Removes duplicate sequences.
- **sort_seqs**: Sorts sequences based on the user defined site and character.  Outputs a list containing the sequences meeting the defined criteria and sequences that do not.
- **pattern_match**: Returns a list that match a specific user defined pattern.

### Features coming soon:

- NEXUS file format support
- site_count for protein
- Dictionary iteration instead of list iterations
- Consensus sequence generation (user defined percentage)

## Flow Cytometry Cell Cycle Analysis


FlowCytometryTools (latest version)
matplotlib (>1.13.1)
scipy (latest version)
ipython

## Installation - Seq_pheno_clustering
```bash
$ sudo apt-get install python3-pyqt4
$ pip3 install -U --user ete3
```

## Credit
Credit should be given to user 'themantalope' for explaining and providing code for converting a newick format tree to a scipy.cluster.hierachy linkage matrix:
https://stackoverflow.com/questions/31033835/newick-tree-representation-to-scipy-cluster-hierarchy-linkage-matrix-format


*Note dbscan_lev_distance does not work as intended