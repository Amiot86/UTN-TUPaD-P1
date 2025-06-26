# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

# Definición de funciones
def calc_potencia(num, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return num
    else:
        return num * calc_potencia(num, exponente - 1)


# Programa principal
numero = int(input("Indique un número: "))
exp = int(input("Indique un exponente: "))
print(f"{numero} elevado a la {exp} es {calc_potencia(numero, exp)}")

