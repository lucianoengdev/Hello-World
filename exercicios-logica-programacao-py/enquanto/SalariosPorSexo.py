"""
#57 Salarios por sexo 

Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários.
No final, mostre o total de salários pagos aos homens e o total pago às
mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não
sempre que ler os dados de um funcionário.
1. Quais são os dados de entrada necessário?
Salario
Sexo
Quer continuar?

2. O que devo fazer com estes dados?
Dizer:
Média do salário dos homens
Média do salário das mulheres

3. Quais são as restrições deste problema?
Perguntar ao usuário se ele quer contunuar, se ele responder que não parar

4. Qual é o resultado esperado?
Média do salario masculino
Média do salário feminino

5. Qual é a sequência de passos a ser feitas para chegar ao resultado?
lista m
lista f

perguntar salario
perguntar genero

if masc vai soma a lista m
soma 1 ao gen m

else vai soma a lista f
soma 1 ao gen f

quer continuar?

if sim repete
else
lista m / gen m
lista f / gen f

print salario masculino
print salario feminino

"""

listasal = []
listagen = []

while True:
    sal = float(input("Qual seu salário?"))
    gen = input("Qual seu gênero (M ou F)?").capitalize()

    listasal.append(sal)
    listagen.append(gen)
    
    continua = input("Quer continuar (S ou N)?").capitalize()
    if continua == "N":
        break


somam = 0
somaf = 0
tamanhom = 0
tamanhof = 0

for i in range(len(listasal)):
    if listagen[i] == "M":
        somam = somam + listasal[i]
        tamanhom = tamanhom + 1

    else:
        somaf = somaf + listasal[i]
        tamanhof = tamanhof + 1

if tamanhom > 0:
    mediam = somam / tamanhom
    print(f"A média de salário masculina é de R${mediam:.2f} anos")
    
else:
    print("Nenhum homem foi cadastrado.")

if tamanhof > 0:
    mediaf = somaf / tamanhof
    print(f"A média de salário feminina é de R${mediaf:.2f} anos")
    
else:
    print("Nenhuma mulher foi cadastrada.")