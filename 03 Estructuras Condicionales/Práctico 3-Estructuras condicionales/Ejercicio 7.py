# Trabajo Práctico 3: Estructuras condicionales
# Alumna: Marisabel Viviana Aramayo

# 7) Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante 
# por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# Declaro las variables fop (significa Frase o Palabra) y vocales.
fop = input("Ingrese una frase o palabra: ")
vocales = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

# Uso condicional para encontrar si la última letra es vocal o no e imprimir un mensaje de acuerdo a eso.
if fop[len(fop) - 1] in vocales:
    print(f"{fop}!")
else:
    print(f"{fop}")

