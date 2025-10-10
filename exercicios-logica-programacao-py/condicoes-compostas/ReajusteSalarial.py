"""
#29 Reajuste Salarial

Desenvolva um programa que leia o nome de um funcionário, seu salário,
quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
acordo com a tabela a seguir:
 - Até 3 anos de empresa: aumento de 3%
 - entre 3 e 10 anos: aumento de 12.5%
 - 10 anos ou mais: aumento de 20
 """
nome = str(input("Qual o seu nome?"))
sal = float(input("Qual o seu salário?"))
ano = int(input("Quantos anos você trabalha nessa empresa?"))

if ano <= 3:
    reaj1 = sal * 1.03
    print(f"Seu novo salário é de {reaj1:.2f}")

elif ano <= 10:
    reaj2 = sal * 1.125
    print(f"Seu novo salário é de {reaj2:.2f}")

else:
    reaj3 = sal * 1.2
    print(f"Seu novo salário é de {reaj3:.2f}")