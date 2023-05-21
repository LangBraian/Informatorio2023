# 7-Escribe un programa que pida al usuario una palabra y determine si es un
# palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
# izquierda).

palabra = input('Ingrese una palabra: ')

palindromo = True
for i in range(len(palabra)):
    if palabra[i] != palabra[-i - 1]:
        palindromo = False
        break
if palindromo:
    print(f'La palabra {palabra} "Si" es un palindromo')
else:
    print(f'La palabra {palabra} "No" es un palindromo')
