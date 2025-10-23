"""
#77 Lista Vetor Coontrário

Faça um programa que leia 7 nomes de pessoas e guarde-os em um vetor. No
final, mostre uma listagem com todos os nomes informados, na ordem inversa
daquela em que eles foram informados.
"""
vetor = []

i = 0
while True:
    i = i + 1 
    nome = input("Qual o seu nome?")
    vetor.append(nome)
    if i == 7:
        break

vetor_reverse = vetor[::-1]
print(vetor_reverse)