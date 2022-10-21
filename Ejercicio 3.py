# Escribir un programa que pida al usuario un número entero
# y muestre por pantalla si es par o impar.

entero = int(input("Escriba un numero entero:\n"))
resto = entero % 2
if resto == 0:
    print("El numero es par")
else:
    print("El numero es impar")