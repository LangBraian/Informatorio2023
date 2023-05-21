# 8-Crea una función llamada es_palindromo que tome una cadena de texto como
# parámetro y devuelva es palindromo si es un palíndromo (es decir, si se lee igual
# de izquierda a derecha que de derecha a izquierda) y no es palindromo en caso
# contrario.

def es_palindromo(palabra):
    palindromo = True
    for i in range(len(palabra)):
        if palabra[i] != palabra[-i - 1]:
            palindromo = False
            break
    if palindromo:
        print(f'La palabra {palabra} "Si" es un palindromo')
    else:
        print(f'La palabra {palabra} "No" es un palindromo')

es_palindromo('menem')

