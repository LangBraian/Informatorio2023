# 3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
# multiplicar correspondiente a ese número del 1 al 10.

numero = int(input('Ingresa un numero: '))
multiplicadores = [ ]
tabla = 0
for multiplicador in range(1.11):
    tabla = numero * multiplicador
    print(f'{numero} * {multiplicador} = {tabla}')
