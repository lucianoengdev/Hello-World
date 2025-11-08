import sqlite3

dtbase = 'listadepessoas.db'


def criar_tabela():
    conn = sqlite3.connect(dtbase)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas( 
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        nome TEXT NOT NULL, 
                        idade INTEGER NOT NULL
                        );
                        ''')
    conn.close()

criar_tabela()

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
        conn = sqlite3.connect(dtbase)
        cursor = conn.cursor()
        cursor.execute("SELECT nome, idade FROM pessoas")
        todas_pessoas = cursor.fetchall()
        conn.close
        if not todas_pessoas:
            print("Nenhuma pessoa na lista")
            print("--------------------------")
            
        else:
            print("---Lista de pessoas cadastradas: ---")
            for pessoa in todas_pessoas:
                print(f"Nome: {pessoa[0]}   Idade: {pessoa[1]}")
                print("--------------------------")
    
    elif(opcao == 2):
        while True:
            try:
                n = str(input("Nome: "))
                i = int(input("Idade: "))
                break
            except Exception as erro:
                print(f"Você cometeu o erro {erro}")

        conn = sqlite3.connect(dtbase)
        cursor = conn.cursor()
        cursor.execute("INSERT into pessoas, ")
        print("--------------------------")
    
    else:
        print("Você saiu do programa")
        break
    

conn.close()