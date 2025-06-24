# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro
#  y imprima la tabla de multiplicar de ese número del 1 al 10. 
# Pedir al usuario el número y llamar a la función.


# Definir funciones
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} * {i} = {numero * i}")

# Programa principal
numero = int(input(f"Ingrese un número: "))
tabla_multiplicar(numero)
