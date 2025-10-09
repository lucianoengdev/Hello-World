"""
#18 Pode votar ou não

Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
dela e depois mostre se ela pode ou não votar.
"""
ano = int(input("Qual seu ano de nascimento?"))
idade = 2025 - ano

if idade <=15:
    print(f"Você tem apenas {idade} anos, por isso não pode votar, pois o mínimo são 16 anos para voto")

else:
    print(f"Você já pode votar, pois ultrapasssa a idade mínima de 16 anos, já que tem {idade} anos")