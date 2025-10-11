"""
#44 Lista Pedida

Crie um algoritmo que leia o valor inicial da contagem, o valor final e o
incremento, mostrando em seguida todos os valores no intervalo:
Ex: Digite o primeiro Valor: 3
Digite o último Valor: 10
Digite o incremento: 2
Contagem: 3 5 7 9 Acabou!
"""
inic = int(input("Digite o primeiro valor"))
fina = int(input("Digite o último valor"))
pulo = int(input("Digite o incremento"))

for item in range (inic, fina + 1,pulo):
    print(item, end = "   ")
    
print("Acabou!")