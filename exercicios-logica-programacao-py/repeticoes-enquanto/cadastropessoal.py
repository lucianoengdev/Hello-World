"""
#53 Cadastro pessoal

 Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
a) Quantos homens foram cadastrados
b) Quantas mulheres foram cadastradas
c) A média de idade do grupo
d) A média de idade dos homens
e) Quantas mulheres tem mais de 20 anos
1. Quais são os dados de entrada necessário?
idade pessoa 1
genero pessoa 1
idade pessoa 2
genero pessoa 2
idade pessoa 3
genero pessoa 3
idade pessoa 4
genero pessoa 4
idade pessoa 5
genero pessoa 5

2. O que devo fazer com estes dados?
Dizer:
a) Quantos homens foram cadastrados
b) Quantas mulheres foram cadastradas
c) A média de idade do grupo
d) A média de idade dos homens
e) Quantas mulheres tem mais de 20 anos

3. Quais são as restrições deste problema?

4. Qual é o resultado esperado?
Relacionar os dados de homem e mulher

5. Qual é a sequência de passos a ser feitas para chegar ao resultado?
lista de genero
count if quantos M tem na lista

count if quantos F tem na lista

lista de idade
média da idade do grupo



count if f lista de genero e maior que 20 na lista de idade 
"""

num1 = int(input("Qual sua idade?"))
sex1 = str(input("Qual seu sexo (M ou F)")).capitalize()
num2 = int(input("Qual sua idade?"))
sex2 = str(input("Qual seu sexo (M ou F)")).capitalize()
num3 = int(input("Qual sua idade?"))
sex3 = str(input("Qual seu sexo (M ou F)")).capitalize()
num4 = int(input("Qual sua idade?"))
sex4 = str(input("Qual seu sexo (M ou F)")).capitalize()
num5 = int(input("Qual sua idade?"))
sex5 = str(input("Qual seu sexo (M ou F)")).capitalize()

lista1 = [num1, num2, num3, num4, num5]
lista2 = [sex1, sex2, sex3, sex4, sex5]


man = sum(1 for sexo in lista2 if sexo == "M")
print(f"Temos {man:.1f} homens na lista")


woman = sum(1 for sexo in lista2 if sexo == "F")
print(f"Temos {woman:.1f} mulheres na lista")


media = sum(lista1) / 5
print(f"A média de idade do grupo é de {media} anos")


somah = 0
for ind in range(len(lista1)):
    if lista2[ind] == "M":
        somah = somah + lista1[ind]
mediah = 0
if man > 0:
    mediah = somah / man
print(f"A média do grupo de homens é de {mediah:.1f}")


mul20 = 0 
for indi in range(len(lista2)):
    if lista1[indi] > 20 and lista2[indi] == "F":
        mul20 = mul20 + 1

print(f"Existem {mul20:.0f} mulheres nesse grupo com mais de 20 anos")