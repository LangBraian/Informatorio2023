# 6 - Crea un programa que pida al usuario el radio de un círculo y
# calcule su área. La fórmula A = pi * r^2. Luego, muestra en
# pantalla el resultado. Supongamos que pi = 3.1316

pi = 3.1316
r = float(input("Escribe el un numero del radio: "))
area = pi * (r * r)
print(f"el valor del area del circulo es {area}")