"""
#54 Peso e altura

Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando
no final:
a) Qual foi a média de altura do grupo
b) Quantas pessoas pesam mais de 90Kg
c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.

Passo a passo
c)
variavel <50kg e <1.6 igual a zero (contador)
for lista 1 para termos um indice
se <50 lista 1 e no mesmo indice na lista 2 é <1.6 entao soma 1 no contador

d)
variavel >1.9 e >100kg igual a zero (contador)
criar o indice da lista 1 para observar na lista 2
se na lista peso for maior que 100 e na lista alt for maior que 1.9 soma mais um ao contador

"""
peso1 = float(input("Qual o seu peso?"))
alt1 = float(input("Qual a sua altura?"))
peso2 = float(input("Qual o seu peso?"))
alt2 = float(input("Qual a sua altura?"))
peso3 = float(input("Qual o seu peso?"))
alt3 = float(input("Qual a sua altura?"))
peso4 = float(input("Qual o seu peso?"))
alt4 = float(input("Qual a sua altura?"))
peso5 = float(input("Qual o seu peso?"))
alt5 = float(input("Qual a sua altura?"))
peso6 = float(input("Qual o seu peso?"))
alt6 = float(input("Qual a sua altura?"))
peso7 = float(input("Qual o seu peso?"))
alt7 = float(input("Qual a sua altura?"))

listapeso = [peso1, peso2, peso3, peso4, peso5, peso6, peso7]
listaalt = [alt1, alt2, alt3, alt4, alt5, alt6, alt7]

somaalt = sum(listaalt)
mediaalt = somaalt / 7
print(f"A média de altura do grupo é de {mediaalt:.2f}")


mais20 = sum(1 for num in listapeso if num > 90)
print(f"existem {mais20:.0f} pessoas com mais do que 90kg")


baixaemagra = 0
for ind in range(len(listapeso)):
    if listapeso[ind] < 50 and listaalt[ind] < 1.5:
        baixaemagra = baixaemagra + 1
print(f"Existem {baixaemagra:.0f} pessoa(s) nessa lista com menos que 50kg e menor que 1,5m")


altoegordo = 0
for gor in range(len(listapeso)):
    if listapeso[gor] > 100 and listaalt[gor] > 1.9:
        altoegordo = altoegordo + 1
print(f"Existem {altoegordo:.0f} pessoa(s) nessa lista com mais do que 100kg e maior que 1,9m")