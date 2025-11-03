"""
#99 Potencia()

Faça um programa que possua uma função chamada Potencia(), que vai receber
dois parâmetros numéricos (base e expoente) e vai calcular o resultado da
exponenciação.
Ex: Potencia(5,2) vai calcular 52 = 25 
"""
def Potencia(base,expoente):
    result = base ** expoente
    return result

valor1 = int(input("Qual a base da sua potencia?"))
valor2 = int(input("Qual o expoente da sua potencia?"))
resultado = Potencia(valor1, valor2)
print(resultado)