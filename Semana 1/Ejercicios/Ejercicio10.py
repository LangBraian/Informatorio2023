# 10- Crea un programa que pida al usuario una cantidad en 
# dolares y la converita a euros.
# Supón que el tipo de cambio es de 0.84 euros por dolar

dolar = float(input("Ingresa la cantidad de dolares que deseas cambiar: "))
cambio = 0.84
euro = dolar * cambio

#En caso de que pidiera como imprimirlo en pantalla seria:

print(f"Si tenes {dolar} dolares al cambiarlos a euros obtendras {euro} euros")
