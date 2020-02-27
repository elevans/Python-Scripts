import os

# TODO: Make pre-loop variables global

def GenerateYumlMapFolderFile(path):

    # pre-loop variables
    excluded_folders = ['main', 'java', '.ipynb_checkpoints', 'json', 'src', 'resources']
    excluded_files = ['.project', '.factorypath', '.classpath', '.envrc','pom.xml', '.mailmap', 'environment.yml', 'README.md', 
        '.travis.yml', '.gitignore', 'plugins.config', 'blobs.png']
    ignored_dirs = ['.vscode', '.settings', '.travis', 'target', '.git']
    folder_hold = ''
    yuml_output = []
    included_files = ''

    for root, dirs, files in os.walk(path):

        # Note: each loop is one file path/directory on the tree

        # setup loop variables
        filtered_root = ''
        loop_check = None
        
        # filteres out ignored dirs
        for k in ignored_dirs:
            if k in root:
                root = ''
            else:
                pass
        
        if root is '':
            pass
        else:
            filtered_root = root

        # base folder of current filtered root path
        folder_base = str(os.path.basename(filtered_root))

        # get the folder above the current folder
        folder_up = os.path.dirname(filtered_root)
        folder_up = str(os.path.basename(folder_up))

        # check if folder_up is in excluded list, if so assign the previous loop's base folder to folder_up
        if folder_up in excluded_folders:
            folder_up = folder_hold
        else:
            pass

        # check if folder_base is in excluded list, if so assign the previous loop's base folder to folder_up
        if folder_base in excluded_folders:
            folder_up = folder_hold
        else:
            if folder_base is '':
                pass
            else:
                # write yuml format string and store and store as an entry in yuml_output
                folder_hold = folder_base
                l = '[{}]-[{}]'.format(folder_up, folder_base)
                yuml_output.append(l)
                
                # check if there are files in this current directory
                if not files:
                    pass
                else:
                    # filter out excluded files and write partial yuml format string
                    for g in files:
                        if g in excluded_files:
                            pass
                        else:
                            included_files += '{}\\n'.format(g)
                                
                    # check if yuml format string is empty, if not complete yuml string and append yuml_output
                    if included_files is '':
                        pass
                    else:
                        k = '[{}]-[note: {}{{bg:wheat}}]'.format(folder_base, included_files)
                        yuml_output.append(k)
                        
                        # mark that this loop has run, skipping the next loop which is intended for files in an exluded folder
                        loop_check = True
                        print('Current folder: {}\nFolder up: {}\n------------------------'.format(folder_base, folder_up))
        
        # check if the previous loop ran
        if loop_check is True: 
            pass
        else:

            # check if there are files in directory (current folder is in excluded list)
            if not files:
                pass
            else:
                # filter out excluded files and write partial yuml format string
                for h in files:
                    if h in excluded_files:
                        pass
                    else:
                        included_files += '{}\\n'.format(h)
                
                # check if yuml format string is empty, if not complete yuml string and append yuml_output
                if included_files is '':
                    pass
                else:
                    if folder_up is '':
                        pass
                    else:
                        k = '[{}]-[note: {}{{bg:wheat}}]'.format(folder_up, included_files)
                        yuml_output.append(k)
                        print('Current folder: {}\nFolder up: {}\n------------------------'.format(folder_base, folder_up))

        # clear files string
        included_files = ''

    return yuml_output

def GenerateYumlMapFolder(path):

    # pre-loop variables
    excluded_folders = ['main', 'java', '.ipynb_checkpoints', 'json', 'src', 'resources']
    ignored_dirs = ['.vscode', '.settings', '.travis', 'target', '.git']
    folder_hold = ''
    yuml_output = []

    for root, dirs, files in os.walk(path):

        # Note: each loop is one file path/directory on the tree

        # setup loop variables
        filtered_root = ''
        loop_check = None
        
        # filteres out ignored dirs
        for k in ignored_dirs:
            if k in root:
                root = ''
            else:
                pass
        
        if root is '':
            pass
        else:
            filtered_root = root

        # base folder of current filtered root path
        folder_base = str(os.path.basename(filtered_root))

        # get the folder above the current folder
        folder_up = os.path.dirname(filtered_root)
        folder_up = str(os.path.basename(folder_up))

        # check if folder_up is in excluded list, if so assign the previous loop's base folder to folder_up
        if folder_up in excluded_folders:
            folder_up = folder_hold
        else:
            pass

        # check if folder_base is in excluded list, if so assign the previous loop's base folder to folder_up
        if folder_base in excluded_folders:
            folder_up = folder_hold
        else:
            if folder_base is '':
                pass
            else:
                # write yuml format string and store and store as an entry in yuml_output
                folder_hold = folder_base
                l = '[{}]-[{}]'.format(folder_up, folder_base)
                yuml_output.append(l)

    return yuml_output

def WriteYumlFile(yuml):

    print('Writing file...')

    # write output file to yuml
    path = '/home/edward/Documents/Development/Repos/LOCI/tutorials/tutorials_map.yuml'
    with open(path, 'w') as f:
        f.write('// {type:deployment}\n// {generate:true}\n\n')
        for e in yuml:
            write_line = e + '\n'
            f.write(write_line)

        f.close()

user_path = '/home/edward/Documents/Development/Repos/LOCI/tutorials/'
yuml_result = GenerateYumlMapFolder(user_path)
#yuml_result = GenerateYumlMapFolderFile(str(user_path))
WriteYumlFile(yuml_result)