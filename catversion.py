#!/usr/bin/env python

import os
import re
import sys
import shutil

def main(file_name, version_number):
    working_path = os.getcwd() + '/' + '.versiondir'
    all_file_versions = os.listdir(working_path)
    for file in all_file_versions:
        if re.search(file_name, file):
            if re.search(version_number, file[-1:]):
                shutil.copy(working_path + '/' + file , working_path + '/' + file_name)

if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    main(sys.argv[1], sys.argv[2])