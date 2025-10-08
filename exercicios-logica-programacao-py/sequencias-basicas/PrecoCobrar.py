"""
#14 Preço a cobrar (locadora de carros)

A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

1. Quais são os dados de entrada necessário?
Quantos dias ficou com o carro
Quantos km percorreu com o carro

2. O que devo fazer com estes dados?
Multiplicar o número de dias por 90
Multiplicar o número de km por 0,20

3. Quais são as restrições deste problema?
Número de dias inteiro e positivo
Número de km positivo

4. Qual é o resultado esperado?
Soma das multiplicações do número de dias com o número de km

5. Qual é a sequência de passos a ser feitas para chegar ao resultado?
Perguntar ao usuário o número de dias que ficou com o carro
Perguntar ao usuário quantos km percorreu com o carro
Multiplicar o número de dias por 90
Multiplicar o número de km por 0,20
Somar as multiplicações
Retornar o resultado
"""

dias = int(input("Quantos dias você ficou com o carro?"))
km = float(input("Quantos kms você percorreu com o carro?"))

total = (dias * 90) + (km * 0.20)

print(f"O valor total a ser pago por esse aluguel é de R${total:.2f}")