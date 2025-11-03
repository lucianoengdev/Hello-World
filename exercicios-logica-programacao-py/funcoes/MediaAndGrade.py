"""
#100 Media + aprovação

Melhore o exercício 96, criando além da função Media() uma outra função
chamada Situacao(), que vai retornar para o programa principal se o aluno está
APROVADO, em RECUPERAÇÃO ou REPROVADO. Essa nova função, vai receber como
parâmetro o resultado retornado pela função Media().
"""
def Media(num1, num2):
    soma = num1 + num2
    media = soma / 2
    return media

valor1 = float(input("Digite um número"))
valor2 = float(input("Digite um número"))

resultado = Media(valor1, valor2)

print(f"O aluno obteve de nota média {resultado:.2f}")

if resultado > 6:
    print("Com isso, ele está APROVADO")
elif resultado > 6:
    print("Com isso, ele está EM RECUPERAÇÃO")
else:
    print("Com isso, ele está REPROVADO")