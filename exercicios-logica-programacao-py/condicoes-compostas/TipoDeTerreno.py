"""
#28  Qual o tipo de terreno?

Faça um programa que leia a largura e o comprimento de um terreno
retangular, calculando e mostrando a sua área em m². O programa também
deve mostrar a classificação desse terreno, de acordo com a lista abaixo:
 - Abaixo de 100m² = TERRENO POPULAR
 - Entre 100m² e 500m² = TERRENO MASTER
 - Acima de 500m² = TERRENO VIP
 """

lar = float(input("Qual a largura do seu terreno?"))
comp = float(input("Qual o comprimento do seu terreno?"))
area = lar * comp
print(f"A área do seu terreno é de {area:.2f}m²")

if area <= 100:
      print("TERRENO POPULAR")

elif area <= 500:
    print("TERRENO MASTER")

else:
    print("TERRENO VIP")