#!/usr/bin/env python

import os
import re
import sys

def main(file_name):
    target_files = []
    working_path = os.getcwd() + '/' + '.versiondir'
    all_file_versions = os.listdir(working_path)
    for file in all_file_versions:
        if re.search(file_name, file):
            target_files.extend([file])
    for target_file in reversed(target_files):
        try:
            if int(target_file[-1:]):
                print target_file
        except Exception as e:
            continue


if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    main(sys.argv[1])