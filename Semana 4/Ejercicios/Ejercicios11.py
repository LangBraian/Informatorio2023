# 11-Crea una función llamada contar_vocales que tome una cadena de texto como
# parámetro y devuelva el número de vocales que contiene.

def contar_vocales(texto):
    contar=0
    for i in texto:
        if i == "a"or i=="e" or i=="i" or i=="o" or i=="u":
            contar+=1
    print(f'El texto: "{texto}" tiene "{contar}" vocales ')

contar_vocales('hola, como estas?')
