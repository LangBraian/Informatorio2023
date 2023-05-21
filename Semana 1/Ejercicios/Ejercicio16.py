# 16-Escribe un programa que solicite al usuario su peso y su altura, y luego calcule
# e imprima su índice de masa corporal (IMC).
# La fórmula para calcular el IMC es: IMC = peso / (altura ** 2).

peso = float(input('Ingresa tu peso: '))
altura = float(input('Ingresa tu altura: '))
imc = peso / (altura**2)

print(f'Debido a que tienes {peso} kg y mides {altura} cm, tu IMC es de {imc}')