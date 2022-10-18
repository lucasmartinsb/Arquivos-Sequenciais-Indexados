import os
from SortLists import sortStockCode
from operator import index, itemgetter

def createIndexId(dataFile):
    if(os.path.exists("Data/IndexID.csv")):
        os.remove("Data/IndexID.csv")
    indexIdFile = open("Data/IndexID.csv", 'w')
    pos = 0

    for row in dataFile:
        rowCsv = row.split(";")
        indexIdFile.write(str(pos).ljust(6)+';'+rowCsv[0]+'\n')
        pos+=1

    indexIdFile.close()

def createIndexStockCode(dataFile):
    if(os.path.exists("Data/IndexStockCode.csv")):
        os.remove("Data/IndexStockCode.csv")
    
    
    pos = 0
    memoryIndex = [[0 for x in range(2)] for y in range(400366)]

    while True:
        rowCsv = dataFile.readline().split(";")
        if(rowCsv[0] == ''):
            break
        else:
            memoryIndex[pos][0] = str(pos).ljust(6)
            memoryIndex[pos][1] = str(rowCsv[2])
        pos+=1

    memoryIndexSorted = sortStockCode(memoryIndex)
    #memoryIndex.sort(key=itemgetter(1))
    print(memoryIndexSorted[1][1])

    # pos = 0
    # indexStockCodeFile = open("Data/IndexStockCode.csv", "w")
    # while True:
    #     try:
    #         row = memoryIndex[pos]
    #         indexStockCodeFile.write(row[0]+';'+row[1]+'\n')
    #         pos+=1
    #     except:
    #         break
    # indexStockCodeFile.close()
