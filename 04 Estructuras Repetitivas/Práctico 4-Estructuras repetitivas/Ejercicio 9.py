# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cont = 0
suma = 0
media = 0
cant_numeros = 10
num = 0



while cont < cant_numeros:
    num = int(input("Ingrese un número entero: "))
    suma = suma + num
    cont = cont + 1
    if cont == cant_numeros:
        media = suma / cant_numeros
        print("La media de los valores es", media)


