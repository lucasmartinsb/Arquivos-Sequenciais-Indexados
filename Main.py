from timeit import default_timer as timer

from Menu import menu
from CreateIndexFiles import createIndexId, createIndexStockCode, createIndexCustomer, createIndexCountry
from binarySearchIndex import searchId, searchStockCode, searchCustomer, searchCountry
from binarySearchData import binarySearchFile
from writeRegister import writeRegister
from Queries import countFromCountry, mostExpensiveProduct


def main():
    option = 100

    while (option!=0):
        option = menu()

        if(option == 11):
            dataFile = open("Data/FinalData.csv", 'r')
            start = timer()
            createIndexId(dataFile)
            end = timer() 

            print("Tempo para gerar arquivo (s): "+str(round(float(end-start), 4))+"\n")
            dataFile.close()
        
        elif(option == 12):   
            dataFile = open("Data/FinalData.csv", 'r')         
            start = timer()
            createIndexStockCode(dataFile)
            end = timer()

            print("Tempo para gerar arquivo (s): "+str(round(float(end-start), 4))+"\n")
            dataFile.close()
            
        elif(option == 13):
            dataFile = open("Data/FinalData.csv", 'r')
            start = timer()
            indexCustomer = createIndexCustomer(dataFile)
            end = timer()

            print("Tempo para gerar arquivo (s): "+str(round(float(end-start), 4))+"\n")
            dataFile.close()
        
        elif(option == 14):
            dataFile = open("Data/FinalData.csv", 'r')
            start = timer()
            indexCountry = createIndexCountry(dataFile)
            end = timer()

            print("Tempo para gerar arquivo (s): "+str(round(float(end-start), 4))+"\n")
            dataFile.close()


        elif(option == 21):
            id = str(input("Digite o ID a ser buscado: "))
            
            indexRow = searchId(id)
            if(indexRow == None):
                print('ID nao encontrado')
            else:
                register = binarySearchFile(register)
                writeRegister(register)
        
        elif(option == 22):
            stockCode = str(input("Digite o stockCode a ser buscado: "))
            indexRow = searchStockCode(stockCode)

            if(indexRow == None):
                print('ID nao encontrado')
            else:
                register = binarySearchFile(int(indexRow[1]))
                writeRegister(register)   

        elif(option == 23):
            customer = str(input("Digite o customer a ser buscado: "))
            indexRow = searchCustomer(customer, indexCustomer)

            if(indexRow == None):
                print('Customer nao encontrado')
            else:
                register = binarySearchFile(indexRow[1])
                writeRegister(register)

            dataFile.close()
        elif(option == 24):
            country = str(input("Digite o country a ser buscado: "))
            indexRow = searchCountry(country, indexCountry)

            if(indexRow == None):
                print('Country nao encontrado')
            else:
                register = binarySearchFile(indexRow[1])
                writeRegister(register)
        
        elif(option == 31):
            country = str(input("Digite o country a ser contado: "))
            print("Quantidade de vendas para o "+country+": "+str(countFromCountry(indexCountry, country)))
        
        elif(option == 32):
            stockCode = str(input("Digite o stockCode a ser buscado maior valor: "))
            mostExpensiveRegister = mostExpensiveProduct(stockCode)
            if(mostExpensiveRegister == None):
                print('StockCode nao econtrado!')
            else:
                writeRegister(mostExpensiveRegister)


if __name__ == "__main__":
    main()