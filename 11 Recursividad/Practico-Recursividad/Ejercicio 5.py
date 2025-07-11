# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

# Definición de funciones
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Programa principal
palabra = input("Ingrese una palabra sin espacios ni tildes: ")
if es_palindromo(palabra):
    print("Es palindromo")
else:
    print("No es palindromo")