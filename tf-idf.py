import json
import os
import numpy as np
import re
import math

#create connector word set

connectDict = { 
  'a':'',
  'also':'',
  'an':'',
  'and':'',
  'as':'',
  'at':'',
  'be':'',
  'by':'',
  'does':'',
  'for':'',
  'from':'',
  'had':'',
  'has':'',
  'have':'',
  'having':'',
  'he':'',
  'him':'',
  'his':'',
  'in':'',
  'into':'',
  'is':'',
  'of':'',
  'on':'',
  'or':'',
  'some':'',
  'that':'',
  'the':'', 
  'then':'',
  'this':'',
  'to':'',
  'was':'',
  'were':'',
  'what':'',
  'when':'',
  'where':'',
  'while':'',
  'who':'',
  'with':'', 
}

# get all .json files from directory
currentDirectory = '../../Predictive Analytics/100 Documents'
fileNames = []
for file in os.listdir(currentDirectory):
    if 'json' in file:
        fileNames.append(file)

# verify all 100 documents are read
documentCount = len(fileNames)

# create corpus of documents from directory
fileDict = {}
for x in range(0, documentCount):
    open_file = open(currentDirectory + '/' + fileNames[x])
    with open_file as data_file:
        data = json.load(data_file)['query']['pages']
        data = list(data.values())[0]['extract'].encode('utf-8').strip()
        fileDict[fileNames[x].replace('.json','').replace('_',' ')] = data

# get all words from corpus
wordsList = []
for x in range(0, documentCount):
    testFileData = fileDict[list(fileDict.keys())[x]].split()
    for y in range(0,len(testFileData)):
        testFileData[y] = re.sub('[^A-Za-z0-9]+', '', testFileData[y].decode('utf-8'))
        testFileData[y] = re.sub(r'\w*\d\w*', '', testFileData[y]).strip()
        if testFileData[y].lower() not in connectDict:
            wordsList.append(testFileData[y].lower())
wordsList = list(filter(None, wordsList))
print(len(wordsList))