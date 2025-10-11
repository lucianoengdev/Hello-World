"""
#46 Somando PA 

Crie um programa que calcule e mostre na tela o resultado da soma entre 6 +
8 + 10 + 12 + 14 + ... + 98 + 100.
"""
for item in range(6,100,2):
    print(item, end = " + ")

print("100 = ")
somatotal = sum(range(6,101,2))

print(somatotal)