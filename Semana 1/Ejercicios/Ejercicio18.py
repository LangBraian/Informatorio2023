# 18-Crea un programa que pida al usuario su nombre, su edad y su ciudad de
# residencia, y lo muestre en pantalla Utilizando una sola línea de código.
# *Recuerda el print() del ejercicio anterior

datos = input('Ingresa tu nombre, edad y cuidad de residencia. Separados por la coma (,): ')
nombre, edad, ciudad = datos.split(',')
print(f'Hola {nombre} tu edad es de{edad} años y tu ciudad de residencia es{ciudad}')