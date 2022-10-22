from binarySearchData import binarySearchFile

def searchId(id):
    dataFile = open("Data/FinalData.csv", 'r')
    found = False
    low = 0
    mid = 0

    for high, line in enumerate(dataFile):
        pass 
    high += 1

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
