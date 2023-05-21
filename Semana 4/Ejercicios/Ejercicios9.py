# 9-Crea una función llamada promedio que tome una lista de números como
# parámetro y devuelva el promedio de esos números.

def promedio(*args):
    suma = 0
    cantidad = len(args)
    for num in args:
        suma = suma + int(num)
        promedio = suma / cantidad
    print(f'El promedio de la lista {args} es de {promedio}')

promedio(2, 3, 4)
