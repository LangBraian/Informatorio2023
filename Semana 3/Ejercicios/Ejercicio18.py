# 18-Escribe un programa que pida al usuario un número y luego imprima un
# triángulo de números como el siguiente:
# 1
# 2 3
# 4 5 6
# 7 8 9 10

numero = int(input('Ingresa un numero: '))
suma=0
for num in range(numero):
    
    for cantidad in range(1,num+2):
        suma += 1
        print(suma, end=" ")
    print()