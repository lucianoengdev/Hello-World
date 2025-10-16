"""
#69 desafio for

[DESAFIO] Desenvolva um programa que leia o primeiro termo e a razão de uma
PA (Progressão Aritmética), mostrando na tela os 10 primeiros elementos da PA e
a soma entre todos os valores da sequência.
"""
primeiro_termo = int(input("Digite qual o primeiro valor da PA:"))
razao = int(input("Digite qual a razão da PA:"))

ultimo_termo = (razao * 9) + primeiro_termo

for i in range(primeiro_termo,ultimo_termo, razao):
    print(i, end = " + ")
print(ultimo_termo, end = " = ")

pa = (primeiro_termo + ultimo_termo) * 5
print(pa)
    
