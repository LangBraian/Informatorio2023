# 13-Escribe un programa que solicite al usuario su nombre y su edad, y luego
# imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
nueva_edad = edad + 10

print(f'{nombre} tu edad en 10 años sera de {nueva_edad} años ')