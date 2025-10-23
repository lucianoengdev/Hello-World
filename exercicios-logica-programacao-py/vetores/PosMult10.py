"""
#78 Posição multiplo de 10 

Escreva um programa que leia 15 números e guarde-os em um vetor. No final,
mostre o vetor inteiro na tela e em seguida mostre em que posições foram
digitados valores que são múltiplos de 10.


if mul:
    soma_peso_mulher = 0
    for mulh in dados:
        if mulh['sex'] == "F":
            soma_peso_mulher = soma_peso_mulher + mulh['weight']
media_peso_mulher = soma_peso_mulher / mul
print(f"A média de peso entre as mulheres é de {media_peso_mulher:.1f}kg")

"""
vetor = []
i = 0
while True:
    i = i + 1
    num = int(input("Digite um número:"))
    vetor.append(num)
    if i == 15:
        break
print(vetor)

for mul, valor in enumerate(vetor):
    if valor % 10 == 0:
        print(mul, end = "  ")