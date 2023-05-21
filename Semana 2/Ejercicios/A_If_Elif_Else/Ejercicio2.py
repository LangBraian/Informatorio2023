# 2-Escribir un programa que pida al usuario un número entero y muestre por
# pantalla si es positivo, negativo o cero.

numero = int(input('Ingrese un numero entero: '))

if numero > 0:
    print(f'El nùmero {numero} es "Positivo"')
elif numero < 0:
    print(f'El nùmero {numero} es "Negativo"')
else:
    print(f'El nùmero {numero} es "0"')
