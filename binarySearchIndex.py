from binarySearchData import binarySearchFile
from rowCount import rowCount

def searchId(id):
    dataFile = open("Data/FinalData.csv", 'r')
    found = False
    low = 0
    mid = 0
    high = rowCount(dataFile)
    dataFile.close()

    while low<=high:
        mid = (high+low)//2
        indexIdFile = open("Data/indexId.csv", 'r')
        indexIdFile.seek(mid*27)
        rowList = indexIdFile.readline().split(";")
        indexIdFile.close()
        rowId = rowList[1][0:19].strip()
        if rowId < id:
            low = mid+1
        elif rowId > id:
            high = mid - 1
        else:
            found = True
            break   

    if found == False:
        return None 
    else:
        pos = int(rowList[0])
        return binarySearchFile(pos)

def searchStockCode(stockCode):
    dataFile = open("Data/FinalData.csv", 'r')
    found = False
    low = 0
    mid = 0
    high = rowCount(dataFile)
    dataFile.close()

    while low<=high:
        mid = (high+low)//2
        indexStockCode = open("Data/indexStockCode.csv", 'r')
        indexStockCode.seek(mid*20)
        rowList = indexStockCode.readline().split(";")
        indexStockCode.close()
        rowStockCode = rowList[1][0:12].strip()
        if rowStockCode < stockCode:
            low = mid+1
        elif rowStockCode > stockCode:
            high = mid - 1
        else:
            found = True
            break   

    if found == False:
        return None 
    else:
        pos = int(rowList[0])
        return binarySearchFile(pos)

def searchCustomer(customer, indexCustomer):
    found = False
    low = 0
    mid = 0
    high = len(indexCustomer)

    while low<=high:
        mid = (high+low)//2
        rowId = indexCustomer[mid][1][0:5].strip()
        if rowId < customer:
            low = mid+1
        elif rowId > customer:
            high = mid - 1
        else:
            found = True
            break   

    if found == False:
        return None 
    else:
        pos = int(indexCustomer[mid][0])
        return binarySearchFile(pos)

def searchCountry(country, indexCountry):
    found = False
    low = 0
    mid = 0
    high = len(indexCountry)

    while low<=high:
        mid = (high+low)//2
        rowCountry = indexCountry[mid][1][0:20].strip()
        if rowCountry < country:
            low = mid+1
        elif rowCountry > country:
            high = mid - 1
        else:
            found = True
            break   

    if found == False:
        return None 
    else:
        pos = int(indexCountry[mid][0])
        return binarySearchFile(pos)