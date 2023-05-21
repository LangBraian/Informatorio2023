# 19-Escribe un programa que solicite al usuario un número decimal y luego
# imprima la parte entera y decimal por separado.

numero = input('Ingresa un numero decimal separado con la coma (,): ')
entero, decimal = numero.split(',')

print(f'El numero ingresado es "{numero}" del cual la parte entera es "{entero}" y la parte decimal "{decimal}"')