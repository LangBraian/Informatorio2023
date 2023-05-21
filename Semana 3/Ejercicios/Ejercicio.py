# # 1-Escribe un programa que pida al usuario una palabra y luego imprima cada
# # letra de la palabra en una línea separada.

# palabras = input('Ingresa una palabra: ')

# for palabra in palabras:
#     print(palabra)

# # 2-Escribe un programa que pida al usuario un número y calcule la suma de todos
# # los números naturales del 1 hasta ese número.

# numero = int(input('Ingresa un numero: '))
# suma = 0

# for num in range(1,numero+1):
#     suma = suma + num
# print(f'La suma de todos los numeros naturales es "{suma}"')

# # 3-Escribe un programa que pida al usuario un número y luego imprima la tabla de
# # multiplicar correspondiente a ese número del 1 al 10.

# numero = int(input('Ingresa un numero: '))
# multiplicadores = [ ]
# tabla = 0
# for multiplicador in range(1.11):
#     tabla = numero * multiplicador
#     print(f'{numero} * {multiplicador} = {tabla}')

# # 4-Escribe un programa que imprima los números pares del 1 al 100.

# for i in range(1,101):
#     if i%2==0:
#         print(i)

# # 5-Escribe un programa que imprima la suma de todos los números pares del 1 al 100.

# par = 0
# for i in range(1,101):
#     if i%2==0:
#         par = par + i
# print(f'La suma de todos los numeros pares es: {par}')

# # 6-Escribe un programa que pida al usuario una palabra y luego imprima la misma
# # palabra pero con las letras en orden inverso.

# palabra = input('Ingresa una palabra:')

# print(palabra[::-1])

# # 6-Escribe un programa que pida al usuario una palabra y luego imprima la misma
# # palabra pero con las letras en orden inverso.

# palabra = input('Ingresa una palabra:')

# print(palabra[::-1])

# # 7-Escribe un programa que pida al usuario una palabra y determine si es un
# # palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
# # izquierda).

# palindromo = True
# for i in range(len(palabra)):
#     if palabra[i] != palabra[-i - 1]:
#         palindromo = False
#         break
# if palindromo:
#     print(f'La palabra {palabra} "Si" es un palindromo')
# else:
#     print(f'La palabra {palabra} "No" es un palindromo')

# # 8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# # el número de palabras que contiene.

# texto = input('Ingresa una cadena de texto: ').split()
# cantidad = len(texto)

# print(f'El texto tiene {cantidad} palabras')







# # 10-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# # la misma cadena pero con todas las vocales en mayúscula.

# texto = input('Ingrese un texto: ')
# texto_nuevo = ''
# for letra in texto:
#     if letra== "a"or letra=="e"or letra=="i"or letra=="o"or letra=="u":
#         texto_nuevo += letra.upper()
#     else:
#         texto_nuevo += letra
# print(texto_nuevo)

# # 11-Escribe un programa que pida al usuario un número y calcule su factorial.
# # Un factorial es el producto que resulta de multiplicar un número entero positivo
# # dado por todos los enteros inferiores a él hasta el uno. Por ejemplo, el factorial
# # de 4 es 4! = 4 × 3 × 2 × 1 = 24.

# numero = int(input('Ingresa un numero: '))
# factorial = 1

# for num in range(1,numero+1):
#     factorial = factorial * num
# print(f'El factorial del numero "{numero}" es "{factorial}"')

# # 12-Escribe un programa que pida al usuario una lista de números separados por
# # comas y calcule su promedio.

# numeros = input('Ingresa una lista de numero separados con la "," Ej: 2,3,4,5: ').split(",")
# suma = 0
# cantidad = len(numeros)
# for num in numeros:
#     suma = suma + int(num)
#     promedio = suma / cantidad
# print(f'El promedio de la lista {numeros} es de {promedio}')

# # 13-Escribe un programa que pida al usuario un número y luego imprima un
# # triángulo de asteriscos con esa cantidad de filas.
# # *
# # **
# # ***
# # ****
# # *****

# numero = int(input('Ingresa un numero: '))

# for num in range(numero):
#     for cantidad in range(num+1):
#         print("*", end="")
#     print()

# # 14-Escribe un programa que pida al usuario un número y luego imprima un
# # triángulo de números como el siguiente:
# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
# # 5 5 5 5 5

# numero = int(input('Ingresa un numero: '))
# suma=0
# for num in range(numero):
#     suma += 1
#     for cantidad in range(1,num+2):
        
#         print(suma, end="")
#     print()







# # 16-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# # la misma cadena pero con cada palabra al revés.

# texto = input('Ingrese una cadena de texto: ')
# lista = texto.split()

# for i in lista:
#     print(i[::-1], end=" ")

# # 17-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# # la misma cadena pero con las palabras en orden inverso.

# texto = input('Ingresa una cadena de texto: ').split()

# print(texto[::-1])

# # 18-Escribe un programa que pida al usuario un número y luego imprima un
# # triángulo de números como el siguiente:
# # 1
# # 2 3
# # 4 5 6
# # 7 8 9 10

# numero = int(input('Ingresa un numero: '))
# suma=0
# for num in range(numero):
    
#     for cantidad in range(1,num+2):
#         suma += 1
#         print(suma, end=" ")
#     print()

