# 12-Escribe un programa que pida al usuario una lista de números separados por
# comas y calcule su promedio.

numeros = input('Ingresa una lista de numero separados con la "," Ej: 2,3,4,5: ').split(",")
suma = 0
cantidad = len(numeros)
for num in numeros:
    suma = suma + int(num)
    promedio = suma / cantidad
print(f'El promedio de la lista {numeros} es de {promedio}')
