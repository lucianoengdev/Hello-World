"""
#91 Maior()

Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses
valores para um procedimento Maior() que vai verificar qual deles é o maior e
mostrá-lo na tela. Caso os dois valores sejam iguais, mostrar uma mensagem
informando essa característica.
"""
def Maior(num1, num2):
    if num1 == num2:
        print("Os dois números são iguais")
    else:
        maior = max(num1, num2)
        print(f"{maior} é o maior número entre esses dois")

valor1 = int(input("Digite um número:"))
valor2 = int(input("Digite um número:"))

Maior(valor1, valor2)