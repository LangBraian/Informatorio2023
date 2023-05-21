# 16-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con cada palabra al revés.

texto = input('Ingrese una cadena de texto: ')
lista = texto.split()

for i in lista:
    print(i[::-1], end=" ")


