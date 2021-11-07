import json
from os import listdir
from os.path import isfile, join, dirname
from ntpath import realpath

# for k, v in .items():
#     print(f"For {k}")
#     print(v['time'])

outputfolder = join(dirname(realpath(__file__)), 'output')

createpath = lambda fn: join(outputfolder, fn)
load_json = lambda path: json.load(open(path))

filenames = [
    filename
    for filename in listdir(outputfolder) 
    if isfile(createpath(filename))
        and filename.endswith('.json')
]

categories = set(
    int(filename[0])
    for filename in filenames
)

filenames_by_category = {}

for c in categories:
    filenames_by_category[c] = []
    for f2 in filenames:
        if f2[0]==str(c):
            filenames_by_category[c].append(f2)

print(filenames_by_category)

