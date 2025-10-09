"""
#24 Preço de viagem

Faça um algoritmo que pergunte a distância que um passageiro deseja
percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
viagens até 200Km e R$0.45 para viagens mais longas.
"""

dist = int(input("Quantos km vamos percorrer?"))
if dist <= 200:
    pmaior = dist * 0.5
    print(f"O valor da sua corrida é de R${pmaior:.2f}")

else:
    pmenor = dist * 0.45
    print(f"O valor da sua corrida é de R${pmenor:.2f}")