import os

# TODO: Include file output

def GenerateYuml(path):
    excluded_folders = ['main', 'java', '.ipynb_checkpoints', 'json', 'src', 'resources']
    excluded_files = ['.project', '.factorypath', '.classpath', '.envrc','pom.xml', '.mailmap', 'environment.yml', 'README.md', '.travis.yml', '.gitignore']
    ignored_dirs = ['.vscode', '.settings', '.travis', 'target', '.git']
    folder_hold = ''
    yuml_output_list = []
    included_files = ''

    for root, dirs, files in os.walk(path):

        # each loop is one file path/directory on the tree

        # setup variables
        filtered_files = []
        filtered_root = ''
        
        # filteres out ignored dirs (e.g.  /.git)
        for k in ignored_dirs:
            if k in root:
                root = ''
            else:
                pass
        
        if root is '':
            pass
        else:
            filtered_root = root

        # base folder of current filtered root
        folder_base = str(os.path.basename(filtered_root))

        # computer folder level of current filtered root (counts /'s)
        level = filtered_root.replace(path, '').count(os.sep)

        # get the folder above the current folder (i.e. base folder)
        folder_up = os.path.dirname(filtered_root)
        folder_up = os.path.basename(folder_up)

        # check if folder up is in excluded list, if so assign previous loops base folder to up
        if folder_up in excluded_folders:
            folder_up = folder_hold
        else:
            pass

        # remove excluded folders and hold last base folder value
        if folder_base in excluded_folders:
            pass
        else:
            if folder_base is '':
                pass
            else:
                folder_hold = folder_base
                l = '[{}]-[{}]'.format(folder_up, folder_base)
                yuml_output_list.append(l)

                if not files:
                    pass
                else:
                    for g in files:
                        if g in excluded_files:
                            pass
                        else:
                            included_files += '{}\\n'.format(g)
                
                    if included_files is '':
                        pass
                    else:
                        # convert files list string to yuml format
                        k = '[{}]-[note: {}]'.format(folder_base, included_files)
                        yuml_output_list.append(k)

        # clear files string
        included_files = ''

    return yuml_output_list


def WriteYumlFile(yuml):

    print('Writing file...')

    # write output file to yuml
    path = '/home/edward/Documents/Development/Repos/Personal/Python-Scripts/Generic/yuml_test.yuml'
    with open(path, 'w') as f:
        f.write('// {type:deployment}\n// {generate:true}\n\n')
        for e in yuml:
            write_line = e + '\n'
            f.write(write_line)

        f.close()

user_path = '/home/edward/Documents/Development/Repos/LOCI/tutorials/howtos/src/main/java/howto/'
yuml_result = GenerateYuml(str(user_path))
WriteYumlFile(yuml_result)