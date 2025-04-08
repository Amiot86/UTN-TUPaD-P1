# Trabajo Práctico 3: Estructuras condicionales
# Alumna: Marisabel Viviana Aramayo

# 3) Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

# Defino la variable numero
numero = int(input("Ingrese un número par: "))

# Uso condicionales para analizar los restos de los numeros ingresados y definir si son pares.
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

