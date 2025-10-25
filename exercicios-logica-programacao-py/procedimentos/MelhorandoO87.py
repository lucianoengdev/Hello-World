"""
#88 melhorando o 87

Crie um programa que melhore o procedimento Gerador() da questão anterior
para que mostre uma mensagem vário
Ex: Ao chamar Gerador("Aprendendo Portugol", 4) aparece:
+-------=======------+
 Aprendendo Portugol
 Aprendendo Portugol
 Aprendendo Portugol
 Aprendendo Portugol
+-------=======------+
"""
def Gerador(mensagem, vezes):
    print("+-----========-----+")
    for i in range(vezes):
        print(f"{mensagem}")
    print("+-----========-----+")

Gerador("Aprendendo Portugol",4)