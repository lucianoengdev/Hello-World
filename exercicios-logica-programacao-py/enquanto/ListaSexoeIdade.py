"""
#59 Lista de sexo e idade

Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai
perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
a) qual é a maior idade lida
b) quantos homens foram cadastrados
c) qual é a idade da mulher mais jovem
d) qual é a média de idade entre os homens
"""

idade = []
sexo = []

idmulher = []
homens = 0
mulheres = 0
while True:
    age = int(input("Qual a sua idade?"))
    gen = input("Qual o seu sexo (M ou F)?").capitalize()

    idade.append(age)
    sexo.append(gen)

    if gen == "M":
        homens = homens + 1

    else:
        mulheres = mulheres + 1
        

    continua = input("Você quer continuar digitando sobre mais pessoas (S ou N)?").capitalize()
    if continua == "N":
        break


maior = max(idade)
print(f"A maior idade lida é de {maior:.0f} anos")

      
print(f"Foram cadastrados {homens:.0f} homens no grupo")

if mulheres > 0:
    mul = 10000
    for ind in range(len(sexo)):
        if sexo[ind] == "F" and idade[ind] < mul:
            mul = idade[ind]
print(f"A menor idade de mulheres do grupo é de {mul:.0f} anos")

somah = 0
if homens > 0:
    for i in range(len(sexo)):
        if sexo[i] == "M":
            somah = somah + idade[i]
mediah = somah / homens
print(f"A média de idade dos homens do grupo é de {mediah:.0f} anos")
