import sqlite3

conn = sqlite3.connect('listapessoas.db')

while True:
    print(f"--------------------------")
    print(f"----- Menu Principal -----")
    print(f"--------------------------")
    print(f"1 - Ver pessoas listadas")
    print(f"2 - Adicionar Pessoas")
    print(f"3 - Sair do Programa")
    while True:
        try:
            opcao = int(input("Digite o número do que deseja fazer: "))
            break
        except:
            print("Você não digitou uma das opções válidas (1, 2 ou 3)")

    if(opcao == 1):
        print("Pessoas listadas: ")
    
    elif(opcao == 2):
        print("Você digitou a opção 2")
    
    else:
        print("Você saiu do programa")
        break
    

conn.close()