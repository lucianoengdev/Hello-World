import random
import string



letra = string.ascii_letters

lista = []
letras = int(input("Digite quantas letras você quer na senha: "))
numeros = int(input("Digite quantas números você quer na senha: "))
simbolos = int(input("Digite quantos símbolos você quer na senha: "))

n = letras + numeros + simbolos

for i in range(letras):
    lista.append(random.choice(letra))
for i in range(numeros):
    lista.append(random.randint(0,9))
for i in range(simbolos):
    lista.append(random.choice(["!", "?", "@", "*"]))

random.shuffle(lista)
print("".join(map(str, lista)))