# 8-Escribir un programa que pida al usuario una cadena de caracteres y muestre
# por pantalla si contiene la letra "a".

cadena = input('Insera una cadena de caracteres: ')

if "a" in cadena:
    print(f'La cadena ingresada "{cadena}" posee el caracter "a"')
else:
    print(f'La cadena ingresada "{cadena}" NO posee el caracter "a"')
