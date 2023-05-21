# 11-Escribir un programa que pida al usuario dos números y muestre por pantalla
# la suma de ellos solo si ambos son pares.

num1 = float(input('Ingresa un nùmero: '))
num2 = float(input('Ingresa otro nùmero: '))
suma = num1 + num2

if not(num1%2) and not(num2%2):
    print(f'Como {num1} y {num2} son pares su suma es "{suma}"')
else:
    print(f'Como {num1} y {num2} no son pares no se suman')