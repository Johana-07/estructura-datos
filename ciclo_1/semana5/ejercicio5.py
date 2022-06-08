# creacion de archivos de texto

ruta = r"C:\Users\Majo\Desktop\REPOSITORIO GITHUB\estructura-datos\ciclo_1\semana5\archivo.txt"

# crear o escritura el archivo de txt
fichero = open(ruta, "w")

# Agregar informacio al final del archivo de txt
fichero = open(ruta, "a")

# solo lectura de un archivo txt
fichero = open(ruta, "r")


fichero.close()
