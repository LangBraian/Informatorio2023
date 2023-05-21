# # 1-Escribir un programa que pida al usuario su edad y muestre por pantalla si es
# # mayor de edad (18 años o más) o no.

# edad = int(input('Ingrese su edad: '))

# if edad >= 18:
#     print('Usted es mayor de edad')
# else:
#     print('Usted es menor de edad')

# # 2-Escribir un programa que pida al usuario un número entero y muestre por
# # pantalla si es positivo, negativo o cero.

# numero = int(input('Ingrese un numero entero: '))

# if numero > 0:
#     print(f'El nùmero {numero} es "Positivo"')
# elif numero < 0:
#     print(f'El nùmero {numero} es "Negativo"')
# else:
#     print(f'El nùmero {numero} es "0"')

# # 3-Escribir un programa que pida al usuario dos números y muestre por pantalla
# # cuál de ellos es mayor.

# numero1 = input('Ingresa un numero: ')
# numero2 = input('Ingrese otro numero: ')

# if numero1 > numero2:
#     print(f'Entre los numeros {numero1} y {numero2} el mayor es "{numero1}"')
# else:
#     print(f'Entre los numeros {numero1} y {numero2} el mayor es "{numero2}"')

# # 4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
# # pantalla si está aprobado (5 o más) o no.

# nota = int(input('Ingrese su nota (Solo es valido del 0 al 10): '))

# if nota < 5 and nota >= 0:
#     print(f'Su nota es {nota} por lo que "Desaprobo" el examen')
# elif nota >= 5 and nota <= 10:
#     print(f'Su nota es {nota} por lo que "Aprobo" el examen')
# else:
#     print('Ingrese una nota con un valor del "0 al 10"')

# # 5-Escribir un programa que pida al usuario un número entero y muestre por
# # pantalla si es par o impar.

# numero = int(input('Ingrese un numero entero: '))

# if numero%2:
#     print(f'El nùmero {numero} es "InPar"')
# else:
#     print(f'El nùmero {numero} es "Par"')

# # Video en youtube (https://www.youtube.com/watch?v=CUMw8zjXj7o)

# # 6-Escribir un programa que pida al usuario un número entero y muestre por
# # pantalla si es múltiplo de 2 y de 3 a la vez.

# numero = int(input('Ingrese un nùmero entero: '))

# if (numero%2 == 0) and (numero%3 == 0):
#     print(f'El nùmero "{numero}" es multiplo de 2 y 3')
# else:
#     print(f'El nùmero "{numero}" NO es multiplo de 2 y 3')