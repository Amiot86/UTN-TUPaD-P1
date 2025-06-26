# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y 
# devuelva su representación en binario como una cadena de texto.

# Definición de funciones
def decimal_bin(numero):
    if numero == 1:
        return "1"
    else:
        return decimal_bin(numero // 2) + str(numero % 2)

# Programa principal
numero = int(input("Ingrese número: "))
print(f"{numero} en binario es {decimal_bin(numero)}")
