"""
#52  Idade de um grupo

Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
a) Qual é a média de idade do grupo
b) Quantas pessoas tem mais de 18 anos
c) Quantas pessoas tem menos de 5 anos
d) Qual foi a maior idade lida
"""
num1 = int(input("Qual sua idade?"))
num2 = int(input("Qual sua idade?"))
num3 = int(input("Qual sua idade?"))
num4 = int(input("Qual sua idade?"))
num5 = int(input("Qual sua idade?"))
num6 = int(input("Qual sua idade?"))
num7 = int(input("Qual sua idade?"))
num8 = int(input("Qual sua idade?"))
num9 = int(input("Qual sua idade?"))
num10 = int(input("Qual sua idade?"))

lista = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
media = sum(lista) / 10
maior = sum(1 for num in lista if num > 18)
menos = sum(1 for num in lista if num < 5)
maxi = max(lista)

print(f"A média de idade é {media:.1f} anos")
print(f"Existem {maior:.0f} pessoas com mais de 18 anos")
print(f"Existem {menos:.0f} pessoas com menos de 5 anos")
print(f"A maior idade do grupo é de {maxi:.0f} anos")