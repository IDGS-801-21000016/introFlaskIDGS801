
from io import open


# archivo = open("archivo.txt", "a")
# archivo.write("\nHola, soy un texto guardado desde Python")
# archivo.close()


archivo = open("archivo.txt", "r")
# # texto = archivo.read()
# archivo.seek(3)
# texto = archivo.read()
print(archivo.readlines())
lista = archivo.readlines()
#quitar el salto de linea
lista = [i.rstrip() for i in lista]
print(lista)

archivo.close()
