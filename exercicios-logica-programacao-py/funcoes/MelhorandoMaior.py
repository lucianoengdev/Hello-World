"""
#97

Refaça o exercício 91, só que agora em forma de função Maior(), mas faça uma
adaptação que vai receber TRÊS números como parâmetro e vai retornar qual foi o
maior entre eles.
"""
def Maior(num1, num2, num3):
    if num1 == num2 == num3:
        return("Os três valores são iguais")
    elif num1 == num2 and num1 > num3 or num1 == num3 and num1 > num2 or num2 == num3 and num2 > num1:
        maiorigual = max(num1,num2,num3)
        return(f"Dois valores são iguais e maiores, é o {maiorigual}")
    else:
        maior = max(num1, num2, num3)
        return maior


valor1 = int(input("Digite um número:"))
valor2 = int(input("Digite um número:"))
valor3 = int(input("Digite um número:"))

resultado = Maior(valor1, valor2, valor3)
print(f"{resultado}")