"""Try / Except
Tente converter input em número e trate erro."""

try:
    numero = int(input("Digite um número: "))
    print(numero)
except ValueError:
    print("Você tem que digitar um número inteiro")