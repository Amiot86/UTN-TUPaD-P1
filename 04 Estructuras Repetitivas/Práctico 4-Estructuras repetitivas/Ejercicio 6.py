#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

cont = 100
while cont >= 0:
    if cont % 2 == 0:
        print (cont)
    cont = cont - 1