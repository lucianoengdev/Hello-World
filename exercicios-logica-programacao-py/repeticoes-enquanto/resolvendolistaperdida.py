"""
#45 Resolvendo problema código acima

O programa acima vai ter um problema quando digitarmos o primeiro valor
maior que o último. Resolva esse problema com um código que funcione em qualquer
situação.
"""
inic = int(input("Digite o primeiro valor"))
fina = int(input("Digite o último valor"))
pulo = int(input("Digite o incremento"))

if inic > fina:
    inic, fina = fina, inic
    


for item in range (inic, fina + 1,pulo):
    print(item, end = "   ")
    
print("Acabou!")
