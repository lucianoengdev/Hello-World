"""
#50 Loucura total 

 Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e
mostre na tela:
a) Quais foram os números sorteados
b) Quantos números estão acima de 5
c) Quantos números são divisíveis por 3
"""
import random

num1 = random.randint(1,10)
print(num1)
num2 = random.randint(1,10)
print(num2)
num3 = random.randint(1,10)
print(num3)
num4 = random.randint(1,10)
print(num4)
num5 = random.randint(1,10)
print(num5)
num6 = random.randint(1,10)
print(num6)
num7 = random.randint(1,10)
print(num7)
num8 = random.randint(1,10)
print(num8)
num9 = random.randint(1,10)
print(num9)
num10 = random.randint(1,10)
print(num10)
num11 = random.randint(1,10)
print(num11)
num12 = random.randint(1,10)
print(num12)
num13 = random.randint(1,10)
print(num13)
num14 = random.randint(1,10)
print(num14)
num15 = random.randint(1,10)
print(num15)
num16 = random.randint(1,10)
print(num16)
num17 = random.randint(1,10)
print(num17)
num18 = random.randint(1,10)
print(num18)
num19 = random.randint(1,10)
print(num19)
num20 = random.randint(1,10)
print(num20)

lista = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12, num13, num14, num15, num16, num17, num18, num19, num20]

maior = sum(1 for num in lista if num > 5)
div3 = sum(1 for num in lista if num % 3 == 0)

print(f"Existem nesses números, {maior:.0f} maior(es) que 5")
print(f"Existem nesses números, {div3:.0f} divisível(veis) por 3")