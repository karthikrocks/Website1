

from os import walk

directory_path = 'D:\Youtube'
files = []
for (dirpath, dirnames, filenames) in walk(directory_path):
    for file in filenames:
        files.append(file)

dictOfElems = dict()
for elem in files:
    if elem in dictOfElems:
        dictOfElems[elem] += 1
    else:
        dictOfElems[elem] = 1

dictOfElems = {key: value for key, value in dictOfElems.items() if value > 1}
print(dictOfElems)
print(files)
