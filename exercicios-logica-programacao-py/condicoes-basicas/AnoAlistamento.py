"""
#22 Ano de alistamento
Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
situação em relação ao alistamento militar.
 - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o
alistamento.
 - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do
alistamento.
"""

ano = int(input("Qual seu ano de nascimento?"))
idade = 2025 - ano

if idade < 18:
    faltam = 18 - idade
    print (f"Faltam {faltam} para o seu alistamento")
           
elif idade == 18:
    print ("Você tem que se alistar esse ano")

else:
    passaram = idade - 18
    print (f"Você deveria ter se alistado a {passaram} anos atrás")