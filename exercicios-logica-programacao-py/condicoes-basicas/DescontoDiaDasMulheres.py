"""
#23 Desconto dia das mulheres

Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
para todos, mas especialmente para mulheres. Faça um programa que leia nome,
sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo
que:
 - Homens ganham 5% de desconto
 - Mulheres ganham 13% de desconto
"""

nome = str(input("Qual o seu nome?"))
sexo = str(input("Qual o seu sexo(M ou F)?"))
valor = float(input("Qual o valor das suas compras?"))
              
if sexo == str("M"):
    totalm = valor * 0.95
    print(f"Sua compra deu um valor total de R${totalm:.2f} reais")

else:
    totalf = valor * 0,87
    print(f"Sua compra deu um valor total de R${totalf:.2f} reais")