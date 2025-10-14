"""
#61 Do while

Crie um programa que mostre na tela a seguinte contagem, usando a estrutura
“faça enquanto”
0 3 6 9 12 15 18 21 24 27 30 Acabou!
"""
num = 0
while True:

    print(num, end = "   ")
    num = num + 3
    if num > 30:
        break

print("Acabou!")