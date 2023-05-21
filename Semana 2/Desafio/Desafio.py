# Desafío 2: Analizador de textos
# Requisitos técnicos:
# -Métodos y propiedades de string.
# -Indexar estructuras de datos.
# -Todos los tipos de datos.

# Se te pide crear un programa que le pida al usuario que ingresar un texto
# cualquiera, por ejemplo, un artículo o una frase.

texto = input('Ingrese un texto: ')

# Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
# elección.

letra = input('Ingrese 3 letras: ')

# Nuestro código va a procesar esa información para realizar los análisis
# necesarios para devolverle al usuario la siguiente información:
# 1- Cantidad de veces que aparece cada una de letras que eligió.
# Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un
# string
# Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se
# encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
# minúscula.

texto = texto.lower()
letra = letra.lower()

texto.count(letra[0])
texto.count(letra[1])
texto.count(letra[2])

print()
print()
print(f'El texto es:"{texto}"')
print(f'Las letras son: "{letra}"')
print()
print(f"""1) La cantidad de veces que aparece cada la letra en el texto es:
    {letra[0]} = {texto.count(letra[0])}
    {letra[1]} = {texto.count(letra[1])}
    {letra[2]} = {texto.count(letra[2])}
     """)

# 2- Cuantas palabras hay en total en todo el texto.
# Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud.

len(texto)

print(f'2) El texto contiene {len(texto)} letras')
print()

# 3- Cual es la primera letra y cuál es la última. (Indexación)

print(f'3) La primera letra del texto es "{texto[0]}" y la ultima letra es "{texto[-1]}"')
print()

# 4- Mostrar el texto en orden inverso.

print(f'4) El Texto a la inversa es: "{texto[::-1]}"')
print()
# 5- Decir si la palabra "python" aparece en el texto.
# Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
# string para mostrar al usuario.

if "python" in texto:
    print(f'5) La palabra python "SI" aparece en el texto')
else:
    print(f'5) La palabra python "NO" aparece en el texto')


buscar = "python" in texto

dic = {True:"si",False:"no"}
print(dic)
print(f'La palabra "python" {dic[buscar]} esta en el texto')

