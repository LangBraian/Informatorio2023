# 5- Crea un programa que pida al usuario dos números enteros y 
# muestre en pantalla su cociente y su resto.

numero1 = int(input("Escribe un número: "))
numero2 = int(input("Escribe otro número que sea menor al anterior: "))
cociente = int(numero1 / numero2)
resto = int(numero1 - (cociente * numero2))

#En caso que solicite imprimir en pantalla seria;
print(f"De la divicion que surge entre {numero1} y {numero2} se obtiene el cociente: {cociente} y queda como resto: {resto}")
