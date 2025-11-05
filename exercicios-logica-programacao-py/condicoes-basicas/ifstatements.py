"""If Statements
Verifique se uma idade é maior de 18.
Diga se uma temperatura é quente (>30), normal, ou fria (<15)."""

idade = int(input("Digite sua idade: "))
temp = int(input("Digite qual a temperatura na sua cidade: "))

is_maior = False
if idade >= 18:
    is_maior = True
    print("Já atingiu a maioridade")

if temp > 30:
    print("Sua cidade está quente!")

elif temp <= 30 and temp >= 15:
    print("Sua cidade está normal!")

else:
    print("Sua cidade está fria!")