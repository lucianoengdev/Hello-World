"""
#15 Salário do funcionário

Crie um programa que leia o número de dias trabalhados em um mês e mostre o
salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25
por hora trabalhada.

1. Quais são os dados de entrada necessário?
Quantos dias trabalhou no mês

2. O que devo fazer com estes dados?
Multiplicar o número de dias 8 para descobrir quantas horas trabalhadas no mês
Multiplicar o número de horas do mês pelo valor da hora trabalhada

3. Quais são as restrições deste problema?
Número de dias inteiro e positivo

4. Qual é o resultado esperado?
Saber o valor do funcionário no mês trabalhado

5. Qual é a sequência de passos a ser feitas para chegar ao resultado?
Perguntar ao usuário o número de dias trabalhados no mês
Multiplicar o número de dias por 8
Multiplicar o resultado da multiplicação por 25
Retornar o resultado
"""

dias = int(input("Quantos dias você trabalhou no mês?"))
salario = dias * 8 * 25

print(f"Você vai receber o valor de R${salario:.2f} por esse mês trabalhado")