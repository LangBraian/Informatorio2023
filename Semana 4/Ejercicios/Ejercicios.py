# # 1-Crea una función llamada suma que tome dos números como parámetros y
# # devuelva la suma de ellos.

# def sumando(num,num2):
#     '''Sirve para realizar la suma de dos numeros'''
#     suma = num + num2
#     return suma

# print(f'La suma de los dos numeros es "{sumando(2,4)}"')

# # 2-Crea una función llamada saludo que tome el nombre de una persona como
# # parámetro e imprima un saludo personalizado.

# def saludos(nombre):
#     '''Saluda de manera personalizada el nombre ingresado'''
#     saludo = print(f'Buenos Dias {nombre}, esperamos que tengas un excelente dia')

# saludos("Braian")

# 3-Crea una función llamada invertir_cadena que tome una cadena de texto como
# parámetro y devuelva la cadena invertida.


# def invertir_cadena(cadena):
#     '''Esta funcion invierte una cadena de caracteres'''
#     texto = ''
#     for letra in range(len(cadena) -1,-1,-1):
#         texto = texto + cadena[letra]
#     return texto

# '''Texto que ingresa el usuario'''
# frase = input('Ingresa una frase: ')

# '''Se aplica la funcion para invertir el texto'''
# frase_invertida = invertir_cadena(frase)

# '''Muestra el texto'''
# print('Texto original:',frase)
# print('Texto invertido:',frase_invertida)

# # 4-Crea una función llamada es_capicua que tome un número como parámetro y
# # devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
# # derecha a izquierda) y False en caso contrario.

# def es_capicua(numero):
#     numero_str=str(numero)
#     cantidad_digito=len(numero_str)

#     if(cantidad_digito%2==0):
#         vueltas=int(cantidad_digito/2)
#         acumulador=0
#         for i in range(vueltas):
#             if(numero_str[i]==numero_str[cantidad_digito-i-1]):
#                 acumulador+=1
        
#         if(acumulador==vueltas):
#             print(f'El numero {numero} es capicua')
#         else:
#             print(f'El numero {numero} no es capicua')
#     else:
#         vueltas=int((cantidad_digito-1)/2)
#         acumulador=0
#         for i in range(vueltas):
#             if(numero_str[i]==numero_str[cantidad_digito-i-1]):
#                 acumulador+=1
        
#         if(acumulador==vueltas):
#             print(f'El numero {numero} es capicua')
#         else:
#             print(f'El numero {numero} no es capicua')   

# es_capicua(10101)

# # 5-Crea una función llamada es_divisible que tome dos números enteros como
# # parámetros y devuelva Es divisible si el primer número es divisible por el
# # segundo número, o No es divisible en caso contrario.

# def es_divisible(num1,num2):
#     if num1%num2==0:
#         print(f'El numero {num1} es divible del numero {num2}')
#     else:
#         print(f'El numero {num1} no es divible del numero {num2}')
#     return es_divisible    
    
# es_divisible(num1=6,num2=2)

# # 6-Crea una función llamada es_par que tome un número como parámetro y
# # devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
# # devuelva Es impar o No es par.

# def es_par(numero):
#     if numero%2==0:
#         print(f'El numero {numero} es PAR')
#     else:
#         print(f'El numero {numero} es IMPAR')

# es_par(2)

# # 7-Crea una función llamada imprimir_pares que tome un número entero como
# # parámetro y imprima todos los números pares desde 1 hasta ese número.

# def imprimir_pares(numero):
#     pares=0
#     impares=0
#     for i in range(1,numero+1):
#         if i%2==0:
#             pares=i
#             print(pares, end=" ")

# imprimir_pares(9)

# 8-Crea una función llamada es_palindromo que tome una cadena de texto como
# parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual
# de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso
# contrario.

# def es_palindromo(palabra):
#     palindromo = True
#     for i in range(len(palabra)):
#         if palabra[i] != palabra[-i - 1]:
#             palindromo = False
#             break
#     if palindromo:
#         print(f'La palabra {palabra} "Si" es un palindromo')
#     else:
#         print(f'La palabra {palabra} "No" es un palindromo')

# es_palindromo('menem')

# # 9-Crea una función llamada promedio que tome una lista de números como
# # parámetro y devuelva el promedio de esos números.

# def promedio(*args):
#     suma = 0
#     cantidad = len(args)
#     for num in args:
#         suma = suma + int(num)
#         promedio = suma / cantidad
#     print(f'El promedio de la lista {args} es de {promedio}')

# promedio(2, 3, 4)

# # 10-Crea una función llamada calcular_factorial que tome un número entero como
# # parámetro y devuelva el factorial de ese número. El factorial de un número
# # entero positivo n se define como el producto de todos los números enteros
# # positivos desde 1 hasta n.

# def calcular_factorial(numero):
#     factorial = 1

#     for num in range(1,numero+1):
#         factorial = factorial * num
#     print(f'El factorial del numero "{numero}" es "{factorial}"')

# calcular_factorial(4)

# # 11-Crea una función llamada contar_vocales que tome una cadena de texto como
# # parámetro y devuelva el número de vocales que contiene.

# def contar_vocales(texto):
#     contar=0
#     for i in texto:
#         if i == "a"or i=="e" or i=="i" or i=="o" or i=="u":
#             contar+=1
#     print(f'El texto: "{texto}" tiene "{contar}" vocales ')

# contar_vocales('hola, como estas?')

# # 12-Crea una función llamada convertir_temperatura que tome una temperatura
# # en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
# # es: Fahrenheit = (Celsius * 9/5) + 32.

# def convertir_temperatura(temperatura):
#     f = (temperatura * 9/5) + 32
#     print(f'''La temperatura de: 
# {temperatura}º Celsius = {f}º Fahrenheit''')

# convertir_temperatura(30)

# # 13-Crea una función llamada calcular_descuento que tome dos parámetros:
# # precio y porcentaje_descuento. La función debe calcular y devolver el precio
# # después de aplicar el descuento.

# def calcular_descuento(precio=None,descuento=None):
#     porcentaje = precio - (precio * (descuento/100))
#     print(f'''El articulo cuesta ${precio} y tiene un {descuento}% de descuento
# por lo que te quedaria en ${porcentaje} finales''')

# calcular_descuento(99,25)

# # 14-Crea una función llamada encontrar_maximo que tome una lista de números
# # como parámetro y devuelva el número máximo de la lista.

# def encontrar_maximo(*args):
#     numero_max = args[0]
#     for i in range(len(args)):
#         if args[i] > numero_max:
#             numero_max = args[i]
#     print(f'En la lista: {args} el numero maximo es "{numero_max}"')
#  #Extra en que posicion se encuentra:   
#     print(f'El numero {numero_max} se encuentra en la posicion {args.index(numero_max)}')
# encontrar_maximo(2,3,10,3,1)

# # 15-Crea una función llamada contar_palabras que tome una cadena de texto
# # como parámetro y devuelva el número de palabras que contiene. Se considera
# # que las palabras están separadas por espacios.

# def contar_palabras(cadena):
#     lista = cadena.split()
#     cantidad = len(lista)
#     print(f'La cadena: "{cadena}" tiene {cantidad} palabras')

# contar_palabras('Hola como estas?')

# # 16-Crea una función llamada eliminar_duplicados que tome una lista como
# # parámetro y devuelva una nueva lista sin duplicados, conservando el orden
# # original.

# def eliminar_duplicados(*args):
#     conjunto = set(args)
#     lista = list(conjunto)
#     print(lista)

# eliminar_duplicados(2,3,4,1,2,2,2,3,4,'braian','eduin','lang','eduin')

# # 17-Crea una función llamada es_anagrama que tome dos cadenas de texto como
# # parámetros y devuelva True si son anagramas (es decir, si tienen las mismas
# # letras pero en distinto orden), o False en caso contrario.

# def es_anagrama(cadena1,cadena2):
#     if sorted(cadena1) == sorted(cadena2):
#         print(f'Las dos cadenas "SI" son anagramas')
#     else:
#         print(f'Las dos cadenas "NO" son anagramas')

# es_anagrama('hola','ohal')

# # 18-Crea una función llamada calcular_mayor_diferencia que tome una lista de
# # números como parámetro y devuelva la mayor diferencia entre el numero mas
# # alto y el numero mas bajo en la lista.

# def calcular_mayor_diferencia(*args):
#     '''Calcula la diferencia del numero maximo y minimo'''
# #Numero maximo
#     numero_max = args[0]
#     for i in range(len(args)):
#         if args[i] > numero_max:
#             numero_max = args[i]
#     print(f'En la lista: {args} el numero maximo es "{numero_max}"')
# #Numero Minimo
#     numero_min = args[0]
#     for i in range(len(args)):
#         if args[i] < numero_min:
#             numero_min = args[i]
#     print(f'En la lista: {args} el numero minimo es "{numero_min}"')
# #Diferencia
#     diferencia = numero_max - numero_min
#     print(f'La diferencia de {numero_max} - {numero_min} = {diferencia} ')

# calcular_mayor_diferencia(2,3,10,3,9)

# # 19-Crea una función llamada es_bisiesto que tome un año como parámetro y
# # devuelva Bisiesto si el año es bisiesto, o No es Bisiesto en caso contrario. Un año
# # es bisiesto si es divisible por 4, pero no por 100, a menos que también sea
# # divisible por 400.

# def es_bisiesto(año):
#     bisiesto = 0
#     if año%400==0 or (año%4==0 and año%100!=0):
#         print(f'El año {año} es bisiesto')
#     else:
#         print(f'El año {año} no es bisiesto')

# es_bisiesto(2024)

