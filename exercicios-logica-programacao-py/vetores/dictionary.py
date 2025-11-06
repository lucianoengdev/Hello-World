"""Dictionaries
Crie um dicionário com 3 países e capitais, imprima só as capitais.
Traduza números (“one”→1, …) baseando em input.
"""
Countrys = {
    "BR": "Brasil",
    "ES": "Espanha",
    "US": "Estados Unidos",
    }

print(Countrys.values())

pais = str(input("Digite o código do país desejado: "))
if pais in Countrys:
    print("O país falado é: " + Countrys[pais])
else:
    print("País não encontrado no dicionário")