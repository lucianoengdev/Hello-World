"""
#82 Nota Media

Faça um algoritmo que leia a nota de 10 alunos de uma turma e guarde-as em
um vetor. No final, mostre:
a) Qual é a média da turma
b) Quantos alunos estão acima da média da turma
c) Qual foi a maior nota digitada
d) Em que posições a maior nota aparece
"""
vetor = []
for nota in range(10):
    valor = float(input("Qual a sua nota?"))
    vetor.append(valor)

soma_notas = sum(vetor)
media_notas = soma_notas / 10
print(f"A nota média da turma é de {media_notas:.1f}")

qtde_alunos = 0
for val in vetor:
    if val > media_notas:
        qtde_alunos = qtde_alunos + 1
print(f"{qtde_alunos:.0f} tiraram nota acima da média da turma")

maior_nota = max(vetor)
print(f"A maior nota digitada foi {maior_nota:.2f}")

print("A(s) posição(ões) onde ocorreu(ram) a maior nota, foi(ram):", end = " ")
for mai, ior in enumerate(vetor):
    if ior == maior_nota:
        print(mai, end = " ")