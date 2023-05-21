# 3-Escribir un programa que pida al usuario dos números y muestre por pantalla
# cuál de ellos es mayor.

numero1 = input('Ingresa un numero: ')
numero2 = input('Ingrese otro numero: ')

if numero1 > numero2:
    print(f'Entre los numeros {numero1} y {numero2}. El mayor es {numero1}')
else:
    print(f'Entre los numeros {numero1} y {numero2}. El mayor es {numero2}')