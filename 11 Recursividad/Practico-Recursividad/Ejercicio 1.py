# 1) Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números 
# enteros entre 1 y el número que indique el usuario

# Definición de funciones
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

# Programa principal
numero = int(input("Ingrese un número: "))
for i in range(1,numero+1):
    print(factorial(i))