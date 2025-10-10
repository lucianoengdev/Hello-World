"""
#31 [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)

Utilização de .capitalize() para garantir que a primeira letra seja maiúscula, tratando entradas como "pedra" ou "PEDRA".
"""
jogador1 = str(input("Qual sua escolha (Pedra/Papel/Tesoura)?")).capitalize()
jogador2 = str(input("Qual sua escolha (Pedra/Papel/Tesoura)?")).capitalize()

if jogador1 == jogador2:
    print("Empatou")
elif (jogador1 == "Pedra" and jogador2 == "Tesoura") or (jogador1 == "Papel" and jogador2 == "Pedra") or (jogador1 == "Tesoura" and jogador2 == "Papel"):
    print("Jogador 1 venceu")
else:
    print("Jogador 2 venceu")      