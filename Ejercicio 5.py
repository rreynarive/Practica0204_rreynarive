# Los alumnos de Hogwarts se han dividido en dos casas,
# Gryffindor y Slytherin, de acuerdo al sexo y el nombre.
# Gryffindor está formado por las mujeres con un nombre
# anterior a la M y los hombres con un nombre posterior a
# la N y Slytheryn por el resto. Escribir un programa que
# pregunte al usuario su nombre y sexo, y muestre por
# pantalla el grupo que le corresponde.

nombre = input("¿Cual es su nombre?\n")
sexo = input("Introduzca su sexo (M o H):\n")

if sexo == "M":
    if nombre[0].upper() < "M":
        print("Eres de Gryffindor")
    else:
        print("Eres de Slytheryn")
else:
    if nombre[0].upper() > "N":
        print("Eres de Gryffindor")
    else:
        print("Eres de Slytheryn")


