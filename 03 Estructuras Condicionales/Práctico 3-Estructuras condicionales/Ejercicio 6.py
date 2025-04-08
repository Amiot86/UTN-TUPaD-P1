#Trabajo Práctico 3: Estructuras condicionales
#Alumna: Marisabel Viviana Aramayo

# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media 
# y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# Importo la libreria random.
# Importo mode, median, mean de statistics
import random
from statistics import mode, median, mean

# Uso estas variables dadas en la consigna
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
print(numeros_aleatorios) # agregue esto para ver los números de la lista

# Defino las variables moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Uso condicionales para imprimir los resultados de las estadisticas
if media > mediana and mediana > moda:
    print("La lista tiene sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("La lista tiene sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No ingresa a ningún caso") #agrego un caso porque veo que a veces no entra en ninguno de los casos anteriores


