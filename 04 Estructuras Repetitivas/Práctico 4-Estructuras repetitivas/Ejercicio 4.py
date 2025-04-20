# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

CORTE = 0

numero = 1
sumatoria = 0

while numero != CORTE:
    numero = int(input("Ingrese un número entero (0 para cortar): "))
    sumatoria = sumatoria + numero

print("La sumatoria de los números es", sumatoria)


