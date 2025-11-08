"""Faça uma função leia inteiro e outre leia float mas com a certeza de que o usuário vai digitar esse números desses tipos"""

#for int
def leia_int():
    while True:
        try:
            inteiro = int(input("Digite um número inteiro: "))
            return inteiro
        except Exception as erro:
            print(f'O número digitado não é um número inteiro, o erro foi {erro}')

#for float
def leia_float():
    while True:
        try:
            decimal = float(input("Digite um número decimal: "))
            return decimal
        except Exception as erro:
            print(f"O número digitado não é um número decimal, o erro foi {erro}")

numint = leia_int()
numfloat = leia_float()

print(f"Você digitou {numint} e {numfloat}")