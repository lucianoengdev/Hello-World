"""
#35 

Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O
aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para
carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e
quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
tabela a seguir:
 - Carros populares (aluguel de R$90 por dia)
 - Até 100Km percorridos: R$0,20 por Km
 - Acima de 100Km percorridos: R$0,10 por Km
 - Carros de luxo (aluguel de R$150 por dia)
 - Até 200Km percorridos: R$0,30 por Km
 - Acima de 200Km percorridos: R$0,25 por Km
 """

carro = str(input("Qual Carro você utilizou (Popular ou Luxo?)")).capitalize()
km = int(input("Quantos km percorridos?"))

if carro == "Popular" and km <= 100:
    dist1 = km * 0.2
    total1 = 90 + dist1
    print(f"O valor do seu aluguel é de R${total1:.2f}")

elif carro == "Popular" and km > 100:
    dist2 = km * 0.1
    total2 = 90 + dist2
    print(f"O valor do seu aluguel é de R${total2:.2f}")

elif carro == "Luxo" and km <= 100:
    dist3 = km * 0.3
    total3 = 150 + dist3
    print(f"O valor do seu aluguel é de R${total3:.2f}")

else:
    dist4 = km * 0.25
    total4 = 150 + dist4
    print(f"O valor do seu aluguel é de R${total4:.2f}")