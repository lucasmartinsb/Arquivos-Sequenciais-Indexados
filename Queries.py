from binarySearchData import binarySearchFile
from binarySearchIndex import searchCountry, searchStockCode
from treeNode import treeNode

def countFromCountry(indexCountry, country):
    try:
        initialPos = int(searchCountry(country, indexCountry)[0]) 
    except:
        return None

    count = 1
    i = 1
    while True:
        try:
            row = indexCountry[initialPos-i]
            i+=1
            rowStockCode = row[2][0:20].strip()
        except: 
            break
        if(rowStockCode == country):
            count+=1
        else:
            break
    
    i = 1
    while True:
        try:
            row = indexCountry[initialPos+i]
            i+=1
            rowStockCode = row[2][0:20].strip()
        except: 
            break
        if(rowStockCode == country):
            count+=1
        else:
            break     
    return count 

def mostExpensiveProductStockCode(stockCode):
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

def customerPurchases(customer, root):
    try:
        return root.findval(customer)
    except:
        return None
    