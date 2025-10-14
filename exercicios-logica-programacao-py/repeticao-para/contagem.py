"""
#67 contagem

Faça um programa usando a estrutura “para” que leia um número inteiro
positivo e mostre na tela uma contagem de 0 até o valor digitado:
Ex: Digite um valor: 9
Contagem: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, FIM!
"""
num = int(input("Digite um número:"))

print("Contagem:", end = "  ")
for i in range(0,num +1, 1):
    print(f"{i:.0f}", end = ", ")

print("Acabou!")