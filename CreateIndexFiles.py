import os
from FindRow import findRowStockCode

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

# Não funciona porque escreve por cima, não insere linhas 
def createIndexStockCode(dataFile):
    if(os.path.exists("Data/IndexStockCode.csv")):
        os.remove("Data/IndexStockCode.csv")
    IndexStockCodeFile = open("Data/IndexStockCode.csv", 'w')
    pos = 0

    while True:
        rowCsv = dataFile.readline().split(";")
        if(rowCsv[0] == ''):
            break 
        else:
            if(os.stat("Data/IndexStockCode.csv").st_size == 0):
                IndexStockCodeFile.write(str(pos).ljust(6)+';'+rowCsv[2]+"\n")
                IndexStockCodeFile.close()
            else: 
                IndexStockCodeFile.close()
                insertPos = findRowStockCode(rowCsv[2]) * 20
                IndexStockCodeFile = open("Data/IndexStockCode.csv", 'a')
                IndexStockCodeFile.seek(insertPos)
                IndexStockCodeFile.write(str(pos).ljust(6)+';'+rowCsv[2]+"\n")
                IndexStockCodeFile.close()
            print(pos)
            pos+=1
    
    IndexStockCodeFile.close()