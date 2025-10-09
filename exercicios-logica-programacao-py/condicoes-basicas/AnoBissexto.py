"""
#21 Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO.
"""
ano = int(input("Digite um ano"))
if ano % 4 == 0:
    print(f"O ano de {ano} é bissexto")
else:
    print(f"O ano de {ano} não é bissexto")