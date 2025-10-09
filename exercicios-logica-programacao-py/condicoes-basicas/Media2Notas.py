"""
#19 Média de 2 notas

Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
não um bom aproveitamento (se ficou acima da média 7.0).
"""

nota1 = float(input("Quanto você tirou na primeira prova?"))
nota2 = float(input("Quanto você tirou na segunda prova?"))
soma = nota1 + nota2
media = soma / 2 
if media > 7:
    print(f"Parabéns, você alcançou {media:.2f} de nota média, sendo um valor satisfatório")

else:
    print(f"Não foi dessa vez, você alcançou {media:.2f} de nota média, sendo um valor não satisfatório")