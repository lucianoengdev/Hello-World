"""O usuário escolhe +, -, *, / e insere números.
Adicione opção para potência **."""

operation = int(input("Qual tipo de operação quer fazer? (1-div, 2-mult, 3-soma, 4-sub):"))
n1 = float(input("Qual o primeiro número da operação? "))
n2 = float(input("Qual o segundo número da operação? "))


res = 0
if operation == 1:
    res = n1 / n2
elif operation == 2:
    res = n1 * n2
elif operation == 3:
    res = n1 + n2
else:
    res = n1 - n2

print("O resultado da sua operação é: " + str(res))