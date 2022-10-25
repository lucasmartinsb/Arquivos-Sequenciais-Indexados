from binarySearchData import binarySearchFile
from binarySearchIndex import searchStockCode

def countFromCountry(indexCountry, country):
    count = 0
    for row in indexCountry:
        if(row[2][0:20].strip() == country):
            count+=1
    return count

def mostExpensiveProduct(stockCode):
    try:
        initialPos = int(searchStockCode(stockCode)[0]) 
    except:
        return None
    indexStockCode = open("Data/indexStockCode.csv", 'r')

    while True:
        indexStockCode.seek((initialPos-1)*27)
        rowCsv = indexStockCode.readline().split(";")
        if(rowCsv[2][0:12].strip() == stockCode):
            indexStockCode.close()
            indexStockCode = open("Data/indexStockCode.csv", 'r')
            initialPos-=1
        else:
            break 
    
    indexStockCode = open("Data/indexStockCode.csv", 'r')
    indexStockCode.seek(initialPos*27)

    mostExpensivePrice = 0
    while True:
        rowCsv = indexStockCode.readline().split(";")
        try:
            rowStockCode = rowCsv[2][0:12].strip()
        except: 
            break
        if(rowStockCode == stockCode):
            dataFileRow = binarySearchFile(int(rowCsv[1]))
            dataFilePrice = float(dataFileRow[6].strip())
            if(dataFilePrice >= mostExpensivePrice):
                mostExpensiveProduct = dataFileRow
                mostExpensivePrice = float(dataFileRow[6].strip())
    
    return mostExpensiveProduct

    
