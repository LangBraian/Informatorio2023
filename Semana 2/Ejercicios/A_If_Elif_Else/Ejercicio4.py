# 4-Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por
# pantalla si está aprobado (5 o más) o no.

nota = int(input('Ingrese su nota (Solo es valido del 0 al 10): '))

if nota < 5 and nota >= 0:
    print(f'Su nota es {nota} por lo que "Desaprobo" el examen')
elif nota >= 5 and nota <= 10:
    print(f'Su nota es {nota} por lo que "Aprobo" el examen')
else:
    print('Ingrese una nota con un valor del "0 al 10"')