# Escribir un programa que pregunte al usuario su edad
# y muestre por pantalla todos los años que ha cumplido
# (desde 1 hasta su edad).

edad = int(input("Introduzca su edad:\n"))
for i in range(edad):
    print(i+1, end=" años\n")



