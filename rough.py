import json
import os


with open('DataBase/data.json', 'r+') as outfile:
    flag = 0
    data = json.load(outfile)
    for i in data['people']:
        print(i,end="\n")
