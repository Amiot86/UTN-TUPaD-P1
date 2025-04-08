#Trabajo Práctico 3: Estructuras condicionales
#Alumna: Marisabel Viviana Aramayo

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías 
# pertenece:
#  ● Niño/a: menor de 12 años.
#  ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#  ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#  ● Adulto/a: mayor o igual que 30 años.

# Declaro las variables adolescente y adulto
adolescente = 12
adulto = 30

# Uso condicionales para definir las edades de las personas
edad = int(input("Ingrese su edad: "))
if edad >= adolescente and edad < 18:
    print("Adolescente")
elif edad <= adolescente:
    print("Es niño/a")
elif edad >= 18 and edad < adulto:
    print("Adulto/a joven")
else:
    print("Adulto/a")