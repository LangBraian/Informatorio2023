# 13-Escribe un programa que pida al usuario un número y luego imprima un
# triángulo de asteriscos con esa cantidad de filas.
# *
# **
# ***
# ****
# *****

numero = int(input('Ingresa un numero: '))

for num in range(numero):
    for cantidad in range(num+1):
        print("*", end="")
    print()
