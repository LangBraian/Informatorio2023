# 5-Escribe un programa que imprima la suma de todos los números pares del 1 al 100.

par = 0
for i in range(1,101):
    if i%2==0:
        par = par + i
print(f'La suma de todos los numeros pares es: {par}')