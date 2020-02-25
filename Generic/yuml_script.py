import os

def list_all_files(path):
    for root, dirs, files in os.walk(path): # Outputs are lists
        level = root.replace(path, '').count(os.sep) # Replace the path with '' and count the # of '/'.
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

def generate_yuml(path):
    excluded_folders = ['main', 'java', '.ipynb_checkpoints', 'json', 'src', 'resources']
    excluded_files = ['.project', '.factorypath', '.classpath', '.envrc','pom.xml', '.mailmap', 'environment.yml', 'README.md', '.travis.yml', '.gitignore']
    ignored_dirs = ['.vscode', '.settings', '.travis', 'target', '.git']
    yuml_output_list = []

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
        folder_current = str(os.path.basename(filtered_root))

        # computer folder level of current filtered root (counts /'s)
        level = filtered_root.replace(path, '').count(os.sep)

        # get the folder above the current folder (i.e. base folder)
        folder_up = os.path.dirname(filtered_root)
        folder_up = os.path.basename(folder_up)

        # remove excluded folders
        if folder_current in excluded_folders:
            pass
        else:
            if folder_current is '':
                pass
            else:
                l = '[{}]-[{}]'.format(folder_up, folder_current)
                yuml_output_list.append(l)
        
    print('Writing file...')

    # write output file to yuml
    path = '/home/edward/Documents/Development/Repos/Personal/Python-Scripts/Generic/yuml_test.yuml'
    with open(path, 'w') as f:
        f.write('// {type:deployment}\n// {generate:true}\n\n')
        for e in yuml_output_list:
            write_line = e + '\n'
            f.write(write_line)

        f.close()

user_path = '/home/edward/Documents/Development/Repos/LOCI/tutorials'
generate_yuml(str(user_path))