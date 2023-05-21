# 9-Escribe un programa que pida al usuario un número y luego imprima la
# secuencia de Fibonacci correspondiente a ese número.

numero = int(input('Ingresa un numero: '))

for num in range(numero+1):
    numero+=num
    print(num)

# 0 = 0, 1
# 1 = 1, 1
# 2 = 

