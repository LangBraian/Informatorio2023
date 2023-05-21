# 12-Crea una función llamada convertir_temperatura que tome una temperatura
# en grados Celsius y la convierta a grados Fahrenheit. La fórmula de conversión
# es: Fahrenheit = (Celsius * 9/5) + 32.

def convertir_temperatura(temperatura):
    f = (temperatura * 9/5) + 32
    print(f'''La temperatura de: 
{temperatura}º Celsius = {f}º Fahrenheit''')

convertir_temperatura(30)
