# 2-Escribe un programa que pida al usuario un número y calcule la suma de todos
# los números naturales del 1 hasta ese número.

numero = int(input('Ingresa un numero: '))
suma = 0

for num in range(1,numero+1):
    suma = suma + num
print(f'La suma de todos los numeros naturales es "{suma}"')
