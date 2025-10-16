"""
#70 Sequencia de Fibonacci

Faça um programa que mostre os 10 primeiros elementos da Sequência
de Fibonacci:
1 1 2 3 5 8 13 21...
variavel0 = 0
variavel1 = 1

print variavel0
print variavel1
i = 1
while true 
variavel2 = variavel0 + variavel1
variavel0 = variavel1
variavel1 = variavel2
print variavel2
if i = 10 break
i = i + 1
"""

variavel0 = 0
variavel1 = 1
print(variavel0, end = "  ")
print(variavel1, end = "  ")

i = 1
while True:
    variavel2 = variavel0 + variavel1
    variavel0 = variavel1
    variavel1 = variavel2
    print(variavel2, end = "  ")
    i = i + 1
    if i == 10:
        break

