# 5-Crea una función llamada es_divisible que tome dos números enteros como
# parámetros y devuelva Es divisible si el primer número es divisible por el
# segundo número, o No es divisible en caso contrario.

def es_divisible(num1,num2):
    if num1%num2==0:
        print(f'El numero {num1} es divible del numero {num2}')
    else:
        print(f'El numero {num1} no es divible del numero {num2}')
    return es_divisible    
    
es_divisible(num1=6,num2=2)
