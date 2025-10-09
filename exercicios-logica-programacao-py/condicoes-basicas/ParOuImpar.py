"""
#20 Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.

Para calcular isso preciso saber o resto da divisão, e se usar = int não vai dar certo pois em python, int não é um valor, mas sim um tipo de dado
Devido a isso, o caractere "%" da o resto da divisão, se tem resto sabemos que não é um valor inteiro
"""
num = int(input("Digite um número inteiro"))
if num % 2 == 0:
    print("Ele é par")

else:
    print("Ele é impar")