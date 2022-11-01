import os
from operator import index, itemgetter
from treeNode import treeNode

def createIndexId(dataFile):
    if(os.path.exists("Data/IndexID.csv")):
        os.remove("Data/IndexID.csv")
    indexIdFile = open("Data/IndexID.csv", 'w')
    pos = 0
    i = 0

    for row in dataFile:
        rowCsv = row.split(";")
        indexIdFile.write(str(i).ljust(6)+';'+str(pos).ljust(6)+';'+rowCsv[0]+'\n')
        pos+=1
        i+=1

    indexIdFile.close()

def createIndexStockCode(dataFile):
    if(os.path.exists("Data/IndexStockCode.csv")):
        os.remove("Data/IndexStockCode.csv")
    pos = 0
    memoryIndex = [[0 for x in range(2)] for y in range(400366)]

    while True:
        rowCsv = dataFile.readline().split(";")
        try:
            memoryIndex[pos][0] = str(pos).ljust(6)
            memoryIndex[pos][1] = str(rowCsv[2])
        except:
            break
        pos+=1


    memoryIndex.sort(key=itemgetter(1))

    pos = 0
    i = 0
    indexStockCodeFile = open("Data/IndexStockCode.csv", "w")
    while True:
        try:
            row = memoryIndex[pos]
            indexStockCodeFile.write(str(i).ljust(6)+';'+row[0]+';'+row[1]+'\n')
            pos+=1
            i+=1
        except:
            break
    indexStockCodeFile.close()

def createIndexCustomer(dataFile):
    pos = 0
    memoryIndex = [[0 for x in range(3)] for y in range(400366)]
    while True:
        rowCsv = dataFile.readline().split(";")
        try:
            memoryIndex[pos][0] = 0
            memoryIndex[pos][1] = str(pos)
            memoryIndex[pos][2] = str(rowCsv[7]).strip()
        except:
            break
        pos+=1
    
    pos = 1
    root = treeNode(memoryIndex[0])
    while True:
        try:
            root.insertTreeNode(memoryIndex[pos])
        except:
            break
        pos+=1
    return root

def createIndexCountry(dataFile):
    pos = 0
    
    memoryIndex = [[0 for x in range(3)] for y in range(400366)]

    while True:
        rowCsv = dataFile.readline().split(";")
        try:
            memoryIndex[pos][0] = 0
            memoryIndex[pos][1] = str(pos).ljust(6)
            memoryIndex[pos][2] = str(rowCsv[8])
        except: 
            break
        pos+=1

    memoryIndex.sort(key=itemgetter(2))

    i = 0
    pos = 0
    while True:
        try:
            memoryIndex[pos][0] = i
            i+=1
            pos+=1
        except:
            break 
        
    return memoryIndex