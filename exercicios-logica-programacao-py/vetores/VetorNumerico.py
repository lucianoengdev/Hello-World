"""
#71 vetor numerico

Faça um programa que preencha automaticamente um vetor numérico com 8
posições, conforme abaixo:
999 999 999 999 999 999 999 999
"""
import random
vetor = []
i = 0
while True:
    variavel = random.randint(1,1000)
    vetor.append(variavel)
    i = i + 1
    if i == 8:
        break
print(vetor)
