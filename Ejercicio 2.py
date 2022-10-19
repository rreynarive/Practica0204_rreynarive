#Escribir un programa que pida al usuario dos números
#y muestre por pantalla su división.
#Si el divisor es cero el programa debe mostrar un error.

divisor = float(input("Seleccione un numero divisor: "))
dividendo = float(input("Seleccione un numero dividendo: "))

if divisor == 0:
    print("¡¡¡ERROR!!!")
else:
    print("La division es", dividendo/divisor)