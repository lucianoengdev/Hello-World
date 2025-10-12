"""
#47 Somando PA Decrescente 
Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 +
450 + 400 + 350 + 300 + ... + 50 + 0
"""
for item in range(500,0,-50):
    print(item, end = " + ")

print("0 =")

soma = sum(range(0,500,50))
print(soma)