"""7
#17 Multa de velocidade

Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.

1. Quais são os dados de entrada necessário?
Velocidade do carro

2. O que devo fazer com estes dados?
Descobrir se tem multa a pagar e o valor da mesma

3. Quais são as restrições deste problema?
Velocidade do carro inteira e positiva

4. Qual é o resultado esperado?
Retornar ao usuário se recebeu multa e o valor dela

5. Qual é a sequência de passos a ser feitas para chegar ao resultado?
Perguntar ao usuário qual a velocidade ele estava conduzindo
se menor que 80 não tem multa

se maior que 80
(velocidade do veículo- 80) * 5 (por km a mais ultrapassado)
"""

vel = int(input("Qual a velocidade o veículo estava?"))

if vel <= 80:
    print("Você estava dentro da velocidade permitida")

else:
    passou = vel - 80
    multa = passou * 5
    print(f"Você ultrapassou a velocidade máxima permitida em {passou:.0f}km/h, portanto sua multa é de R${multa:.2f} reais")