#!/usr/bin/env python
# coding: utf-8

import zipfile, os, os.path

path_to_zip = './main.zip'
extract_to = './'
with zipfile.ZipFile(path_to_zip, 'r') as zip_ref:
    zip_ref.extractall(extract_to)


dirs_with_py = []
for current_dir, dirs, files in os.walk('.' + path_to_zip.split('.')[-2]):
    for file in files:
        if file[-3:] == '.py':
            dirs_with_py.append(current_dir)
            break

