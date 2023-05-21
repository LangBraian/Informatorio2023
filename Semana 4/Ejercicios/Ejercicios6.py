# 6-Crea una función llamada es_par que tome un número como parámetro y
# devuelva Es par si el numero cumple con dichas condiciones y en caso contrario
# devuelva Es impar o No es par.

def es_par(numero):
    if numero%2==0:
        print(f'El numero {numero} es PAR')
    else:
        print(f'El numero {numero} es IMPAR')

es_par(2)