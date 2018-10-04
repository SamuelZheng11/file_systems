#!/usr/bin/env python

import os
import re
import shutil
import sys

def main(file_name, version_number):
    target_files = []
    working_path = os.getcwd() + '/' + '.versiondir'

    all_file_versions = os.listdir(working_path)
    for file in all_file_versions:
        if re.search(file_name, file):
            target_files.extend([file])

    for target_file in target_files:
        if target_file[-1:] is version_number:
            shutil.copy(working_path + '/' + target_file, working_path + '/' + file_name)

    for target_file in target_files:
        try:
            if re.search('[0-9]', target_file[-1:]):
                shutil.copy(working_path + '/' + target_file, working_path + '/' + target_file[:-1] + str(int(target_file[-1:]) + 1))
        except Exception as e:
            continue

    target_files = get_files(file_name, working_path)

    for target_file in target_files:
        if target_files[-1:] is str(7):
                os.remove(working_path + '/' + target_file)

    shutil.copy(working_path + '/' + file_name, working_path + '/' + file_name + '.1')

def get_files(file_name, working_path):
    target_files = []
    all_file_versions = os.listdir(working_path)
    for file in all_file_versions:
        if re.search(file_name, file):
            target_files.extend([file])
    return target_files

if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    main(sys.argv[1], sys.argv[2])