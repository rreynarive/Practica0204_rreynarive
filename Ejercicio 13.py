# Escribir un programa que muestre el eco de todo lo que el usuario
# introduzca hasta que el
# usuario escriba “salir” que terminará.

while True:
    mensaje = input("Introduzca su mensaje:\n")
    if mensaje == "salir":
        break
    else:
        print(mensaje)
