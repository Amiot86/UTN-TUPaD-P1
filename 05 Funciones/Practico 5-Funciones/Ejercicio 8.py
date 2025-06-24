# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos 
# y la altura en metros, y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# Definicion de funciones
def calcular_imc(peso, altura):
    return peso / (altura * altura)

# Programa principal
peso = float(input("Ingrese el peso en kg: "))
altura = float(input("Ingrese la altura en metros: "))
print(f"El IMC es {calcular_imc(peso, altura)}")