"""
#11 Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.

1. Quais são os dados de entrada necessário?
Valores A, B e C da função

2. O que devo fazer com estes dados?
Calcular o valor de delta de função de segundo grau ax^2 + bx + c = y

3. Quais são as restrições deste problema?

4. Qual é o resultado esperado?
Valor de delta = b^2 -4ac

5. Qual é a sequência de passos a ser feitas para chegar ao resultado?
Pedir ao usuário os valores de A, B e C
Elevar B ao quadrado
multiplicar A x C x -4
Subtrair o resultado de b^2 pela multipplicação
"""

valorA = float(input("Qual o valor de A da sua função?"))
valorB = float(input("Qual o valor de B da sua função?"))
valorC = float(input("Qual o valor de C da sua função?"))

belevado = valorB * valorB
multiplicacao = valorA * valorC * -4

resultado = belevado - multiplicacao

print(f"Dado os valores preenchidos A, B e C, respectivamente {valorA:.2f}, {valorB:.2f} e {valorC:.2f}, o resultado de delta é {resultado:.2f}")