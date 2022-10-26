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
        indexIdFile.seek(mid*34)
        rowList = indexIdFile.readline().split(";")
        indexIdFile.close()
        rowId = rowList[2][0:19].strip()
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
        return rowList

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
        indexStockCode.seek(mid*27)
        rowList = indexStockCode.readline().split(";")
        indexStockCode.close()
        rowStockCode = rowList[2][0:12].strip()
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
        return rowList

def searchCustomer(customer, rootIndexCustomer):
    return rootIndexCustomer.findval(customer)

def searchCountry(country, indexCountry):
    found = False
    low = 0
    mid = 0
    high = len(indexCountry)

    while low<=high:
        mid = (high+low)//2
        try: 
            rowCountry = indexCountry[mid][2][0:20].strip()
        except: 
            break
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
        return indexCountry[mid]