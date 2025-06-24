# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros 
# y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

# Definicion de funciones
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
a = float(input("Ingrese un número: "))
b = float(input("Ingrese un segundo número: "))
c = float(input("Ingrese un tercer número: "))
print (f"El promedio es {calcular_promedio(a, b, c)}")

