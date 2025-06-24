# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius 
# y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# Definición de funciones
def celsius_a_fahrenheit(celsius):
    fahrenheit = celsius * (9 / 5) + 32
    return fahrenheit


# Programa principal
celsius = float(input("Ingrese la temperatura en celcius: "))
print (f"La temperatura en fahrenheit es {celsius_a_fahrenheit(celsius)} ")