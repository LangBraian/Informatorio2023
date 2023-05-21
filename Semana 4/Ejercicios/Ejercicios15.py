# 15-Crea una función llamada contar_palabras que tome una cadena de texto
# como parámetro y devuelva el número de palabras que contiene. Se considera
# que las palabras están separadas por espacios.

def contar_palabras(cadena):
    lista = cadena.split()
    cantidad = len(lista)
    print(f'La cadena: "{cadena}" tiene {cantidad} palabras')

contar_palabras('Hola como estas?')