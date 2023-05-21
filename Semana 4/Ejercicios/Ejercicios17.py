# 17-Crea una función llamada es_anagrama que tome dos cadenas de texto como
# parámetros y devuelva True si son anagramas (es decir, si tienen las mismas
# letras pero en distinto orden), o False en caso contrario.

def es_anagrama(cadena1,cadena2):
    if sorted(cadena1) == sorted(cadena2):
        print(f'Las dos cadenas "SI" son anagramas')
    else:
        print(f'Las dos cadenas "NO" son anagramas')

es_anagrama('hola','ohal')