"""
#89 melhorando o 88

 Crie um programa que melhore o procedimento Gerador() da questão anterior
para que o programador possa escolher uma entre três bordas:
 +-------=======------+ Borda 1
 ~~~~~~~~:::::::~~~~~~~ Borda 2
 <<<<<<<<------->>>>>>> Borda 3
Ex: Uma chamada válida seria Gerador("Portugol Studio", 3, 2)
~~~~~~~~:::::::~~~~~~~
 Portugol Studio
 Portugol Studio
 Portugol Studio
~~~~~~~~:::::::~~~~~~~
"""
def Gerador(mensagem, vezes, escolha):
    Borda1 = "+-------=======------+"
    Borda2 = "~~~~~~~~:::::::~~~~~~~" 
    Borda3 = "<<<<<<<<------->>>>>>>" 
    if escolha == 1:
        print(Borda1)
    elif escolha == 2:
        print(Borda2)
    else:
        print(Borda3)
    for i in range(vezes):
        print(f"{mensagem}")
    if escolha == 1:
        print(Borda1)
    elif escolha == 2:
        print(Borda2)
    else:
        print(Borda3)

Gerador("Portugol Studio", 3, 2)