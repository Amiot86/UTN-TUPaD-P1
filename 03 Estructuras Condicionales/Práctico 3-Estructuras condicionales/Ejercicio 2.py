# Trabajo Práctico 3: Estructuras condicionales
# Alumna: Marisabel Viviana Aramayo

# 2) Escribir un programa que solicite su nota al usuario. 
# Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
# en caso contrario deberá mostrar el mensaje “Desaprobado”.

# Defino la variable NOTA_APROBADO como seis
NOTA_APROBADO = 6

# Defino la variable nota que ingresa el usuario
nota = float(input("Ingrese su nota: "))

# Uso condicinales para ver si la nota ingresada esta aprobada o desaprobada.
if nota >= NOTA_APROBADO:
    print("Aprobado")
else:
    print("Desaprobado")