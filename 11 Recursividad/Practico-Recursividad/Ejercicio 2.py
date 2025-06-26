# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# Definición de funciones
def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion-2) + fibonacci(posicion-1)
    
# Programa principal
pos = int(input("Ingrese posicion: "))
for i in range(pos + 1):
    print(fibonacci(i))

