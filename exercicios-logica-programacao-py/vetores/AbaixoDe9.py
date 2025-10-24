"""
#84 abaixo de 9

Crie um programa que leia o nome e a idade de 9 pessoas e guarde esses
valores em dois vetores, em posições relacionadas. No final, mostre uma listagem
contendo apenas os dados das pessoas menores de idade.
"""
vetor_nome = []
vetor_idade = []

vetor = []

for identidade in range(9):
    nome = input("Qual é o seu nome?")
    idade = int(input("Qual é a sua idade?"))
    vetor_nome.append(nome)
    vetor_idade.append(idade)

for pessoa in range(len(vetor_nome)):
    if vetor_idade[pessoa] < 18:
        nome_pessoa = vetor_nome[pessoa]
        idade_pessoa = vetor_idade[pessoa]
        vetor.append({'age': idade_pessoa, 'name': nome_pessoa})

print(vetor)