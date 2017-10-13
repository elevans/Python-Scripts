from progressbar import update_progress

class ReadSequenceFile:

    # TODO:  Write method to handle nexus fromat sequence files.

    def fasta(self, input_file):

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

        return seq_dict

class WriteSequenceFile:

    # TODO: Write method for writing nexus format sequence files.

    def fasta(self, output_filename, input_seqs):

        i = 0

        # Write fasta format sequence files with proper formating.
        with open(output_filename, 'w') as f:
            while i < len(input_seqs):
                seq_name = str(i)
                seq_name_write = ">"+ seq_name + "\n"
                f.write(seq_name_write)
                seq_data = input_seqs[i] + "\n"
                f.write(seq_data)
                i += 1

            f.close()

        print("Done.")

class ParseSequences:

    # TODO:  Write site_count_protein method for handling protein sequences.

    def remove_bad_seqs_DNA(self, input_seqs):
        
        # If passed a dict convert to list
        converter = TypeConvert()
        v = converter.dict_to_list(input_seqs)
        initial_count = len(v)

        i = 0

        # If sequences/strings containing any of the following characters, remove them from the sequence list.
        while i < len(v):
            line = v[i]
            bad_chars = set('UWSMKRYBDHVNuwsmkrybdhvn')

            if any((c in bad_chars) for c in line):
                v.pop(i)
                print(line + " removed " + "index: " + str(i))
                i -=1
            else:
                pass

            i += 1

        # Calculate the total number of sequences that have been removed
        final_count = len(v)
        removed_count = initial_count - final_count

        print(str(removed_count) + ' DNA sequences removed')
        print('Sequences in dataset: ', final_count)

        return v
    
    def remove_bad_seqs_protein(self, input_seqs):
        
        # TODO:  bad_chars should be dynamic, the set should be defined as a user input string?  Write catch for duplicates since a set can't take duplicates.

        # If passed a dict convert to list
        converter = TypeConvert()
        v = converter.dict_to_list(input_seqs)
        initial_count = len(v)

        i = 0

        # If sequences/strings containing any of the following characters, remove them from the sequence list.
        while i < len(v):
            line = v[i]
            bad_chars = set('Xx')

            if any((c in bad_chars) for c in line):
                v.pop(i)
                print(line + " removed " + "index: " + str(i))
                i -= 1
            else:
                pass

            i = i + 1

        final_count = len(v)
        removed_count = initial_count - final_count

        print(str(removed_count) + ' protein sequences removed')
        print('Sequences in dataset: ', final_count)

        return v

    def site_count_DNA(self, input_seqs, site_number):

        # If passed a dict convert to list
        converter = TypeConvert()
        v = converter.dict_to_list(input_seqs)
        initial_count = len(v)

        nuc_pos = int(site_number) - 1
        i = 0
     
        nuc_A = 0
        nuc_G = 0
        nuc_C = 0
        nuc_T = 0

        while i < len(v):
            line = v[i]
            char = line[nuc_pos]

            if "A" == char:
                nuc_A += 1
            elif "G" == char:
                nuc_G += 1
            elif "C" == char:
                nuc_C += 1
            elif "T" == char:
                nuc_T += 1

            i += 1

        input_seq_total = len(v)

        nuc_A_percent = 100 * (nuc_A/input_seq_total)
        nuc_G_percent = 100 * (nuc_G/input_seq_total)
        nuc_C_percent = 100 * (nuc_C/input_seq_total)
        nuc_T_percent = 100 * (nuc_T/input_seq_total)

        print("A: " + str(nuc_A) + " ," + str(nuc_A_percent) + " %")
        print("G: " + str(nuc_G) + " ," + str(nuc_G_percent) + " %")
        print("C: " + str(nuc_C) + " ," + str(nuc_C_percent) + " %")
        print("T: " + str(nuc_T) + " ," + str(nuc_T_percent) + " %")

    def remove_duplicates(self, input_seqs):

        # If passed a dict convert to list
        converter = TypeConvert()
        v = converter.dict_to_list(input_seqs)
        initial_count = len(v)

        # Extract uniques and place them into a new list
        raw_list = v
        uniques_list = []
        [uniques_list.append(x) for x in raw_list if x not in uniques_list]

        # Count the number of duplicate sequences removed
        initial_count = len(raw_list)
        updated_count = len(uniques_list)
        removed_count = initial_count - updated_count

        print (str(removed_count) + " duplicate sequences removed")
        print ("Dataset size: ", len(uniques_list))
                
        return uniques_list

    def sort_seqs(self, input_seqs):

        # If passed a dict convert to list
        converter = TypeConvert()
        v = converter.dict_to_list(input_seqs)
        initial_count = len(v)

        seq_pos = int(input("Enter nucleotide or amino acid position: "))
        seq_pos -= 1
        seq_val = input("Enter nucleotide or amino acid character to sort: ")

        sorted_list = []
        excluded_list = []

        i = 0

        while i < len(v):
            line = v[i]

            if line[seq_pos] == seq_val:
                sorted_list.append(line)
            else:
                excluded_list.append(line)
            i += 1
            update_progress(i/len(v))

        print(str(len(sorted_list)) + " sequences in new dataset containing \'" + seq_val + "\'" + " at position " + str(seq_pos + 1) + ".")

        return sorted_list, excluded_list

    def pattern_match(self, input_seqs):

        # If passed a dict convert to list
        converter = TypeConvert()
        v = converter.dict_to_list(input_seqs)
        initial_count = len(v)

        pattern = input("Enter pattern to search for: ")

        matched_list = []

        i = 0

        while i < len(v):
            line = v[i]

            if pattern in line:
                matched_list.append(line)
            else:
                pass
            i += 1
            update_progress(i/len(v))

        final_count = len(matched_list)
        pattern_freq = 100 * (final_count/initial_count)

        print(str(final_count) + " (" + str(round(pattern_freq, 2)) + " %) sequences contain the \'" + pattern + "\'" + "pattern.")

        return matched_list

class TypeConvert:

    def dict_to_list(self, input_data):

         # Checks if input data is a list or dict.  If a dict, convert to a list.  If a list, pass the data on.
        if isinstance(input_data, dict):
            v = list(input_data.values())
        else:
            v = input_data

        return v