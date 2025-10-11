"""
#42 Contando

Faça um algoritmo que pergunte ao usuário um número inteiro e positivo
qualquer e mostre uma contagem até esse valor:
Ex: Digite um valor: 35
Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!
"""

num = int(input("Digite um número inteiro e positivo"))

for item in range(0,num + 1,1):
    print (item)

print("Acabou!")