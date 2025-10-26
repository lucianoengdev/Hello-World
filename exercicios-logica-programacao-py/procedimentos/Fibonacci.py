"""
#94 Fibonacci()

[DESAFIO] Desenvolva um aplicativo que tenha um procedimento chamado
Fibonacci() que recebe um único valor inteiro como parâmetro, indicando quantos
termos da sequência serão mostrados na tela. O seu procedimento deve receber
esse valor e mostrar a quantidade de elementos solicitados.
Obs: Use os exercícios 70 e 75 para te ajudar na solução
Ex:
Fibonacci(5) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> FIM
Fibonacci(9) vai gerar 1 >> 1 >> 2 >> 3 >> 5 >> 8 >> 13 >> 21 >> 34 >> FIM
"""
def Fibonacci(elementos):
    valor0 = 1
    valor1 = 1
    print(valor0, end = " >> ")
    print(valor1, end = " >> ")
    for i in range(elementos - 2):
        valor2 = valor0 + valor1
        print(valor2, end = " >> ")
        valor0 = valor1
        valor1 = valor2
    print("FIM")
    


extensao = int(input("Digite quantos valores serão mostrados em sequência na tela para a sequencia de Fibonacci:"))
Fibonacci(extensao)