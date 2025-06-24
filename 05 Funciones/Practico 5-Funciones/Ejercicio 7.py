# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros 
# y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

# Definición de funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)


# Programa principal
a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número (distinto de 0): "))

print(operaciones_basicas(a, b))
