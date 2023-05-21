# # 1-Escribe un programa que solicite al usuario su nombre
# # y lo imprima en la pantalla.
# nombre = input("Escribe tu primer nombre: ")
# print(nombre)

# # 2- Escribe un programa que solicite al usuario su nombre
# # y luego imprima un mensaje de bienvenida.

# nombre = input("Escribe tu primer nombre: ")
# print(F"Te damos la bienvenida {nombre}")

# # 3- Crea un programa que pida al usuario su edad y
# # lo imprima en pantalla.

# edad = input("Escribe tu edad: ")
# print(f"Tu edad actual es de {edad} años")

# # 4- Crea un programa que calcule la suma de dos números y
# # lo imprima en pantalla.

# numero1 = 5
# numero2 = 6
# suma = numero1 + numero2
# print(f"La suma de los {numero1} y {numero2} da como resultado {suma}")

# # 5- Crea un programa que pida al usuario dos números enteros y 
# # muestre en pantalla su cociente y su resto.

# numero1 = int(input("Escribe un número: "))
# numero2 = int(input("Escribe otro número que sea menor al anterior: "))
# cociente = int(numero1 / numero2)
# resto = int(numero1 - (cociente * numero2))

# #En caso que solicite imprimir en pantalla seria;
# print(f"De la divicion que surge entre {numero1} y {numero2} se obtiene el cociente: {cociente} y queda como resto: {resto}")

# # 6 - Crea un programa que pida al usuario el radio de un círculo y
# # calcule su área. La fórmula A = pi * r^2. Luego, muestra en
# # pantalla el resultado. Supongamos que pi = 3.1316

# pi = 3.1316
# r = float(input("Escribe el un numero del radio: "))
# area = pi * (r * r)
# print(f"el valor del area del circulo es {area}")

# # 7- Escrib(e un programa que calcule el área de un triángulo
# # a partir de la base y la altura dadas.

# base = float(input("Escribre la base del triangulo: "))
# altura = float(input("Ahora escribe la altura del triangulo: "))
# area = (base * altura) / 2

# # en caso que solicite como se ve en pantalla seria:

# print(f"El area del triangulo segun la base {base} y la altura {altura} su valor es de {area}")

# # 8- Crea un programa que pida al usuario el radio de un círculo
# #  y muestre su diámetro, su circunferencia y su área.
# # Supón que pi es aproximadamente 3.14159.

# pi = 3.14159
# radio = float(input("Ingresa el valor del Radio: "))
# diametro = radio * 2
# circunferencia = pi * diametro
# area = pi * (radio **2)

# print(f"Este circulo tiene un diametro de {diametro}, su circunferencia es {circunferencia} y su area es {area}")

# # 9- Escribe un programa que solicite al usuario dos números y
# # luego imprima la suma, resta, multiplicacion y division
# # de los dos números

# numero1 = int(input("Escribe un número: "))
# numero2 = int(input("Escribe otro número: "))
# suma = numero1 + numero2
# resta = numero1 - numero2
# multiplicacion = numero1 * numero2
# division = numero1 / numero2

# print(f"De los numeros {numero1} y {numero2} se obtienen los siguientes resultados")
# print(f"De la Suma {suma}, de la Resta {resta}, de la multiplicacion {multiplicacion} y de la Division {division}")

# # 10- Crea un programa que pida al usuario una cantidad en 
# # dolares y la converita a euros.
# # Supón que el tipo de cambio es de 0.84 euros por dolar

# dolar = float(input("Ingresa la cantidad de dolares que deseas cambiar: "))
# cambio = 0.84
# euro = dolar * cambio

# #En caso de que pidiera como imprimirlo en pantalla seria:

# print(f"Si tenes {dolar} dolares al cambiarlos a euros obtendras {euro} euros")

# # 11- Crea un programa que pida al usuario una palabra y
# # muestre en pantalla cuántas letras tiene.
# # Pss psssss toma... .len()

# palabra = input("Ingresa una palabra: ")

# print(f'la palabra "{palabra}" tiene "{len(palabra)}" letras')

# # 12-Escribe un programa que solicite al usuario su fecha de nacimiento en formato
# # dd/mm/aaaa y luego imprima su edad en años.
# # Utiliza la función .split()

# fecha_de_nacimiento = input("Escribe tu fecha de nacimiento con el formato dd/mm/aaaa: ")

# dia, mes, anio = fecha_de_nacimiento.split("/")

# edad = 2023 - int(anio)

# print(f'Tienes {edad} años')

# #Se puede mejorar el codigo utilizando un IF para el mes.

# # 13-Escribe un programa que solicite al usuario su nombre y su edad, y luego
# # imprima un mensaje que indique cuántos años tendrá el usuario en 10 años más.

# nombre = input("Ingresa tu nombre: ")
# edad = int(input("Ingresa tu edad: "))
# nueva_edad = edad + 10

# print(f'{nombre} tu edad en 10 años sera de {nueva_edad} años ')

# 14-Escribe un programa que solicite al usuario un número entero y luego
# imprima el doble y el triple de ese número.

# numero = int(input('Ingresa un numero entero: '))
# doble = numero*2
# triple = numero*3

# print(f'El numero ingresado es {numero}, el doble es {doble} y el triple es {triple}')

# # 15-Escribe un programa que solicite al usuario una temperatura en grados
# # Celsius y luego imprima la temperatura equivalente en grados Fahrenheit.
# # La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 1.8) + 32.

# celsius = float(input('Ingresa un grado de temperatura: '))

# fahrenheit = (celsius * 1.8) + 32

# print(f'La temperatura ingresada es {celsius} grados celsius es equivalente a {fahrenheit} grados fahrenheit')

# # 16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
# # e imprima su índice de masa corporal (IMC).
# # La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).

# peso = float(input('Ingresa tu peso: '))
# altura = float(input('Ingresa tu altura: '))
# imc = peso / (altura**2)

# print(f'Debido a que tienes {peso} kg y mides {altura} cm, tu IMC es de {imc}')

# # 17-Escribe un programa que solicite al usuario dos palabras y luego las imprima
# # en orden inverso.
# # Por ejemplo, si el usuario ingresa "hola" y "mundo", el programa debe imprimir
# # "mundo hola".
# # Importante!!! Utiliza un solo print() 😈.

# palabra1 = input('Ingresa una palabra: ')
# palabra2 = input('Ingresa otra palabra: ')

# print(f'Las palabras ingresadas alteradas el orden son "{palabra2} {palabra1}"')

# # 18-Crea un programa que pida al usuario su nombre, su edad y su ciudad de
# # residencia, y lo muestre en pantalla Utilizando una sola línea de código.
# # *Recuerda el print() del ejercicio anterior

# datos = input('Ingresa tu nombre, edad y cuidad de residencia. Separados por la coma (,): ')
# nombre, edad, ciudad = datos.split(',')
# print(f'Hola {nombre} tu edad es de{edad} años y tu ciudad de residencia es{ciudad}')

# # 19-Escribe un programa que solicite al usuario un número decimal y luego
# # imprima la parte entera y decimal por separado.

# numero = input('Ingresa un numero decimal separado con la coma (,): ')
# entero, decimal = numero.split(',')

# print(f'El numero ingresado es "{numero}" del cual la parte entera es "{entero}" y la parte decimal "{decimal}"')
