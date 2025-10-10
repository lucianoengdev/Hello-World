"""
#36 Programa Vida Saudável 

Um programa de vida saudável quer dar pontos atividades físicas que podem
ser trocados por dinheiro. O sistema funciona assim:
 - Cada hora de atividade física no mês vale pontos
 - até 10h de atividade no mês: ganha 2 pontos por hora
 - de 10h até 20h de atividade no mês: ganha 5 pontos por hora
 - acima de 20h de atividade no mês: ganha 10 pontos por hora
 - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos)
Faça um programa que leia quantas horas de atividade uma pessoa teve por mês,
calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar.
"""
hora = int(input("Quantas horas você se exercitou no mês?"))

if hora <= 10:
    ponto1 = hora * 2
    real1 = ponto1 * 0.05
    print(f"Parabéns, você se exercitou por {hora:.0f} horas, ganhou {ponto1:.0f} pontos e R${real1:.2f} reais")

elif hora <= 20:
    ponto2 = hora * 5
    real2 = ponto2 * 0.05
    print(f"Parabéns, você se exercitou por {hora:.0f} horas, ganhou {ponto2:.0f} pontos e R${real2:.2f} reais")

else:
    ponto3 = hora * 10
    real3 = ponto3 * 0.05
    print(f"Parabéns, você se exercitou por {hora:.0f} horas, ganhou {ponto3:.0f} pontos e R${real3:.2f} reais")