"""
#37 Reajuste Salarial

Uma empresa precisa reajustar o salário dos seus funcionários, dando um
aumento de acordo com alguns fatores. Faça um programa que leia o salário atual,
o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa.
No final, mostre o seu novo salário, baseado na tabela a seguir:
- Mulheres
 - menos de 15 anos de empresa: +5%
 - de 15 até 20 anos de empresa: +12%
 - mais de 20 anos de empresa: +23%
- Homens
 - menos de 20 anos de empresa: +3%
 - de 20 até 30 anos de empresa: +13%
 - mais de 30 anos de empresa: +25%
 """
sal = float(input("Qual seu salário atual?"))
gen = str(input("Qual seu gênero (M ou F)?")).capitalize()
temp = int(input("Quantos anos você tem de empresa?"))

if gen == "F" and temp < 15:
    sal1 = sal * 1.05
    print(f"Seu novo salário é de R${sal1:.2f} reais")

elif gen == "F" and temp <= 20:
    sal2 = sal *1.12
    print(f"Seu novo salário é de R${sal2:.2f} reais")

elif gen == "F" and temp > 20:
    sal3 = sal * 1.23
    print(f"Seu novo salário é de R${sal3:.2f} reais")

elif gen == "M" and temp < 20:
    sal4 = sal * 1.03
    print(f"Seu novo salário é de R${sal4:.2f} reais")

elif gen == "M" and temp <= 30:
    sal5 = sal * 1.13
    print(f"Seu novo salário é de R${sal5:.2f} reais")

else:
    sal6 = sal * 1.25
    print(f"Seu novo salário é de R${sal6:.2f} reais")