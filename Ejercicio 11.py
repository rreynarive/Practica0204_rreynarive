# Escribir un programa que pida al usuario una palabra
# y luego muestre por pantalla una a una las letras de
# la palabra introducida empezando por la última.

palabra = input("Introduzca una palabra\n")
len(palabra)
for letra in range(len(palabra)-1, -1, -1):
    print(palabra[letra])