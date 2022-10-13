from timeit import default_timer as timer

import os
from Menu import menu
from CreateIndexFiles import createIndexId, createIndexStockCode

def main():
    option = 100

    while (option!=0):
        dataFile = open("Data/FinalData.csv", 'r')
        option = menu()

        if(option == 11):
            start = timer()
            createIndexId(dataFile)
            end = timer() 

            print("Tempo para gerar arquivo (s): "+str(round(float(end-start), 4))+"\n")
            dataFile.close()
        
        elif(option == 12):            
            start = timer()
            createIndexStockCode(dataFile)
            end = timer()

            print("Tempo para gerar arquivo (s): "+str(round(float(end-start), 4))+"\n")
            dataFile.close()
            
        elif(option == 13):
            #indexStockCode = createIndexDescription(data)
            dataFile.close()
        
        elif(option == 14):
            #indexDescription = createIndexCustomer(data)
            dataFile.close()

        elif(option == 21):
            indexIdFile = open("Data/IndexID.csv", 'r')
            id = str(input("Digite o ID a ser buscado: "))
            
            #binarySearchIndexId(data, indexIdFile, id)
            
            dataFile.close()
            indexIdFile.close()
        
        elif(option == 22):
            IndexStockCodeFile = open("Data/IndexStockCode.csv", 'r')
            stockCode = str(input("Digite o stockCode a ser buscado: "))

            #binarySearchIndexStockCode(data, IndexStockCodeFile, stockCode)
            
            dataFile.close()
            indexIdFile.close()
            
        elif(option == 23):
            description = str(input("Digite o description a ser buscado: "))
            #binarySearchIndexStockCode(data, indexDescription, description)
            dataFile.close()

        elif(option == 24):
            customer = str(input("Digite o customer a ser buscado: "))
            #binarySearchCustomer(data, indexCustomer, customer)
            dataFile.close()

if __name__ == "__main__":
    main()