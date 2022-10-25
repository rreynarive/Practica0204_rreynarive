# Escribir un programa que pida al usuario un número entero
# y muestre por pantalla un triángulo rectángulo que tenga
# tantas líneas como el número introducido,
# como el triángulo de más abajo.

numero = int(input("Introduzca un numero impar\n"))
num = numero % 2

for fila in range(numero):
    for a in range(fila):
        if num != 0:
            print("{}".format(a), end=" ")
    if num != 0:
        print("{}".format(fila), end=" ")
    print(" ")