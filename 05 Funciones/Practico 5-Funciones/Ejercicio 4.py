# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro 
# y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math
# Definir funciones
def calcular_area_circulo(radio):
    return math.pi * math.sqrt(radio)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Programa principal
radio = int(input("Ingrese el radio del circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El circulo tiene un area {area} y un perimetro {perimetro}")