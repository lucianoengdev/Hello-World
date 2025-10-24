"""
#83 ordenamento crescente

[DESAFIO] Crie uma lógica que preencha um vetor de 20 posições com números
aleatórios (entre 0 e 99) gerados pelo computador. Logo em seguida, mostre os
números gerados e depois coloque o vetor em ordem crescente, mostrando no final
os valores ordenados.
"""
import random
vetor = []

for numero in range(20):
    adicionar = random.randint(0,99)
    vetor.append(adicionar)

print(vetor)
vetor_ordenado = sorted(vetor)
print(vetor_ordenado)