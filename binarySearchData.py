def binarySearchFile(pos):
    dataFile = open("Data/FinalData.csv", 'r')
    dataFile.seek(137*pos) 
    rowList = dataFile.readline().split(";")
    dataFile.close()
    return rowList