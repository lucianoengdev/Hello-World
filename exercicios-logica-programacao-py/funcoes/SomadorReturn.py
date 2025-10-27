"""
#95 Somador() + return

Refaça o exercício 90, só que agora em forma de função Somador(), que vai
receber dois parâmetros e vai retornar o resultado da soma entre eles para o
programa principal.
"""
def Somador(num1, num2):
    soma = num1 + num2
    return soma

num1 = int(input("Digite um número"))
num2 = int(input("Digite um número"))

resultado = Somador(num1, num2)

print(f"O programa retornou {resultado}")