"""
#55 Melhorar o jogo do #32

DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32. A partir de
agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4
tentativas para tentar acertar.

#32 Chute um Número

[DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
jogador vai tentar descobrir qual foi o valor sorteado.
"""
import random

aleatorio = random.randint(1,10)

for tent in range(4):
    num = int(input(f"Digite o número, essa é sua tentativa de número {tent + 1}"))


    if num == aleatorio:
        print("Parabéns, você acertou")
        break
    elif num > aleatorio:
        print("Errou, você chutou um número mais alto")
    else:
        print("Errou, você chutou um número mais baixo")


else:
print("Acabaram suas 4 tentativas")
print(f"O número aleatório era {aleatorio}")
