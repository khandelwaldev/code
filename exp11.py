import os
import sys
import pathlib
import zipfile

dirName = input('Enter directory name:- ')

if not os.path.isdir(dirName):
    print(f'Directory {dirName} not exists')
    sys.exit(0)

curDir = pathlib.Path(dirName)

with zipfile.ZipFile('MyFile.zip', mode='w') as archive:
    for file_path in curDir.rglob("'"):
        archive.write(file_path, arcname=file_path.relative_to(curDir))

if os.path.isfile('MyFile.zip'):
    print(f'Archive, MyFile.zip, created successfully')
else:
    print('error in creating zip file')
    