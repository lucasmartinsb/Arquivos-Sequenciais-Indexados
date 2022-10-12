#include <curses.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define max_invoices 400366

struct Invoice{
    char *ID[20];
    char *invoiceNo[8];
    char *stockCode[13];
    char *description[36];
    int quantity;
    char *invoiceDate[17];
    float unitPrice;
    char *customerID[6];
    char *country[20];
};
struct Invoice invoice;

int menu(){
    int option = 1;
    while(option != 0){
        printf("0. Sair\n");
        printf("1. Criacao de indice\n");
        printf("2. Consulta de registro\n");
        scanf("%d", &option);
        if(option == 1){
            printf("  1. Indice em arquivo, - Campo chave (ID)\n");
            printf("  2. Indice em arquivo, - Campo invoiceNo (valores duplicados)\n");
            printf("  3. Indice em memoria - Campo stockCode (valores duplicados)\n");
            printf("  4. Indice em memoria - Campo description (valores duplicados)\n");
            printf("  ");
            scanf("%d", &option);
            option += 10;
            printf("\n");
            break;
        }
        if(option==2){
            printf("  1. Busca por ID - Indice em arquivo\n");
            printf("  2. Busca por invoiceNo - Indice em arquivo (valores duplicados)\n");
            printf("  3. Busca por stockCode - Indice em memoria (valores duplicados)\n");
            printf("  4. Busca por description - Indice em memoria (valores duplicados)\n");
            printf("  ");
            scanf("%d", &option);
            option += 20;
            printf("\n");
            break;
        }
    }
    printf("\n");
    return option;
}

int main(){
    int option;

    while (option !=0){
        FILE *data = fopen("Data/FinalData.csv", "r");
        option = menu();

        if(option == 11){
            remove("Data/IndexID.csv");
            FILE *indexID = fopen("Data/IndexID.csv", "w");
            //createIndexID(data);
            fclose(data);
        }
        if(option == 12){
            remove("Data/IndexInvoiceNo.csv");
            FILE *indexInvoiceNo = fopen("Data/IndexInvoiceNo.csv", "w");
            //createIndexInvoiceNo(data);
            fclose(data);
        }
        if(option == 13){
            //createIndexStockCode(data);
            fclose(data);
        }
        if(option == 14){
            //createIndexDescription(data);
            fclose(data);
        }

        else if(option == 21){
            FILE *indexID = fopen("Data/IndexID.csv", "r");
            char *ID[20];
            printf("Digite o ID a ser buscado: ");
            fflush(stdin);
            fgets(ID, 20, stdin);
            //binarySearchIndexID(data, indexID, ID);
            fclose(data);
            fclose(indexID);
        }
        else if(option == 22){
            FILE *indexInvoiceNo = fopen("Data/IndexInvoiceNo.csv", "r");
            char *InvoiceNo[8];
            printf("Digite o InvoiceNo a ser buscado: ");
            fflush(stdin);
            fgets(InvoiceNo, 8, stdin);
            //searchIndexInvoiceNo(data, indexInvoiceNo, InvoiceNo);
            fclose(data);
        }
        else if(option == 23){
            char *StockCode[13];
            printf("Digite o StockCode a ser buscado: ");
            fflush(stdin);
            fgets(StockCode, 13, stdin);
            //searchIndexStockCode(data, StockCode);
            fclose(data);
        }
        else if(option == 24){
            char *Description[36];
            printf("Digite a Description a ser buscado: ");
            fflush(stdin);
            fgets(Description, 36, stdin);
            //searchIndexDescription(data, Description);
            fclose(data);
        }
        
    }
}