"""
#60 3 Listas

Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas.
O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
a) O nome da pessoa mais velha
b) O nome da mulher mais jovem
c) A média de idade do grupo
d) Quantos homens tem mais de 30 anos
e) Quantas mulheres tem menos de 18 anos

for indice, pessoa in enumerate(pessoas):
    if pessoa['idade'] > mais_velha:
        mais_velha = pessoa['nome']
"""
pessoas = []

while True:
    name = input("Qual o seu nome?")
    age = int(input("Qual a sua idade?"))
    sex = input("Qual o seu sexo (M ou F)?").capitalize()

    pessoas.append({'nome': name,'idade': age,'sexo': sex})

    continua = input("Você quer continuar (S ou N)?").capitalize()

    if continua == "N":
        break

mais_velha = 0
nome_mais_velha = ""
qtde_pessoas = 0
for pessoa in pessoas:
    qtde_pessoas = qtde_pessoas + 1
    if pessoa['idade'] > mais_velha:
        nome_mais_velha = pessoa['nome']
print(f"A pessoa mais velha do grupo é a {nome_mais_velha}")        

mulheres = [p for p in pessoas if p['sexo'] == "F"]
if mulheres:
    mulher_mais_jovem = 10000
    nome_mulher_mais_jovem = ""
    for pessoa in pessoas:
        if pessoa['sexo'] == "F" and pessoa['idade'] < mulher_mais_jovem:
            mulher_mais_jovem = pessoa['idade']
            nome_mulher_mais_jovem = pessoa['nome']
    print(f"A mulher mais jovem é a {nome_mulher_mais_jovem}")

else:
    print("Nenhuma mulher encontrada na lista")

lista_idades = [p['idade'] for p in pessoas]
soma_idades = sum(lista_idades)
media_idades = soma_idades / qtde_pessoas
print(f"A idade média do grupo é de {media_idades:.1f} anos")

homens = [p for p in pessoas if p['sexo'] == "M"]
if homens:
    qtde_homens30 = 0
    for pessoa in pessoas:
        if pessoa['sexo'] == "M" and pessoa['idade'] > 30:
            qtde_homens30 = qtde_homens30 + 1
    print(f"Existem nesse grupo, {qtde_homens30:.0f} homens com mais de 30 anos")

else:
    print("Nenhum homem com mais de 30 anos foi encontrado na lista")


if mulheres:
    qtde_mulher18 = 0
    for pessoa in pessoas:
        if pessoa['sexo'] == "F" and pessoa['idade'] < 18:
            qtde_mulher18 = qtde_mulher18 + 1
    print(f"Existem nesse grupo, {qtde_mulher18:.0f} mulheres com menos de 18 anos")
    
else:
    print("Nenhuma mulher com menos de 18 anos foi encontrada na lista")
    