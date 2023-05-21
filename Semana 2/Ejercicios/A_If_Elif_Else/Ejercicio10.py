# 10-Escribir un programa que pida al usuario una letra y muestre por pantalla si es
# una vocal o una consonante.

letra = input('Inserte una letra: ')

vocal = ['a','e','i','o','u']

if letra == vocal[0] or letra == vocal[1] or letra == vocal[2] or letra == vocal[3] or letra == vocal[4] :
    print('La letra',letra,'es una Vocal')
else:
    print('La letra',letra,'es una Consonante')