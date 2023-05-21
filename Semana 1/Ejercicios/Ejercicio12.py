# 12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
# dd/mm/aaaa y luego imprima su edad en años.
# Utiliza la función .split()

fecha_de_nacimiento = input("Escribe tu fecha de nacimiento con el formato dd/mm/aaaa: ")

dia, mes, anio = fecha_de_nacimiento.split("/")

edad = 2023 - int(anio)

print(f'Tienes {edad} años')

#Se puede mejorar el codigo utilizando un IF para el mes.