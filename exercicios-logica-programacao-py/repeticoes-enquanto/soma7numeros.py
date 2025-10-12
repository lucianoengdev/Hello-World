"""
#48 Soma de 7 números

Faça um programa que leia 7 números inteiros e no final mostre o somatório
entre eles.
"""
num1 = int(input("Digite um número inteiro"))
num2 = int(input("Digite um número inteiro"))
num3 = int(input("Digite um número inteiro"))
num4 = int(input("Digite um número inteiro"))
num5 = int(input("Digite um número inteiro"))
num6 = int(input("Digite um número inteiro"))
num7 = int(input("Digite um número inteiro"))

lista = [num1, num2, num3, num4, num5, num6, num7]
soma = sum(lista)
print(soma)