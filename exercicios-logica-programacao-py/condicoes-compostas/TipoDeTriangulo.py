"""
#30 Tipo de triângulo

[DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
 - EQUILÁTERO: todos os lados iguais
 - ISÓSCELES: dois lados iguais
 - ESCALENO: todos os lados diferentes

         [DESAFIO #25] Crie um programa que leia o tamanho de três segmentos de reta.
Analise seus comprimentos e diga se é possível formar um triângulo com essas
retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento
de cada lado deve ser menor que a soma dos outros dois.

1. Quais são os dados de entrada necessário?
3 segmentos de reta

2. O que devo fazer com estes dados?
Indicar se é possível as 3 retas formarem um triângulo

3. Quais são as restrições deste problema?
O valor de cada uma das retas tem que ser positivo
O comprimento de cada lado tem que ser menor do que os outros 2 somados

4. Qual é o resultado esperado?
Ter a resposta se é possível formar um triângulo ou não com esses segmentos de retas

5. Qual é a sequência de passos a ser feitas para chegar ao resultado?
pedir medida da reta A
pedir medida da reta B
pedir medida da reta C
if A < B + C; 
B < A + C;
C < A + B;
    é possível formar um triângulo
    if A = B = C = Equilátero;
     A <> B <> C = Escaleno
    else = ISÓSCELES
else não é possível
"""
reta1 = float(input("Qual a medida da sua primeira reta?"))
reta2 = float(input("Qual a medida da sua segunda reta?"))
reta3 = float(input("Qual a medida da sua terceira reta?"))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("É possível essas 3 retas formarem um triângulo")
    if reta1 == reta2 == reta3:
        print("Triângulo EQUILÁTERO")
    elif reta1 != reta2 == True and0 reta1 != reta3 == True and reta2 != reta3 == True:
        print("Triângulo ESCALENO")
    else:
        print("Triângulo ISÓSCELES")

else:
    print("Não é possível essas 3 retas formarem um triângulo")