# 8- Crea un programa que pida al usuario el radio de un círculo
#  y muestre su diámetro, su circunferencia y su área.
# Supón que pi es aproximadamente 3.14159.

pi = 3.14159
radio = float(input("Ingresa el valor del Radio: "))
diametro = radio * 2
circunferencia = pi * diametro
area = pi * (radio **2)

print(f"Este circulo tiene un diametro de {diametro}, su circunferencia es {circunferencia} y su area es {area}")
