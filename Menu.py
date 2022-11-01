def menu():
    option = 1
    while(option != 0):
        print("0. Sair")
        print("1. Criacao de indice")
        print("2. Consulta de registro")
        print("3. Consultas")
        option = int(input())
        if(option == 1):
            print("  1. Indice em arquivo - Campo chave (ID)")
            print("  2. Indice em arquivo - Campo stockCode")
            print("  3. Indice em arvore binaria - Campo customer")
            print("  4. Indice em memoria - Campo country")
            option = int(input("  "))
            option += 10
            break
        
        elif(option == 2):
            print("  1. Busca por ID - Indice em arquivo")
            print("  2. Busca por stockCode - Indice em arquivo")
            print("  3. Busca por customer - Indice em arvore binaria")
            print("  4. Busca por country - Indice em memoria")

            option = int(input("  "))
            option += 20
            break

        elif(option == 3):
            print("  1. Quantidade de vendas para o um country")
            print("  2. Valor mais alto de um produto")
            print("  3. Buscar quantidade de compras de um customer")

            option = int(input("  "))
            option += 30
            break
    return option