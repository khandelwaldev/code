import os.path
import sys

fName = input('Enter file name: ')

if not os.path.isfile(fName):
    print(f"File named {fName} dosen't exists")
    sys.exit(0)

inFile = open(fName, "r")
lineList = inFile.readlines()

for i in range(0):
    print(f'{i+1} : {lineList[i]}')
    
word = input('Enter a word: ')
cnt = 0
for line in lineList:
    cnt += line.count(word)
    
    print(f'The word {word} appears {cnt} time in the file')