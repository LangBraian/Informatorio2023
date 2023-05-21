# 9-Escribir un programa que pida al usuario tres números y muestre por pantalla
# el mayor de ellos.

numero = input('Coloca 3 numeros separados por la coma "Ej: 3,5.1,9": ')

num1, num2, num3 = numero.split(',')

if num1 > num2 and num1 > num3:
    print(f'De los numeros ingresados {numero} el mayor es "{num1}"')
elif num2 > num1 and num2 > num3:
    print(f'De los numeros ingresados {numero} el mayor es "{num2}"')
elif num3 > num1 and num3 > num2:
    print(f'De los numeros ingresados {numero} el mayor es "{num3}"')