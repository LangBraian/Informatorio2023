# 19-Escribe un programa que pida al usuario un número y luego imprima si ese
# número es un número perfecto o no. Un número perfecto es aquel que es igual a
# la suma de sus divisores propios (excluyendo el propio número).
# Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se
# puede dividir por 1, 2 y 3, y cuando sumas esos números, el resultado es 6

numero = int(input('Ingresa un numero: '))
factorial = 1

for num in range(1,numero+1):
    factorial = factorial * num
if numero == factorial:
    print(f'El numero {numero} "Si" es un numero Perfecto')
else:
    print(f'El numero {numero} "No" es un numero Perfecto')

.