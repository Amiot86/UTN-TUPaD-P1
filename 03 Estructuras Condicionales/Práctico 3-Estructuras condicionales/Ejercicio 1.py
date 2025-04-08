#Trabajo Práctico 3: Estructuras condicionales
#Alumna: Marisabel Viviana Aramayo

# 1) Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# Defino la variable EDAD_MINIMA a 18 años
EDAD_MINIMA = 18

# Defino la variable edad que ingresa el usuario.
edad = int(input("Ingrese su edad: "))

# Uso condicionales para determinar si el número anteriormente ingresado indica si es mayor de edad o no.
if edad >= EDAD_MINIMA:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

