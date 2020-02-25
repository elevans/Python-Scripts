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
    excluded_folders = ['main', 'java', '.ipynb_checkpoints', 'metadata', 'json', 'META-INF', '.settings', 'src', 'target', '.git', '.vscode', '.travis']
    excluded_files = ['.project', '.factorypath', '.classpath', '.envrc','pom.xml', '.mailmap',
     'environment.yml', 'README.md', '.travis.yml', '.gitignore']

    for root, dirs, files in os.walk(path):

        # each loop is one file path/directory on the tree
        # setup variables
        filtered_files = []

        # compute folder level
        level = root.replace(path, '').count(os.sep)

        # base folder of root
        folder_base = str(os.path.basename(root))
        
        # folder one leve up of root
        # TODO: logic here to link back to the previous folder if folder up = exluded_files
        folder_up = os.path.dirname(root)
        folder_up = os.path.basename(folder_up)

        # Remove excluded directories
        if folder_base in excluded_folders:
            folder_base = ''
            continue
        else:
            pass

        if not folder_base:
            pass
        else:

            # Remove excluded files
            
            for item in files:
                if item in excluded_files:
                    None
                else:
                    filtered_files.append(item)
                           
        # compute yuml format
        if level == 0:
            print('[{}]'.format(folder_base))
        else:
            print('[{}]-[{}]'.format(folder_up, folder_base))
            for i in filtered_files:
                print('       ' + i)

user_path = '/home/edward/Documents/Development/Repos/LOCI/tutorials'
generate_yuml(str(user_path))

# output string proposal for yuml
# line1 = '[{}]'.format(base)
# line2 = '[{}]-[{}]'.format(base, connect)