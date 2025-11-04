texto = input(str("Digite um texto com até 4 palavras: "))

a = 0
e = 0
i = 0
o = 0
u = 0
for j in texto:
    if j == "a":
        a = a + 1
    if j == "e":
        e = e + 1
    if j == "i":
        i = i + 1
    if j == "o":
        o = o + 1
    if j == "u":
        u=+1

print(f"a = {a}, e = {e}, i = {i}, o = {o}, u = {u}")