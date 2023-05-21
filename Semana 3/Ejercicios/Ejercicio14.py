# 14-Escribe un programa que pida al usuario un número y luego imprima un
# triángulo de números como el siguiente:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

numero = int(input('Ingresa un numero: '))
suma=0
for num in range(numero):
    suma += 1
    for cantidad in range(1,num+2):
        
        print(suma, end="")
    print()
