""""If Statements & Comparisons
Compare dois números e diga qual é maior.
Verifique se uma senha digitada é igual a “python123”."""

senha = str(input("Digite sua senha para acessar o programa: "))

if senha == "python123":
    n1 = int(input("Digite o primeiro número para saber qual o maior entre dois números: "))
    n2 = int(input("Digite o segundo número para saber qual o maior entre dois números: "))
    maior = max(n1, n2)
    print("O maior número entre esses dois é: " + str(maior))

else: 
    print("Você digitou a senha errada")