# 19-Crea una función llamada es_bisiesto que tome un año como parámetro y
# devuelva Bisiesto si el año es bisiesto, o No es Bisiesto en caso contrario. Un año
# es bisiesto si es divisible por 4, pero no por 100, a menos que también sea
# divisible por 400.

def es_bisiesto(año):
    bisiesto = 0
    if año%400==0 or (año%4==0 and año%100!=0):
        print(f'El año {año} es bisiesto')
    else:
        print(f'El año {año} no es bisiesto')

es_bisiesto(2024)
