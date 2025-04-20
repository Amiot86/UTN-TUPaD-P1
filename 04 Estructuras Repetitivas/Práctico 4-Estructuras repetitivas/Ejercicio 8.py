# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
cont = 0
pares = 0
impares = 0
positivos = 0
negativos = 0

while cont < 100:
    num = int(input("Ingrese un número entero: "))    
    if num % 2 == 0:
        pares = pares + 1
    elif num % 2 != 0:
        impares = impares + 1
    if num < 0:
        negativos = negativos + 1
    elif num > 0:
        positivos = positivos + 1
    cont = cont + 1

print("La cantidad de números ingresados es:",cont)
print("La cantida de números pares es:",pares)
print("La cantidad de números impares es:",impares)
print("La cantidad de números positivos es:",positivos)
print("La cantidad de números negativos es:",negativos)




