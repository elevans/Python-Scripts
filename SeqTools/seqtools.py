import collections
from progressbar import update_progress

#TODO: Recode to iteratre accross dictionaries, stop using lists if possible.
#      Keep type convert in case list conversion is needed.

# TODO: Check if pulling keys or values.  don't do single variable with items.

class ReadFile:

    # TODO:  Write method to handle nexus fromat sequence files.

    def fasta(self, input_file):

        """Read a FASTA file and returns a dictionary
    
        input -- FASTA file format
        returns -- type dicts

        """
        with open(input_file) as f:
            content = f.readlines()
            f.close()

        # Strip new line ('\n')
        content = [line.strip('\n') for line in content]

        seq_dict = {}
        seq_name = ""
        concat_sequence = ""

        for line in content:
            if ">" in line:
                seq_dict[seq_name] = concat_sequence

                # Reset seq_name to current sequence and rest concat_sequence to empty.
                line = line.translate({ord(c): None for c in '>'})
                seq_name = line
                concat_sequence = ""
            else:
                concat_sequence += line

        # Add last key value pair to dictionary
        seq_dict[seq_name] = concat_sequence        
        del seq_dict[""]

        print(str(len(seq_dict)) + " sequences read.")

        return seq_dict

class WriteFile:



    # TODO: Write method for writing nexus format sequence files.

    def fasta(self, input_seqs):

        """Write a dictionary as a FASTA file

        input -- type list
        output -- fasta file
        
        """
        file_name = input("Enter output file name: ")

        with open(file_name, 'w') as f:
            for k, v in input_seqs.items():
                seq_name = str(k)
                seq_data = str(v)
                seq_name_write = ">" + seq_name + "\n"
                f.write(seq_name_write)
                seq_data_write = seq_data + "\n"
                f.write(seq_data_write)

            f.close()

        print ("Done.")

    def gen_data(self, input_data):
        
        # Write gen_freq and co_freq data to file (basically writes key/value pairs as a CSV file)
        file_name = input("Enter file name: ")

        with open(file_name, 'w') as f:
            for k, v in input_data.items():
                f.write(str(k) + "," + str(v) + "\n")
            
        print("Done!")

        return

class ParseData:

    def remove_bad_seqs(self, input_seqs):

         # Get bad characters to remove
        user_bad_chars = input("Enter characters to remove: ")
        processed_seqs = {}

        for k, v in input_seqs.items():
            seq = str(v)
            bad_chars = set(user_bad_chars)

            if any((c in bad_chars) for c in seq):
                print("Sequence " + k + " removed.")
            else:
                processed_seqs[k] = v

        # Calculate the total number of sequences that have been removed
        final_count = len(processed_seqs)
        removed_count = len(input_seqs) - len(processed_seqs)

        print(str(removed_count) + ' sequences removed')
        print('Sequences in new dataset: ', final_count)

        return processed_seqs

    def remove_short_seqs(self, input_seqs):

        output_seqs = {}
        input_length = (int(input("Enter sequence length to remove (will remove sequences of equal or shorter length): ")))
                
        for k, v in input_seqs.items():
            seq = str(v)
            if len(seq) <= input_length:
                print("Sequence " + k + " removed. Length: " + str(len(seq)))
                pass
            else:
                output_seqs[k] = v
        
        return output_seqs

    def remove_long_seqs(self, input_seqs):

        output_seqs = {}
        input_length = (int(input("Enter sequence length to remove (will remove sequences of equal or longer length): ")))

        for k, v in input_seqs.items():
            seq = str(v)
            if len(seq) >= input_length:
                print("Sequence " + k + " removed. Length: " + str(len(seq)))
                pass
            else:
                output_seqs[k] = v

        return output_seqs

    def sort_fixed_length(self, input_seqs):

        output_seqs = {}
        input_length = (int(input("Enter sequence length to store.  Sequences larger or smaller in length will be discarded: ")))

        for k, v in input_seqs.items():
            seq = str(v)
            if len(seq) == input_length:
                output_seqs[k] = v
            else:
                print("Sequence " + k + " removed. Length: " + str(len(seq)))
                pass
        
        return output_seqs
    
    def site_count(self, input_seqs):

        site_freq = {}

        input_pos = int(input("Enter sequence position to count: ")) - 1

        # TODO: Optionally store keys in a list and write out to file
        for k, v in input_seqs.items():
            seq = str(v)
            c = seq[input_pos]
            if c is not None:
                if c in site_freq.keys():
                    site_count_update = (site_freq[c] + 1)
                    site_freq[c] = site_count_update
                else:
                    site_freq[c] = 1
        
        # Print out results
        for k, v in site_freq.items():
            print(k, v, str((v/len(input_seqs)) * 100) + " %")

    def remove_duplicates(self, input_seqs):

        raw_list = []
        unique_seqs = {}

        for v in input_seqs.values():
            raw_list.append(v)

        uniques_list = []
        [uniques_list.append(x) for x in raw_list if x not in uniques_list]

        for k, v in input_seqs.items():
            if v in uniques_list:
                unique_seqs[k] = v
                uniques_list.remove(v)
            else:
                pass
                    

        # Count the number of duplicate sequences removed
        initial_count = len(input_seqs)
        updated_count = len(unique_seqs)
        removed_count = initial_count - updated_count

        print (str(removed_count) + " duplicate sequences removed.")
        print ("New dataset size: " + str(len(unique_seqs)) + " sequences.")
                    
        return unique_seqs

    def sort_seqs(self, input_seqs):
        input_char = input("Enter character to sort: ")
        input_pos = int(input("Enter character position: ")) - 1

        sorted_seqs = {}

        for k, v in input_seqs.items():
            seq = str(v)
            if seq[input_pos] == input_char:
                sorted_seqs[k] = v
            else:
                pass

        print("input :", len(input_seqs))
        print("output :", len(sorted_seqs))

        return sorted_seqs

    def pattern_match(self, input_seqs):

        pattern = input("Enter pattern: ")

        sorted_seqs = {}

        for k, v in input_seqs.items():
            seq = str(v)
            if pattern in seq:
                sorted_seqs[k] = v
            else:
                pass

        print("input :", len(input_seqs))
        print("output :", len(sorted_seqs))
        
        return sorted_seqs

    def gen_freq(self, input_seqs):
        seq_freq = collections.OrderedDict()

        for k, v in input_seqs.items():
            seq = str(v)
            if seq is not None:
                i = 0
                for c in seq:
                    i += 1
                    char_pos = str(c + str(i))
                    if char_pos in seq_freq.keys():
                        freq_count_update = (seq_freq[char_pos] + 1)
                        seq_freq[char_pos] = freq_count_update
                    else:
                        seq_freq[char_pos] = 1

        # Convert counts into percents
        seq_freq_percent = collections.OrderedDict()

        # Percent based on original item length of alignment (i.e. number of sequences)
        for k in seq_freq.keys():
            seq_freq_percent[k] = (seq_freq[k] / (len(input_seqs)))

        return seq_freq_percent

    def co_freq(self, input_seqs):
        input_char = input("Enter input character:  ")
        input_pos = int(input("Enter sequence position:  ")) - 1

        seq_freq = {}

        match_count = 0

        # TODO: Optionally store Keys in a list and write list out (matched sequences)
        # Matches sequences based on character input and position,
        # then creates ordered dict with character/position as key
        # and count as value.
        for k, v in input_seqs.items():
            seq = str(v)
            if input_char == seq[input_pos]:
                i = 0
                match_count += 1
                for c in seq:
                    i += 1
                    char_pos = str(c + str(i))
                    if char_pos in seq_freq.keys():
                        freq_count_update = (seq_freq[char_pos] + 1)
                        seq_freq[char_pos] = freq_count_update
                    else:
                        seq_freq[char_pos] = 1

        # Convert counts into percents
        seq_freq_percent = {}

        # Percent based on match count
        for l in seq_freq.keys():
            seq_freq_percent[l] = (seq_freq[l]/match_count)

        seq_freq_percent["Total number of sequences"] = match_count

        return seq_freq_percent

    def codon_freq(self, input_seqs):
        codon_freq = collections.OrderedDict()

        for k, v in input_seqs.items():
            seq = str(v)
            nuc_count = 0
            codon_count = 0
            codon = ""

            for c in seq:
                codon += c
                nuc_count += 1

                if nuc_count == 3:
                    codon_count += 1 # codon number
                    codon_pos = codon + "_" + str(codon_count) # key e.g. TAT_1

                    # Check if codon triplet is already in dictionary, ifnot craete new key/value pair with 1 as initial value

                    if codon_pos in codon_freq.keys(): # if codon already exists in dictionary update the value
                        freq_count_update = (codon_freq[codon_pos] + 1) # whatever the value is at this key
                        codon_freq[codon_pos] = freq_count_update # overwrite key with new value
                        nuc_count = 0
                        codon = ""
                    else:
                        codon_freq[codon_pos] = 1
                        nuc_count = 0
                        codon = ""
                else:
                    pass

        codon_freq_percent = collections.OrderedDict()

        # Percent based on original item length of alignment (i.e. number of sequences)
        for k in codon_freq.keys():
            codon_freq_percent[k] = (codon_freq[k] / (len(input_seqs))) 
            
        return codon_freq_percent




codon_table = {"TTT" : "F", "TTC" : "F", "TTA" : "L", "TTG" : "L", "CTT" : "L", "CTC" : "L", "CTA" : "L", "CTG" : "L", "ATT" : "I",
 "ATC" : "I", "ATA" : "I", "ATG" : "M", "GTT" : "V", "GTC" : "V", "GTA" : "V", "GTG" : "V", "TCT" : "S", "TCC" : "S", "TCA" : "S",
  "TCG" : "S", "CCT" : "P", "CCC" : "P", "CCA" : "P", "CCG" : "P" , "ACT" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T", "GCT" : "A",
   "GCC" : "A", "GCA" : "A", "GCG" : "A", "TAT" : "Y", "TAC" : "Y", "TAA" : "*", "TAG" : "*", "CAT" : "H", "CAC" : "H", "CAA" : "Q",
    "CAG" : "Q", "AAT" : "N", "AAC" : "N", "AAA" : "K", "AAG" : "K", "GAT" : "D", "GAC" : "D", "GAA" : "E", "GAG" : "E", "TGT" : "C",
     "TGC" : "C", "TGA" : "*", "TGG" : "W", "CGT" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R", "AGT" : "S", "AGC" : "S", "AGA" : "R",
      "AGG" : "R", "GGT" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G"}