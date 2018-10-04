#!/usr/bin/env python

import logging

import os
import re

def main():
    os.system("cd " + os.getcwd())
    os.system("rm .versiondir/*")
    os.system("rm -R .versiondir")
    os.system("fusermount -u mount")

if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    main()