# Desafio 2:
# Escribe un programa que solicite al usuario su informacion personal
# incluyendo su nombre completo, edad, peso, direccion y número de
# teléfono. A continuacion, el programa deberá imprimir un mensaje
# con los datos ingresados por el usuario en el siguiente formato:

# La informacion ingresada es la siguiente:
# Nombre Completo: [nombre completo]
# Edad: [edad]
# Estatura: [estatura] cm
# Peso: [peso] kg
# Dirección: [direccioón]
# Número de teléfono: [número de telefono]

nombre = input("Ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
estatura = input("Ingrese cuando mide usted de altura: ")
peso = input("Ingreso cuanto pesa actualmente: ")
direccion = input("Ingrese su direccion actual: ")
numero = int(input("Ingrese los 10 digitos de su numero de telefono sin 0 y sin 15. Ej: 3624201030: "))

print("La informacion ingresada es la siguiente:")
print(f"Nombre completo: {nombre}")
print(f"Edad: {edad}")
print(f"Estatura: {estatura} cm")
print(f"Peso: {peso} kg")
print(f"Dirección: {direccion}")
print(f"Número de teléfono: {numero}")
