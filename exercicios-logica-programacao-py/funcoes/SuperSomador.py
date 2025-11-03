"""
#98 SuperSomador()

Crie um programa que tenha uma função SuperSomador(), que vai receber dois
números como parâmetro e depois vai retornar a soma de todos os valores no
intervalo entre os valores recebidos.
Ex:
SuperSomador(1, 6) vai somar 1 + 2 + 3 + 4 + 5 + 6 e vai retornar 21
SuperSomador(15, 19) vai somar 15 + 16 + 17 + 18 + 19 e vai retornar 85
"""
def SuperSomador(num1,num2):
    ini = 0
    for i in range(num1,num2 + 1):
        ini = ini + i
    return ini

valor1 = int(input("Digite o primeiro número que você quer somar todo o intervalo:"))
valor2 = int(input("Digite o segundo número que você quer somar todo o intervalo:"))
resultado = SuperSomador(valor1,valor2)
print(resultado)