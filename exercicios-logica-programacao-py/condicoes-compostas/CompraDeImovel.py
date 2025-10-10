"""
#33 Compra de Imóvel

Escreva um programa para aprovar ou não o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
ela não pode exceder 30% do salário ou então o empréstimo será negado.

1. Quais são os dados de entrada necessário?
Valor da casa
Salario do comprador
Em quantos anos vai pagar

2. O que devo fazer com estes dados?
Calcular qual o valor da parcela da casa

3. Quais são as restrições deste problema?
O valor da parcela não pode exceder 30% do salário do comprador

4. Qual é o resultado esperado?
Saber se será possível comprar a casa ou não, e se possível, qual o valor da parcela

5. Qual é a sequência de passos a ser feitas para chegar ao resultado?
pedir o valor da casa
pedir o salário do comprador
pedir em quantos anos ele vai pagar

anos * 12 = número de meses que ele vai pagar
salário * 0,3 valor máximo da parcela
valor da casa / número de meses = valor da parcela

if valor da parcela é menor que o valor máximo ele pode comprar
else não pode comprar
"""
casa = float(input("Qual o valor da casa?"))
sal = float(input("Quanto você ganha por mês?"))
anos = float(input("Em quantos anos você vai pagar a casa?"))

meses = 12 * anos
parcelas = casa / meses
maxi = sal * 0.3

if parcelas <= maxi:
    print(f"Você pode comprar a casa, e o valor da parcela vai ser de R${parcelas:.2f} por mês durante {meses:.0f} meses.") 

else:
    print(f"Você não pode comprar a casa, porque o valor da parcela vai ser de R${parcelas:.2f} que é maior que 30% do seu salário.") 