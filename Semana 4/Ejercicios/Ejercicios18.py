# 18-Crea una función llamada calcular_mayor_diferencia que tome una lista de
# números como parámetro y devuelva la mayor diferencia entre el numero mas
# alto y el numero mas bajo en la lista.

def calcular_mayor_diferencia(*args):
    '''Calcula la diferencia del numero maximo y minimo'''
#Numero maximo
    numero_max = args[0]
    for i in range(len(args)):
        if args[i] > numero_max:
            numero_max = args[i]
    print(f'En la lista: {args} el numero maximo es "{numero_max}"')
#Numero Minimo
    numero_min = args[0]
    for i in range(len(args)):
        if args[i] < numero_min:
            numero_min = args[i]
    print(f'En la lista: {args} el numero minimo es "{numero_min}"')
#Diferencia
    diferencia = numero_max - numero_min
    print(f'La diferencia de {numero_max} - {numero_min} = {diferencia} ')

calcular_mayor_diferencia(2,3,10,3,9)