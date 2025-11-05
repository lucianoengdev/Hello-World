"""Return Statement
Função que retorna o quadrado de um número.
Função que retorna o maior de dois números."""

def quad(number):
    return number * number

def bigger(n1, n2):
    return max(n1, n2)

number = int(input("Digite um número para descobrir o quadrado dele: "))
n1 = int(input("Digite o primeiro número para saber qual o maior entre 2 números: "))
n2 = int(input("Digite o segundo número para saber qual o maior entre 2 números: "))

quadrado = quad(number)
maior = bigger(n1, n2)
print(quadrado)
print(maior)