"""
#74 vetor repetido

Crie um programa que preencha automaticamente (usando lógica, não apenas
atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
5 3 5 3 5 3 5 3 5 3
"""
vetor = []
i = 5
a = 1
while True:
    vetor.append(i)
    if i == 5:
        i = i - 2
    else:
        i = i + 2
    a = a + 1
    if a == 11:
        break

print(vetor)

    