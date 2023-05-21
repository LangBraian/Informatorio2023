# 9- Escribe un programa que solicite al usuario dos números y
# luego imprima la suma, resta, multiplicacion y division
# de los dos números

numero1 = int(input("Escribe un número: "))
numero2 = int(input("Escribe otro número: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"De los numeros {numero1} y {numero2} se obtienen los siguientes resultados")
print(f"De la Suma {suma}, de la Resta {resta}, de la multiplicacion {multiplicacion} y de la Division {division}")
