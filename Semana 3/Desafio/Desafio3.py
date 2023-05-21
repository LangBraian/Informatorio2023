'''
Desafío 3: Adivina el número
Requisitos técnicos:
- Operadores lógicos.
- Operadores de comparación.
- Control de flujo - Condicionales.
- Control de Flujo - Repetitivas.
Vamos a crear un juego completamente funcional.
Para ello el programa debe:
1) Pedir al usuario que ingrese su nombre.
2) Informarle que el número a adivinar está entre 1 y 100, y que tiene 8 intentos para adivinarlo.
3) Generar aleatoriamente un número entero entre 1 y 100.
tip 1: importar de la biblioteca random la función randint (Tu profe te explicará en clase cómo hacerlo)
4) Informarle al usuario cuántos intentos le quedan y solicitarle que ingrese un número.
El "número" ingresado por el usuario puede:
 a) No ser un número entero, en éste caso avisarle que no es un número entero el que ingresó.
tip 2: con el método isdigit() puedes saber si es posible convertir a entero
 b) Ser menor al que tiene que adivinar, en éste caso informarle que el número a adivinar es mayor.
 c) Ser mayor al que tiene que adivinar, en éste caso informarle que el número a adivinar es menor.
 d) Igual al que tiene que adivinar, en éste caso informarle que ha ganado y decirle en cuál intento
lo adivinó.
9) Si el usuario no ingresa un número entero no debes descontarle un intento, en los demás casos si
debes descontarle un intento.
10) En cada intento debes informarle al usuario los intentos que le quedan disponibles y solicitarle que
ingrese otro número.
11) Si el usuario no acierta en los 8 intentos, debes informarle que se agotaron los intentos y cuál era el
número que tenía que adivinar.
'''
#1)
nombre = input('Ingrese un nombre: ')
#2)
print(f'''Hola {nombre} Tenes que adivinar un número con solo una pista 
        "Está entre 1 y 100". 
Pero tenes 8 intentos para adivinarlo.''')
#3)
import random
numero_aleatorio = random.randrange(1,100)

#4)
intento = 0

while intento < 8:
    numero = input('Ingresa el numero que consideras como correcto: ')
    if numero.isdigit() == False:
        print(f'''Recorda que solo se pueden ingresar numeros enteros. Todavia te quedan "{8 - intento}"''')
    elif int(numero) > numero_aleatorio:
        intento += 1
        print(f'El numero ingresado es Mayor. Pero te quedan {8 - intento} intentos.')
    elif int(numero) < numero_aleatorio:
        intento += 1
        print(f'El numero ingresado es Menor. Pero te quedan {8 - intento} intentos.')
    elif int(numero) == numero_aleatorio:
        intento += 1
        break
if int(numero) == numero_aleatorio:
    print(f'¡Perfecto! "{nombre}" Lograste adivinar el numero en el intento nº {intento}')
else:
    print(f'''"{nombre}"" Has agotado la cantidad maxima de 8 intentos, 
    el numero que estuviste cerca de adiviar era: {numero_aleatorio}''')
print('¿Quieres volver a intentarlo?')
    