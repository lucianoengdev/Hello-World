"""
#8 Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.

Ex:
Digite uma distância em metros: 185.72
A distância de 85.7m corresponde a:
0.18572Km
1.8572Hm
18.572Dam
1857.2dm
18572.0cm
185720.0mm
"""

numero = float(input("Digite uma distância em metros:"))
km = round(numero / 1000, 5)
hm = numero / 100
dam = round(numero / 10, 3)
dm = numero * 10
cm = round(numero * 100, 2)
mm = numero * 1000


print("A distância de " + str(numero) + "m corresponde a:")
print(str(km) + "Km")
print(f"{hm:.4f}Hm")
print(str(dam) + "Dam")
print(f"{dm:.1f}dm")
print(str(cm) + "cm")
print(f"{mm:.1f}mm")