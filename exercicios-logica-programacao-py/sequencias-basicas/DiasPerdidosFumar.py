"""
#16 Quantos dias de vida perdeu por fumar

[DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
quantos dias de vida um fumante perderá e exiba o total em dias.

1. Quais são os dados de entrada necessário?
Quantos cigarros o usuário fuma por dia
Quantos anos ele já fumou

2. O que devo fazer com estes dados?
Multiplicar o número de anos por 365 para saber o número de dias fumados
Multiplicar o número de dias fumados por quantos cigarros ele fuma por dia

Saber quantos cigarros são necessários para dar um dia (24h dividido por 10min)

3. Quais são as restrições deste problema?
Número de cigarros inteiro e positivo
Número de dias inteiro e positivo
A cada 4 anos fumados tem um dia a mais por ter passado por um ano bissexto                           #Vou ignorar inicialmente

4. Qual é o resultado esperado?
Saber quantos dias de vida o cigarro já tirou do fumante

5. Qual é a sequência de passos a ser feitas para chegar ao resultado?
Perguntar ao usuário o número de cigarros trabalhados no ano
Perguntar ao usuário a quantos anos ele fuma
Multiplicar o número de cigarros por 365
Multiplicar o resultado da multiplicação por quantos anos ele fuma

Multiplicar o número de cigarros por 10
Multiplicar 24 por 60 pra saber quantos minutos tem por dia
Dividir o número de minutos do cigarro calculado pelo número de minutos que tem em um dia

Retornar o resultado arredondado para o fumante
"""

cigarrosdia = int(input("Quantos cigarros você fuma por dia?"))
anos = int(input("A quantos anos você fuma?"))

cigarrostotal = cigarrosdia * 365
cigarrosano = cigarrostotal * anos
cigarrosmin = cigarrosano * 10

mindia = 24 * 60

tempodevida = cigarrosmin / mindia

print(f"Dado que fuma {cigarrosdia} cigarros por dia e já faz isso em um período de {anos}, o fumante já perdeu {tempodevida:.0f} dias de vida")
