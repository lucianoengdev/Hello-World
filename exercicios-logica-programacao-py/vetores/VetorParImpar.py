"""
#79 par ou impar do vetor

Desenvolva um programa que leia 10 números inteiros e guarde-os em um vetor.
No final, mostre quais são os números pares que foram digitados e em que
posições eles estão armazenados.
"""
vetor = []
i = 0
while True:
    i = i + 1
    num = int(input("Digite um número:"))
    vetor.append(num)
    if i == 10:
        break

vetorpar = []
for par in vetor:
    if par % 2 == 0:
        vetorpar.append(par)

vetorparposicao = []
for par, valor in enumerate(vetor):
    if valor % 2 == 0:
        vetorparposicao.append(par)
print("Os números pares são")
print(vetorpar, end = "  ")
print()
print("Eles estão nas posições:")
print(vetorparposicao, end = "  ")