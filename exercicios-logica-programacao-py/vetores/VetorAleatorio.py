"""
#76 Vetor Aleatório

Crie um programa que preencha automaticamente um vetor numérico com 7
números gerados aleatoriamente pelo computador e depois mostre os valores
gerados na tela.
"""
import random
vetor = []
i = 0
while True:
    variavel = random.randint(1,1000)
    vetor.append(variavel)
    i = i + 1
    if i == 7:
        break
print(vetor)
