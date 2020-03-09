#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "EarthHadjo"

def get_spec_paths(dir):
    """ given dir name returns the appended
    results of the search for special files"""
    result = []
    file_directory = os.listdir(dir)
    for file_name in file_directory:
        if re.search(r'__\w+__', file_name):
            result.append(file_name)
    return result

def copy_to_dir(path, files):
    """ copies path of special files to
    a directory (only if --todir is an arg)"""
    cwd = os.getcwd()
    if not os.path.exists(path):
        create_dir = 'mkdir -p {0}'.format(path)
        os.system(create_dir)
    else:
        print("Path exists")
        os.chdir(cwd)
        shutil.copy(files.path)

def zip_to_file(paths, zippath):
    """creates zipfile from special path"""
    paths = list(paths)
    command = "zip -j {} {}".format(zippath, ' '.join(paths))
    print("Command I'm going to do: ")
    print(command)
    os.system(command)
    
def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    parser.add_argument('fromdir', help='dir to look for local files')
    args = parser.parse_args()
    if args.todir:
       copy_to_dir(args.todir, all_paths)
    if args.tozip:
        zip_to_file(all_paths, os.path.join(os.getcwd(), args.tozip))
    if not args.todir and not args.tozip:
        for file in all_paths:
            print(os.path.abspath(file))

if __name__ == "__main__":
    main()
