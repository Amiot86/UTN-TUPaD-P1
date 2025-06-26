# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero)
#  y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

# Definición de funciones
def contar_digito (numero,digito):
    if numero // 10 == 0:
        if numero == digito:
            return 1
        else:
            return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

# Programa principal
numero = int(input("Ingrese un entero positivo: "))
digito = int(input("Ingrese un digito del 0 a 9: "))
print(f"El digito {digito} aparece {contar_digito(numero,digito)} veces en {numero}")
