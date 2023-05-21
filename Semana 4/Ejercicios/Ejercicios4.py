# 4-Crea una función llamada es_capicua que tome un número como parámetro y
# devuelva True si es capicúa (es decir, si se lee igual de izquierda a derecha que de
# derecha a izquierda) y False en caso contrario.

def es_capicua(numero):
    numero_str=str(numero)
    cantidad_digito=len(numero_str)

    if(cantidad_digito%2==0):
        vueltas=int(cantidad_digito/2)
        acumulador=0
        for i in range(vueltas):
            if(numero_str[i]==numero_str[cantidad_digito-i-1]):
                acumulador+=1
        
        if(acumulador==vueltas):
            print(f'El numero {numero} es capicua')
        else:
            print(f'El numero {numero} no es capicua')
    else:
        vueltas=int((cantidad_digito-1)/2)
        acumulador=0
        for i in range(vueltas):
            if(numero_str[i]==numero_str[cantidad_digito-i-1]):
                acumulador+=1
        
        if(acumulador==vueltas):
            print(f'El numero {numero} es capicua')
        else:
            print(f'El numero {numero} no es capicua')   

es_capicua(10101)
