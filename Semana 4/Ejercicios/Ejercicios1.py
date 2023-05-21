# 1-Crea una función llamada suma que tome dos números como parámetros y
# devuelva la suma de ellos.

def sumando(num,num2):
    '''Sirve para realizar la suma de dos numeros'''
    suma = num + num2
    print(f'La suma de los dos numeros es "{suma}"')
    return suma

sumando(2,4)