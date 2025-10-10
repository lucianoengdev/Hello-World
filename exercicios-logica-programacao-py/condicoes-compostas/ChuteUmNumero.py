"""
#32 Chute um Número

[DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
jogador vai tentar descobrir qual foi o valor sorteado.
"""
import random

aleatorio = random.randint(1,5)

acertou = False

while acertou == False:
    
    numero = int(input('Escreva um número entre 1 a 5'))
    if numero > aleatorio:
        print("Chute maior do que o valor gerado, tente novamente")
    
    elif numero < aleatorio:
        print("Chute menor do que o valor gerado, tente novamente")
    
    else:
        print("Você Acertou!")
        acertou = True 