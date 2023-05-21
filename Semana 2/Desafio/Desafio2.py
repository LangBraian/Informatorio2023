# Se te pide crear un programa que le pida al usuario que ingresar un texto
# cualquiera, por ejemplo, un artículo o una frase.

texto = input('Ingrese un texto: ')

# Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
# elección.

letra = input('Ingrese 3 letras separadas por un espacio Ej:a b c')

# 1- Cantidad de veces que aparece cada una de letras que eligió.
# Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un
# string

letras_separadas = letra.split()

# Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se
# encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
# minúscula.

texto = texto.lower()
letra = letra.lower()

cantidad_letra0 = texto.count(letra[0])
cantidad_letra1 = texto.count(letra[2])
cantidad_letra2 = texto.count(letra[4])

print(f"""1) La cantidad de letras que aparecen son:
        {letra[0]} = {cantidad_letra0}
        {letra[2]} = {cantidad_letra1}
        {letra[4]} = {cantidad_letra2}
        """)

# 2- Cuantas palabras hay en total en todo el texto.
# Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud.

lista_texto = texto.split()

print(f'2) El texto tiene en total "{len(lista_texto)}" palabras')

# 3- Cual es la primera letra y cuál es la última. (Indexación)

print(f'3) La primera letra del texto es "{texto[0]}"" y la ultima es "{texto[-1]}"')

# 4- Mostrar el texto en orden inverso.
print("4)")
print(f'  a) Las "letras" del texto en inversa son: {texto[::-1]}')
lista_texto.reverse()
print(f'  b) Las "palabras" del texto en inversa son: {lista_texto}')

# 5- Decir si la palabra "python" aparece en el texto.
# Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
# string para mostrar al usuario.

python = "python" in texto
diccionario = {True: "Si", False: "No"}

print(f'5) En el texto "{diccionario[python]}"" esta la palabra "python"')









