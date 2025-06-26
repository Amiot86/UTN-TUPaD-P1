# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y 
# devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.

# Definición de funciones
def suma_digitos(n):
    if n // 10 == 0:
        return n
    else:
        return n % 10 + suma_digitos(n//10)

# Programa principal
numero = int(input("Ingrese un número entero: "))
print(f"La suma de sus digitos es {suma_digitos(numero)}")
