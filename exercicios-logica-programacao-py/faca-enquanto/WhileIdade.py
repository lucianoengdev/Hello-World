"""
#62 Do While Idade

Faça um programa usando a estrutura “faça enquanto” que leia a idade de
várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou
não continuar a digitar dados. No final, quando o usuário decidir parar, mostre
na tela:
a) Quantas idades foram digitadas
b) Qual é a média entre as idades digitadas
c) Quantas pessoas tem 21 anos ou mais.
"""

lista = []

while True:
    idade = int(input("Qual sua idade?"))
    lista.append(idade)
    continua = input("Quer continuar (S ou N)?").capitalize()
    if continua == "N":
        break

soma = sum(lista)
qtde = 0

for i in lista:
    qtde = qtde + 1

maior21 = sum (1 for num in lista if num > 21)

print(f"Foram digitadas {qtde:.0f} idades")

media = soma / qtde
print(f"A média das idades, é de {media:.0f} anos")

print(f"Existem {maior21} pessoas com mais de 21 anos")
