# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
# #Ejemplo: si e usuario ingresa 547, el programa debe mostrar 745

n = int(input("Imgrese un número para invertir el orden de sus digitos: "))
numero = 0

while n != 0:
    numero = 10*numero+n % 10
    n //= 10

print(numero)    