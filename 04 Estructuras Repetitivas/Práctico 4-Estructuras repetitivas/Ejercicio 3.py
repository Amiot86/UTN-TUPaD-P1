# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

numero_uno = int(input("Ingrese un número entero: "))
numero_dos = int(input("Ingrese otro número entero: "))
sumatoria = 0


for cont in range(numero_uno+1,numero_dos):
    print(cont)
    sumatoria = sumatoria + cont

print("La sumatoria de los números es", sumatoria)