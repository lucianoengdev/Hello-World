"""
#58 Idade turma

Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa
vai parar quando for digitada a idade 999. No final, mostre quantos alunos
existem na turma e qual é a média de idade do grupo.
"""

idade = []

contagem = 0

while True:
    num = int(input("Digite sua idade"))

    if num == 999:
        break

    else:
        idade.append(num)
        contagem = contagem + 1

soma = sum(idade)
media = soma / contagem

print(f"Existem {contagem:.0f} alunos na turma e a média de idade do grupo é de {media:.2f}")