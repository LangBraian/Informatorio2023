# 13-Crea una función llamada calcular_descuento que tome dos parámetros:
# precio y porcentaje_descuento. La función debe calcular y devolver el precio
# después de aplicar el descuento.

def calcular_descuento(precio=None,descuento=None):
    porcentaje = precio - (precio * (descuento/100))
    print(f'''El articulo cuesta ${precio} y tiene un {descuento}% de descuento
por lo que te quedaria en ${porcentaje} finales''')

calcular_descuento(99,25)