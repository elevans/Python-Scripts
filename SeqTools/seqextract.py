import seqtools as st

def read_file (input_file):
    
    with open(input_file) as f:
        content = f.readlines()
        f.close()

        # Strip new line ('\n')
        content = [line.strip('\n') for line in content]
    
    return (content)

def extract_sequences (seqs, names):

    output_seqs = {}
    num_seqs_retained = 0

    for k, v in seqs.items():
        if k in names:
            extract_key = k
            extract_value = v
            output_seqs[extract_key] = extract_value

        else:
            num_seqs_retained += 1

    print ("Number of sequences extracted: ", len(output_seqs))
    print ("Number of sequences retained: ", num_seqs_retained)

    return(output_seqs)

def write_file (sequences):
    
    with open("extracted_sequences.fasta", 'w') as f:
        for k, v in sequences.items():
            seq_name = str(k)
            seq_data = str(v)
            seq_name_write = ">" + seq_name + "\n"
            f.write(seq_name_write)
            seq_data_write = seq_data + "\n"
            f.write(seq_data_write)

        f.close()

    print ("Done.")

# Initialize objects
reader = st.ReadFile()
writer = st.WriteFile()
parser = st.ParseData()

# Read sequence file
input_seqs = reader.fasta(input("Enter sequence file: "))

# Read name file to extract sequences
input_names = read_file(input("Enter 'extract-name' file: "))

results = extract_sequences(input_seqs,input_names)

# Write the data out
write_file(results)