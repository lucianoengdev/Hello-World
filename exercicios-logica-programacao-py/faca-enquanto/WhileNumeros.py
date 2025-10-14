"""
#63 Do while números

Crie um programa usando a estrutura “faça enquanto” que leia vários números.
A cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na
tela:
a) O somatório entre todos os valores
b) Qual foi o menor valor digitado
c) A média entre todos os valores
d) Quantos valores são pares

"""
lista = []

while True:
    num = int(input("Digite seu número"))
    lista.append(num)
    continua = input("Você deseja continuar (S ou N)?").capitalize()
    if continua == "N":
        break

soma = sum(lista)
print(f"O somatório dos números digitados é {soma:.0f}")

menor = min(lista)
print(f"O menor número da lista é {menor:.0f}")

qtde = 0
for i in lista:
    qtde = qtde + 1
media = soma / qtde
print(f"A média de números dessa lista é {media:.1f}")

par = sum(1 for num in lista if num % 2 == 0)
print(f"Existem {par:.0f} números pares nessa lista")