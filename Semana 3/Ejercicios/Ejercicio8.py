# 8-Escribe un programa que pida al usuario una cadena de texto y luego imprima
# el número de palabras que contiene.

texto = input('Ingresa una cadena de texto: ').split()
cantidad = len(texto)

print(f'El texto tiene {cantidad} palabras')