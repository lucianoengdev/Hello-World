"""
#73 vetor logica reversa

Crie um programa que preencha automaticamente (usando lógica, não apenas
atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
9 8 7 6 5 4 3 2 1 0
0 1 2 3 4 5 6 7 8 9
"""
vetor = []
i = 9
while True:
    vetor.append(i)
    i = i - 1
    if i == -1:
        break
print(vetor)
