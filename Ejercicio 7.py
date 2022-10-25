# Escribir un programa que pida al usuario un número entero
# y muestre por pantalla un triángulo rectángulo como el de más abajo,
# de altura el número introducido.

numero = int(input("Introduzca un numero\n"))

for fila in range(numero+1):
    for a in range(fila):
        print("*", end=" ")
    print(" ")