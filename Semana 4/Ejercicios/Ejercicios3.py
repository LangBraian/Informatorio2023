# 3-Crea una función llamada invertir_cadena que tome una cadena de texto como
# parámetro y devuelva la cadena invertida.


def invertir_cadena(cadena):
    '''Esta funcion invierte una cadena de caracteres'''
    texto = ''
    for letra in range(len(cadena) -1,-1,-1):
        texto = texto + cadena[letra]
    return texto

'''Texto que ingresa el usuario'''
frase = input('Ingresa una frase: ')

'''Se aplica la funcion para invertir el texto'''
frase_invertida = invertir_cadena(frase)

'''Muestra el texto'''
print('Texto original:',frase)
print('Texto invertido:',frase_invertida)
