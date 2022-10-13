import os
from FindRow import findAndWriteRowStockCode

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
    if(os.path.exists("Data/IndexStockCodeAux.csv")):
        os.remove("Data/IndexStockCodeAux.csv")    
    
    pos = 0

    while True:
        rowCsv = dataFile.readline().split(";")
        if(rowCsv[0] == ''):
            break 
        else:
            if(os.stat("Data/IndexStockCode.csv").st_size == 0):
                indexStockCodeFile = open("Data/IndexStockCode.csv", 'w')
                indexStockCodeFile.write(str(pos).ljust(6)+';'+rowCsv[2]+"\n")
                indexStockCodeFile.close()
            else: 
                insertPos = findAndWriteRowStockCode(rowCsv[2])
                indexStockCodeFileAux = open("Data/IndexStockCodeAux.csv", 'a')
                indexStockCodeFileAux.write(str(pos).ljust(6)+';'+rowCsv[2]+"\n")
                indexStockCodeFile = open("Data/IndexStockCode.csv", 'r')
                indexStockCodeFile.seek(insertPos*20)
                indexRow = 'aux'
                while(indexRow!=''):
                    indexStockCodeFileAux.write(indexStockCodeFile.readline())
                
                indexStockCodeFile.close()
                indexStockCodeFileAux.close()

                os.remove("Data/IndexStockCode.csv")
                os.rename("Data/IndexStockCodeAux.csv", "Data/IndexStockCode.csv")
            print(pos)
            pos+=1
    
    indexStockCodeFile.close()