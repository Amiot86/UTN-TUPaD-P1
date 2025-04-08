# Trabajo Práctico 3: Estructuras condicionales
# Alumna: Marisabel Viviana Aramayo

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra
# en otoño, invierno, primavera o verano.

# Importo datetime de la libreria
from datetime import date, datetime

# Creo la variable MESES_A_NUMEROS para buscar equivalencia entre el mes en letras y el mes en números
MESES_A_NUMEROS = {'Enero': 1,
        'Febrero': 2,
        'Marzo': 3,
        'Abril': 4,
        'Mayo': 5,
        'Junio': 6,
        'Julio': 7,
        'Agosto': 8,
        'Septiembre': 9,
        'Octubre': 10,
        'Noviembre': 11,
        'Diciembre': 12}

# Pedi al usuario que ingrese los datos
# Uso capitalize para que el usuario pueda ingresar mayusculas o minusculas
hemisferio = (input("Ingrese en que hemisferio se encuentra: ")).capitalize()
mes = (input("Ingrese el mes actual: ")).capitalize()
mes = MESES_A_NUMEROS[mes]
dia = int(input("Ingrese el día actual: "))

# Defino variables para las estaciones del año. 
# La estación cinco suple un error que me daba porque el año no comienza en diciembre.
ESTACION_UNO = [date(2025, 12, 21), date(2025, 12, 31)]
ESTACION_CINCO = [date(2025, 1, 1), date(2025, 3, 20)]
ESTACION_DOS = [date(2025, 3, 21), date(2025, 6, 20)]
ESTACION_TRES = [date(2025, 6, 21), date(2025, 9, 20)]
ESTACION_CUATRO =[date(2025, 9, 21), date(2025, 12, 20)]

# Uso el condicional para determinar la estación de acuerdo a la fecha
if (ESTACION_UNO[0] <= date(2025,mes,dia) and ESTACION_UNO[1] >= date(2025,mes,dia)) and hemisferio == "Norte":
    print("Usted se encuentra en invierno")
elif(ESTACION_CINCO[0] <= date(2025,mes,dia) and ESTACION_CINCO[1] >= date(2025,mes,dia)) and hemisferio == "Norte":
    print("Usted se encuentra en invierno")
elif(ESTACION_UNO[0] <= date(2025,mes,dia) and ESTACION_UNO[1] >= date(2025,mes,dia)) and hemisferio == "Sur":
    print("Usted se encuentra en verano")
elif(ESTACION_CINCO[0] <= date(2025,mes,dia) and ESTACION_CINCO[1] >= date(2025,mes,dia)) and hemisferio == "Sur":
    print("Usted se encuentra en verano")
elif(ESTACION_DOS[0] <= date(2025,mes,dia) and ESTACION_DOS[1] >= date(2025,mes,dia)) and hemisferio == "Norte":
    print("Usted se encuentra en primavera")
elif(ESTACION_DOS[0] <= date(2025,mes,dia) and ESTACION_DOS[1] >= date(2025,mes,dia)) and hemisferio == "Sur":
    print("Usted se encuentra en otoño")
elif(ESTACION_TRES[0] <= date(2025,mes,dia) and ESTACION_TRES[1] >= date(2025,mes,dia)) and hemisferio == "Norte":
    print("Usted se encuentra en verano")
elif(ESTACION_TRES[0] <= date(2025,mes,dia) and ESTACION_TRES[1] >= date(2025,mes,dia)) and hemisferio == "Sur":
    print("Usted se encuentra en invierno")
elif(ESTACION_CUATRO[0] <= date(2025,mes,dia) and ESTACION_CUATRO[1] >= date(2025,mes,dia)) and hemisferio == "Norte":
    print("Usted se encuentra en otoño")
elif(ESTACION_CUATRO[0] <= date(2025,mes,dia) and ESTACION_CUATRO[1] >= date(2025,mes,dia)) and hemisferio == "Sur":
    print("Usted se encuentra en primavera")
