"""
#68 Dados de peso e sexo

Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura
“para”. No final, mostre na tela:
a) Quantas mulheres foram cadastradas
b) Quantos homens pesam mais de 100Kg
c) A média de peso entre as mulheres
d) O maior peso entre os homens

1. Quais são os dados de entrada necessário?
Sexo 
Peso
(x8)

2. O que devo fazer com estes dados?
Dizer:
a) Quantas mulheres foram cadastradas
b) Quantos homens pesam mais de 100Kg
c) A média de peso entre as mulheres
d) O maior peso entre os homens

3. Quais são as restrições deste problema?
Tenho que usar "for"

5. Qual é a sequência de passos a ser feitas para chegar ao resultado?
criar lista
perguntar sexo e peso(x8) e adicionar a lista
for F in listasexo +1

for M in listasexo and >100kg in listapeso + 1

for F in sexo soma o peso da pessoa
divide essa soma pela resposta da letra a

if homens > 0 na lista
variavel = 1
for homen na lista ver seu peso, se for mmaior que a variavel, troca a variavel
"""

dados = []


for i in range(1,9,1):
    sexo = input("Qual o seu sexo (M ou F)?").capitalize()
    peso = float(input("Qual o seu peso?"))
    
    dados.append({'sex': sexo, 'weight': peso})


mul = sum(1 for num in dados if num['sex'] == "F")
print(f"Existem {mul:.0f} mulheres na lista")

hom = sum(1 for car in dados if car['sex'] == "M" and car['weight'] > 100)
print(f"Existem {hom:.0f} homens na lista com mais de 100kg")

if mul:
    soma_peso_mulher = 0
    for mulh in dados:
        if mulh['sex'] == "F":
            soma_peso_mulher = soma_peso_mulher + mulh['weight']
media_peso_mulher = soma_peso_mulher / mul
print(f"A média de peso entre as mulheres é de {media_peso_mulher:.1f}kg")

if hom:
    maior_peso_homens = 1
    for home in dados:
        if home['sex'] == "M" and home['weight'] > maior_peso_homens:
            maior_peso_homens = home['weight']
print(f"O maior peso entre os homens da lista é de {maior_peso_homens:.1f}kg")

print(dados)