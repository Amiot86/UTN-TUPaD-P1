# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.
numero = int(input("Ingrese un número entero positivo: "))

sumatoria = 0
cont = 0

for cont in range (0, numero+1):
    sumatoria = cont + sumatoria

print(sumatoria)
