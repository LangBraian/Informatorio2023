# 6-Escribir un programa que pida al usuario un número entero y muestre por
# pantalla si es múltiplo de 2 y de 3 a la vez.

numero = int(input('Ingrese un nùmero entero: '))

if (numero%2 == 0) and (numero%3 == 0):
    print(f'El nùmero "{numero}" es multiplo de 2 y 3')
else:
    print(f'El nùmero "{numero}" NO es multiplo de 2 y 3')

# Video de youtube. https://www.youtube.com/watch?v=jOCh6ZpkE1k