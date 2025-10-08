"""
#9 Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.
"""

real = float(input("Quantos reais voce tem na carteira?"))
dolar = real / 3.45

print(f"Com R${real:.2f} reais na carteira, você pode comprar US${dolar:.2f}")