"""
#85 dados pessoa

Faça um algoritmo que leia o nome, o sexo e o salário de 5 funcionários e
guarde esses dados em três vetores. No final, mostre uma listagem contendo
apenas os dados das funcionárias mulheres que ganham mais de R$5 mil.
"""
vetor_nome = []
vetor_sexo = []
vetor_salario = []
vetor_mul5 = []

for pessoa in range(5):
    nome = input("Qual o seu nome?")
    sexo = input("Qual o seu sexo (M ou F)?").capitalize()
    salario = float(input("Qual o seu salário?"))
    vetor_nome.append(nome)
    vetor_sexo.append(sexo)
    vetor_salario.append(salario)

for i in range(len(vetor_nome)):
    if vetor_sexo[i] == "F" and vetor_salario[i] > 5000:
        nom = vetor_nome[i]
        sex = vetor_sexo[i]
        sal = vetor_salario[i]
        vetor_mul5.append({'name': nom, 'gender': sex, 'pay(R$)': sal})

print(vetor_mul5)