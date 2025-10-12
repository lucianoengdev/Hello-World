"""
#51 Maior e Menor

Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela
qual foi o maior e qual foi o menor preço digitados.
"""
num1 = float(input("Digite o preço do produto(R$)"))
num2 = float(input("Digite o preço do produto(R$)"))
num3 = float(input("Digite o preço do produto(R$)"))
num4 = float(input("Digite o preço do produto(R$)"))
num5 = float(input("Digite o preço do produto(R$)"))
num6 = float(input("Digite o preço do produto(R$)"))
num7 = float(input("Digite o preço do produto(R$)"))
num8 = float(input("Digite o preço do produto(R$)"))

lista = [num1, num2, num3, num4, num5, num6, num7, num8]

menor = min(lista)
maior = max(lista)

print(f"O maior preço entre os produtos é de R${maior:.2f} reais")
print(f"O menor preço entre os produtos é de R${menor:.2f} reais")