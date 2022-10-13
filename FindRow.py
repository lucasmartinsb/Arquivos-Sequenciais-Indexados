def findRowStockCode(stockCode):
    indexStockCodeFileAux = open("Data/IndexStockCodeAux.csv", 'w')
    IndexStockCodeFile = open("Data/IndexStockCode.csv", 'r')
    pos = 0
    while True:
        rowCsv = IndexStockCodeFile.readline()
        if(rowCsv.split(";")[0] == ''):
            IndexStockCodeFile.close()
            indexStockCodeFileAux.close()
            return pos
        else:
            if(stockCode <= rowCsv.split(";")[1]):
                IndexStockCodeFile.close()
                indexStockCodeFileAux.close()
                return pos
            indexStockCodeFileAux.write(rowCsv)
            pos+=1