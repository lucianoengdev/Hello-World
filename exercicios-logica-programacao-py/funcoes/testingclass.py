"""Classes & Objects
Crie classe Carro com atributos marca e ano.
Crie método que imprime descrição do carro.
"""
from classobject import Car

carro1 = Car("Celta", "2008")
carro2 = Car("Uno Quadrado", "2003")

#print(f"{carro1.car}, {carro1.year}")
#print(f"{carro2.car}, {carro2.year}")

print(carro1.age())