import os
from os.path import join, getsize


# base_dir = '/home/trent/data/workspace/PycharmProjects/python_works/mrms/'
# path = os.path.join(base_dir, 'resources/')

all_files_path = []
all_files_name = []

def get_all_file(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            all_files_path.append(os.path.join(root, file))
            all_files_name.append(file)

    return (all_files_path, all_files_name)

# get_all_file(path)
# print(all_files_path)
# print(all_files_name)
