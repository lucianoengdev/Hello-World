"""
#27 Passou de ano?

Crie um programa que leia duas notas de um aluno e calcule a sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
 - Média até 4.9: REPROVADO
 - Média entre 5.0 e 6.9: RECUPERAÇÃO
 - Média 7.0 ou superior: APROVADO
 """

nota1 = float(input("Qual sua primeira nota?"))
nota2 = float(input("Qual sua segunda nota?"))
soma = nota1 + nota2
media = soma / 2

if media <= 4.9:
    print(f"Sua media é de {media:.1f}, portanto você está REPROVADO")

elif media <= 6.9:
        print(f"Sua media é de {media:.1f}, portanto você está em RECUPERAÇÃO")

else:
        print(f"Sua media é de {media:.1f}, portanto você está APROVADO")