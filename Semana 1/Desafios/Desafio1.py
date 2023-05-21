# Desafio 1:
# Trabajas en una empresa X donde sus vendedores cobran comisiones del 6%
# de sus ventas totales y el departamento comercial te solicita que ayudes
# a los vendedores a calcular sus comisiones creando un programa que les
# pregunte su nombre y cuanto han vendido este mes.
# Tu programa le va a responder con una frase que incluya su nombre y el
# monto que le corresponde por las comisiones.

nombre = input("Ingrese su nombre: ")
venta = float(input("Ingrese el importe de sus ventas: "))
comision = venta * 0.06

print(f"Estimado {nombre} debido a que su volumen de ventas del mes fue {venta} su comision es de {comision}")
