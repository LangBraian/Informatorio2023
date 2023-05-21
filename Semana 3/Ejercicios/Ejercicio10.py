# 10-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# la misma cadena pero con todas las vocales en mayúscula.

texto = input('Ingrese un texto: ')
texto_nuevo = ''
for letra in texto:
    if letra== "a"or letra=="e"or letra=="i"or letra=="o"or letra=="u":
        texto_nuevo += letra.upper()
    else:
        texto_nuevo += letra
print(texto_nuevo)

