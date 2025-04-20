# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

from random import *
aleatorio = randint(0,9)

numero = int(input("Adivine el número que estoy pensando. Ingrese un número aleatorio entre 0 y 9: "))

while numero != aleatorio:
    numero = int(input("Incorrecto, ingrese otro número del 0 al 9: "))
    
print ("Correcto!")
    
