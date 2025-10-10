"""
#34 IMC

O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no
peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o
indivíduo dentro de certas faixas.
 - abaixo de 18.5: Abaixo do peso
 - entre 18.5 e 25: Peso ideal
 - entre 25 e 30: Sobrepeso
 - entre 30 e 40: Obesidade
 - acima de 40: Obseidade mórbida
Obs: O IMC é calculado pela expressão peso/altura² (peso dividido pelo quadrado
da altura)
"""
alt = float(input("Qual sua altura?"))
peso = float(input("Qual o seu peso?"))

altura = alt ** 2

imc = peso / altura

if imc <= 18.5:
    print(f"Você está abaixo do peso, seu IMC é de {imc:.1f}")

elif imc <= 25:
    print(f"Você está no peso ideal, seu IMC é de {imc:.1f}")

elif imc <= 30:
    print(f"Você está com sobrepeso, seu IMC é de {imc:.1f}")

elif imc <= 40:
    print(f"Você está com Obesidade, seu IMC é de {imc:.1f}")

else:
    print(f"Você está com obesidade Mórbida, seu IMC é de {imc:.1f}")