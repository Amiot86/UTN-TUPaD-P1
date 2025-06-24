# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) 
# que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
#  Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Definicion de funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
edad = input("Ingrese edad: ")
residencia = input("Ingrese residencia: ")
informacion_personal(nombre, apellido, edad, residencia)
