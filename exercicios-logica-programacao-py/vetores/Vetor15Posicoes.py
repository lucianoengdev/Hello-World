"""
#75 Vetor 15 posições 

Crie um programa que preencha automaticamente (usando lógica, não apenas
atribuindo diretamente) um vetor numérico com 15 posições com os primeiros
elementos da sequência de Fibonacci:
1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
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
    if i == 15:
        break