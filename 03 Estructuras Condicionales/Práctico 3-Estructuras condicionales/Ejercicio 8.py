# Trabajo Práctico 3: Estructuras condicionales
# Alumna: Marisabel Viviana Aramayo

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario 
# e imprimir el resultado por pantalla.
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# Declaro las variables nombre y numero que fueron ingresadas por el usuario
nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese el número 1, 2 o 3: "))

# Uso condicional para devolver el nombre con el formato correspondiente a la opción que selecciono el usuario
if numero == 1:
    print(f"{nombre.upper()}")
elif numero == 2:
    print(f"{nombre.lower()}")
elif numero == 3:
    print(f"{nombre.capitalize()}")
    
