class ReadSequenceFile:

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

    def fasta(self, output_filename, seq_list):

        i = 0

        with open(output_filename, 'w') as f:
            while i < len(seq_list):
                seq_name = str(i)
                seq_name_write = ">"+ seq_name + "\n"
                f.write(seq_name_write)
                seq_data = seq_list[i] + "\n"
                f.write(seq_data)
                i += 1

            f.close()

        
class ParseSequences:

    def remove_bad_seqs_DNA(self, seq_dict):
        
        v = list(seq_dict.values())

        initial_count = len(v)

        i = 0

        # If sequences/strings containing any of the following characters, remove them from the sequence list.
        while i < len(v):

            line = v[i]

            if "N" in line:
                v.pop(i)
          
            elif "Y" in line:
                v.pop(i)

            i += 1

        final_count = len(v)
        removed_count = initial_count - final_count

        print(str(removed_count) + ' DNA sequences removed')
        print('Sequences in dataset: ', final_count)

        return v
    
    def remove_bad_seqs_protein(self, seq_dict):
        
        v = list(seq_dict.values())

        initial_count = len(v)

        i = 0

        # If sequences/strings containing any of the following characters, remove them from the sequence list.
        while i < len(v):

            line = v[i]

            if "*" in line:
                v.pop(i)
          
            elif "X" in line:
                v.pop(i)

            i += 1

        final_count = len(v)
        removed_count = initial_count - final_count

        print(str(removed_count) + ' protein sequences removed')
        print('Sequences in dataset: ', final_count)

        return v

    def site_count_DNA(self, seq_list, site_number):

        i = 0

        nuc_pos = int(site_number) - 1

        nuc_A = 0
        nuc_G = 0
        nuc_C = 0
        nuc_T = 0

        while i < len(seq_list):

            line = seq_list[i]

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

        seq_total = len(seq_list)

        nuc_A_percent = 100 * (nuc_A/seq_total)
        nuc_G_percent = 100 * (nuc_G/seq_total)
        nuc_C_percent = 100 * (nuc_C/seq_total)
        nuc_T_percent = 100 * (nuc_T/seq_total)

        print("A: " + str(nuc_A) + " ," + str(nuc_A_percent) + " %")
        print("G: " + str(nuc_G) + " ," + str(nuc_G_percent) + " %")
        print("C: " + str(nuc_C) + " ," + str(nuc_C_percent) + " %")
        print("T: " + str(nuc_T) + " ," + str(nuc_T_percent) + " %")

