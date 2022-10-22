def menu():
    option = 1
    while(option != 0):
        print("0. Sair")
        print("1. Criacao de indice")
        print("2. Consulta de registro")
        option = int(input())
        if(option == 1):
            print("  1. Indice em arquivo, - Campo chave (ID)")
            print("  2. Indice em arquivo, - Campo stockCode")
            print("  4. Indice em memoria - Campo customer")
            print("  3. Indice em memoria - Campo country")
            option = int(input("  "))
            option += 10
            break
        
        elif(option == 2):
            print("  1. Busca por ID - Indice em arquivo")
            print("  2. Busca por stockCode - Indice em arquivo")
            print("  3. Busca por customer - Indice em memoria")
            print("  4. Busca por country - Indice em memoria")

            option = int(input("  "))
            option += 20
            break
    return option