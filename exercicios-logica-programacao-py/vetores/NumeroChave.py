"""
#80 Número Chave

Faça um algoritmo que preencha um vetor de 30 posições com números entre 1 e
15 sorteados pelo computador. Depois disso, peça para o usuário digitar um
número (chave) e seu programa deve mostrar em que posições essa chave foi
encontrada. Mostre também quantas vezes a chave foi sorteada.
"""
import random
vetor = []
i = 0
while True:
    i = i + 1
    num = random.randint(1,15)
    vetor.append(num)
    if i == 30:
        break

num_usuario = int(input("Digite um número entre 1 a 15:"))
print(vetor)
vetorposicoes = []
qtde = 0
for ind, valor in enumerate(vetor):
    if num_usuario == valor:
        qtde = qtde + 1
        vetorposicoes.append(ind)

print(f"Esse número apareceu {qtde:.0f} vezes, nas posições", end = " ")
print(vetorposicoes)