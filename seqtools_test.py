from seqtools import ReadSequenceFile, WriteSequenceFile, ParseSequences

# Input file
user_file = input('Enter filename: ')
result_filename = input("Enter output filename: ")

# Initialize file_reader and seq_parser objects
file_reader = ReadSequenceFile()
file_writer = WriteSequenceFile()
seq_parser = ParseSequences()

# Input data and parse the data
input_data = file_reader.fasta(user_file)
good_seqs_data = seq_parser.remove_bad_seqs_protein(input_data)
unique_seqs_data = seq_parser.remove_duplicates(good_seqs_data)
file_writer.fasta(result_filename, unique_seqs_data)