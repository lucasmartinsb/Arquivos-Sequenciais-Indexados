def findRowStockCode(stockCode):
    IndexStockCodeFile = open("Data/IndexStockCode.csv", 'r')
    pos = 0
    while True:
        rowCsv = IndexStockCodeFile.readline().split(";")
        if(rowCsv[0] == ''):
            IndexStockCodeFile.close()
            return pos
        else:
            if(stockCode <= rowCsv[1]):
                IndexStockCodeFile.close()
                return pos
            pos+=1