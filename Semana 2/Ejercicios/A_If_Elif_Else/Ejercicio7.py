# 7-Escribir un programa que pida al usuario un carácter y muestre por pantalla si
# es una letra mayúscula, una letra minúscula, un número o un carácter especial.

caracter = input('Ingresa solo un caracter: ')
if caracter.islower():
    print('El caracter',caracter,'es Miniscula')
elif caracter.isupper():
    print('el caracter',caracter,'es Mayuscula')
elif caracter.isdigit():
    print('El caracter',caracter,'es un Nùmero')
else:
    print('El caracter',caracter,'Es un caràcter especial')