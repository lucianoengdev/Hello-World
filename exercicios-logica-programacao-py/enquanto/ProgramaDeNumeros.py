"""
#56 programa de numeros

Crie um programa que leia vários números pelo teclado e mostre no final o
somatório entre eles.
Obs: O programa será interrompido quando o número 1111 for digitado
"""

lista = []

while True:
    num = int(input("Digite um número"))

    if num == 1111:
        break

    else:
        lista.append(num)


soma = sum(lista)
print(f"O somatório da lista até aqui foi de {soma:.0f}")