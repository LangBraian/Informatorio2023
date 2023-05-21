# 14-Crea una función llamada encontrar_maximo que tome una lista de números
# como parámetro y devuelva el número máximo de la lista.

def encontrar_maximo(*args):
    numero_max = args[0]
    for i in range(len(args)):
        if args[i] > numero_max:
            numero_max = args[i]
    print(f'En la lista: {args} el numero maximo es "{numero_max}"')
 #Extra en que posicion se encuentra:   
    print(f'El numero {numero_max} se encuentra en la posicion {args.index(numero_max)}')
encontrar_maximo(2,3,10,3,1)