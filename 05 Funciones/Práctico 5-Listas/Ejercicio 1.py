# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista_range = list(range(1,101))

for i in range(len(lista_range)):
    if lista_range[i] % 4 ==0:
        print (lista_range[i])
