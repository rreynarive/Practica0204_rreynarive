# Escribir un programa que pida al usuario un número entero
# y muestre por pantalla un triángulo rectángulo que tenga
# tantas líneas como el número introducido,
# como el triángulo de más abajo.

numero = int(input("Introduzca un numero impar\n"))

for fila in range(1, numero+1, 2):
    for a in range(fila, 0, -2):
        print(a, end=" ")

    print(" ")
