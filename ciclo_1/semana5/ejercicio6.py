# leer o escribir en un archivo de txt

datos = ["Linea 1", "Linea 2", "Linea 3", "Linea 4", "Linea 5"]


""" for lie in datos:
    fichero.write(lie)
    fichero.write("\n")
fichero.close()


for i in range(1001):
    for lie in datos:
        variable = str(i) + ", " + lie
        fichero.write(variable)
    fichero.write("\n")

fichero.close()


ruta = r"C:\Users\Majo\Desktop\REPOSITORIO GITHUB\estructura-datos\ciclo_1\semana5\archivo_p.txt"
fichero = open(ruta, "w")

for lie in datos:
    print(lie, file=fichero)
fichero.close()


ruta = r"C:\Users\Majo\Desktop\REPOSITORIO GITHUB\estructura-datos\ciclo_1\semana5\archivo_list_comp.txt"
fichero = open(ruta,"w")

fichero.writelines("%s\n" % s for s in datos)
fichero.close()
"""
