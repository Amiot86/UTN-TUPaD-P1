# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro 
# y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.

# Definición de funciones
def segundos_a_horas(segundos):
    return segundos / 60


# Programa principal
segundos = int(input("Ingrese los segundos: "))
horas = segundos_a_horas(segundos)
print(f"Los segundos ingresados equivalen a {horas} horas")
