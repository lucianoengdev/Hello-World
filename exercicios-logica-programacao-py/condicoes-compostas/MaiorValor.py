"""
#26 Qual maior valor?

Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
na tela uma das mensagens abaixo:
 - O primeiro valor é o maior
 - O segundo valor é o maior
 - Não existe valor maior, os dois são iguais
 """

num1 = int(input("Digite um número"))
num2 = int(input("Digite um número"))

if num1 > num2:
    print("O primeiro número é maior")

elif num1 == num2:
    print("Não existe valor maior, os dois são iguais")

else: 
    print("O segundo número é maior")