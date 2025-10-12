"""
#49 Números pares ou ímpares

 Crie um programa que leia 6 números inteiros e no final mostre quantos deles
são pares e quantos são ímpares.
1. Quais são os dados de entrada necessário?
6 números

2. O que devo fazer com estes dados?
Dizer quantos são pares e quantos são ímpares

3. Quais são as restrições deste problema?
Os números tem que ser inteiros

4. Qual é o resultado esperado?
Saber qantos valores pares temos e quantos ímpares temos

5. Qual é a sequência de passos a ser feitas para chegar ao resultado?
pedir numero 1
pedir numero 2
pedir numero 3
pedir numero 4
pedir numero 5
pedir numero 6
count if num /2 = 0
count if num /2 <> 0

print primeiro count if
print segundo count if
"""

num1 = int(input("Digite um número inteiro"))
num2 = int(input("Digite um número inteiro"))
num3 = int(input("Digite um número inteiro"))
num4 = int(input("Digite um número inteiro"))
num5 = int(input("Digite um número inteiro"))
num6 = int(input("Digite um número inteiro"))

lista = [num1, num2, num3, num4, num5, num6]

pares = sum (1 for num in lista if num % 2 == 0)
impares = sum (1 for num in lista if num % 2 != 0)
print(f"Existem {pares:.0f} valores pares dentre esses 6 que você falou")
print(f"Existem {impares:.0f} valores ímpares dentre esses 6 que você falou")
