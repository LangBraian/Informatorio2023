# 16-Crea una función llamada eliminar_duplicados que tome una lista como
# parámetro y devuelva una nueva lista sin duplicados, conservando el orden
# original.

def eliminar_duplicados(*args):
    conjunto = set(args)
    lista = list(conjunto)
    print(lista)

eliminar_duplicados(2,3,4,1,2,2,2,3,4,'braian','eduin','lang','eduin')
