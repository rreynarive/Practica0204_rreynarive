# Escribir un programa en el que se pregunte al
# usuario por una frase y una letra, y muestre por
# pantalla el número de veces que aparece la letra en la frase.

palabra = input("Introduzca una palabra\n")
letra = input("Introduzca una letra\n")

print("La letra {} aparece {} veces ".format(letra, palabra.count(letra)))
