texto = str(input("Digite um texto para traduzir pra linguagem do 'x': "))
linguagemx = ""

for i in texto:
    if i.lower() in "aeiou":
        if i.isupper():
            linguagemx = linguagemx + "X"
        else:
            linguagemx = linguagemx + "x"
    else: 
        linguagemx = linguagemx + i

print(linguagemx)