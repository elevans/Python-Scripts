class ReadSequenceFile:

    def fasta (input_file):
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