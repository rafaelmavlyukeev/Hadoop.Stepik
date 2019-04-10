# put your python code here
import sys
import itertools

inFile = open('input.txt')
myDict = dict()
userDict = dict()
myList = list()
urlList = list()
queryList = list()

for line in inFile:
    (user, field) = line.strip().split('\t')
    fieldType = field.split(':')[0]
    fieldValue = field.split(':')[1]
    userDict = myDict.get(user, {'url': [], 'query': []})
    myList = userDict.get(fieldType, list())
    myList.append(fieldValue)
    userDict[fieldType] = myList.copy()
    myDict[user] = userDict

print(myDict)

for user in myDict:
    urlList = myDict[user]['url']
    queryList = myDict[user]['query']

    for query, url in list(itertools.product(queryList, urlList)):
        print(user, query, url, sep='\t')
