# 15-Escribe un programa que pida al usuario una cadena de texto y determine
# cuántas veces aparece cada letra en la cadena.

texto = input('Ingrese un texto: ')
contador = []
for i in texto:
    contador[i] += 1

print(contador)

