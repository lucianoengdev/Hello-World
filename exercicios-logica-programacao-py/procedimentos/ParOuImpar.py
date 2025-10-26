"""
#92 ParouImpar()

Crie uma lógica que leia um número inteiro e passe para um procedimento
ParOuImpar() que vai verificar e mostrar na tela se o valor passado como
parâmetro é PAR ou ÍMPAR.
"""
def ParOuImpar(valor):
    if valor % 2 == 0:
        print("Esse número é par")
    else:
        print("Esse número é ímpar")

val = int(input("Digite um número:"))
ParOuImpar(val)