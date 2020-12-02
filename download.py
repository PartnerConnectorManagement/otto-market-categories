import requests
import json
import os

def getToken():
    data = {'username': os.environ['OK_USERNAME'], 'password': os.environ['OK_PASSWORD'], 'grant_type': 'password', 'client_id': os.environ['OK_CLIENT_ID']}
    header = {'Content-Type': 'application/x-www-form-urlencoded', 'cache-control': 'no-cache'}
    r = requests.post('https://api.otto.market/v1/token?=', data=data, headers=header)
    output = json.loads(r.text)
    print('got token')
    return output['access_token'] 
    print(output['access_token'])

def getCategories(token):
    data = {}
    header = {'Authorization': 'Bearer ' + token}
    r = requests.get('https://api.otto.market/v1/products/categories?limit=100', data=data, headers=header)
    result = json.loads(r.text)
    print('downloaded file')
    return result
    print(result['categoryGroups'][0])

class Index:
    def __init__(self, name, index):
        self.name = name
        self.index = index

def createIndexing(json):
    index = []
    #print(len(json['categoryGroups']))
    for x in range(len(json['categoryGroups'])):
        for y in range(len(json['categoryGroups'][x]['categories'])):
            newIndex = Index(json['categoryGroups'][x]['categories'][y], x)
            index.append(newIndex)
    #print(index)
    return index

def writeFile(input, name):
    f = open(name, 'w')
    f.write(input)
    f.close()
    print('File ' + name + ' has been saved!')

def writeIndex(input):
    outputString = 'let index = ['
    for x in input:
        outputString += '{name:"' + x.name + '",'
        outputString += 'index:"' + str(x.index) + '"},'
    outputString = outputString[:-1]    
    outputString += ']'

    writeFile(outputString, 'index.js')

def writeCategories(input):
    outputString = 'let categories = ['
    for x in input:
        outputString += '{' 
        outputString += 'categoryGroup: "' +  x['categoryGroup'] + '"'
        outputString += '},'
    outputString = outputString[:-1]

    writeFile(outputString, 'categories.js')




token = getToken()
categories = getCategories(token)
index = createIndexing(categories)

writeIndex(index)
#writeCategories(categories['categoryGroups'])