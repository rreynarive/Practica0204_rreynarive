# Escribir un programa que muestre por
# pantalla la tabla de multiplicar del 1 al 10.


for fila in range(0, 100, 10):
    for i in range(10+1):
        print("10 x", i, "=", fila, end="\n")
print(" ")