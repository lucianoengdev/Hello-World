"""
#96 Media() + return

Crie um programa que tenha uma função Media(), que vai receber as 2 notas de
um aluno e retornar a sua média para o programa principal.
"""
def Media(num1, num2):
    soma = num1 + num2
    media = soma / 2
    return media

valor1 = float(input("Digite um número"))
valor2 = float(input("Digite um número"))

resultado = Media(valor1, valor2)

print(f"O programa retornou {resultado}")