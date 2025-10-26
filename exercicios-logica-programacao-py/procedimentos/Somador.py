"""
#90 Somador()

Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses
valores para um procedimento Somador() que vai calcular e mostrar a soma entre
eles.
"""

def Somador(num1, num2):
    soma = num1 + num2
    print(f"{soma} É o resultado entre a soma dos números {num1} e {num2}")

num1 = int(input("Digite um número"))
num2 = int(input("Digite um número"))
Somador(num1, num2)