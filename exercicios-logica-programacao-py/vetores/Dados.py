"""
#81 dados 

Crie um programa que leia a idade de 8 pessoas e guarde-as em um vetor. No
final, mostre:
a) Qual é a média de idade das pessoas cadastradas
b) Em quais posições temos pessoas com mais de 25 anos
c) Qual foi a maior idade digitada (podem haver repetições)
d) Em que posições digitamos a maior idade
"""
vetor = []
for i in range(8):
    idade = int(input("Qual a sua idade?"))
    vetor.append(idade)

soma_idades = sum(vetor)
media_idades = soma_idades / 8
print(f"A média das idades é de {media_idades:.1f} anos")

vetorposicoes = []
for ind, valor in enumerate(vetor):
    if valor > 25:
        vetorposicoes.append(ind)
print("Temos pesoas com mais de 25 anos nas posições: ", end = "  ")
print(vetorposicoes)

maior_idade = max(vetor)
print(f"A maior idade digitada foi de {maior_idade:.0f} anos")

posicoesmaioridade = []
for ida, valor in enumerate(vetor):
    if valor == maior_idade:
        posicoesmaioridade.append(ida)