def nombre_completo(nombre, apellido="Abad"):
    """generacion del nombre completo de la persona
    Parametros
        nombre (_type_): _description_
        apellido (str, optional): _description_. Defaults to "Abad".
    Retorna
        La unin de los dos parametros ingresados
    """
    completo = nombre + " " + apellido
    return completo


print(nombre_completo("Cesar", "Diaz"))  # Cesar Diaz
print(nombre_completo("Andrea", "Martinez"))  # Andrea Martinez
print(nombre_completo(apellido="Noriega", nombre="Paola"))  # Paola Noriega
print(nombre_completo("Cesar"))  # Cesar Abad
print(nombre_completo.__doc__)  # imprime la documentacion de la funcion


# funciones sin parametros
def saludar_al_mundo():
    return "Hola Mundo"


print(saludar_al_mundo())  # Hola Mundo


# funciones con  parametros
def saludar_alguien(quien):
    return "Hola "+str(quien)


print(saludar_alguien("Cesar"))  # Hola Cesar


# funciones con  parametro opcinal
def saludar_alguien_adicional(quien, adicional="!"):
    return "Hola "+str(quien)+str(adicional)


# llamar a la funcion con 1 parametro
print(saludar_alguien_adicional("Cesar"))  # Hola Cesar!
# llamar a la funcion con 2 parametros
print(saludar_alguien_adicional("Mundo", "*"))  # Hola Mundo*
# llamar a la funcion con las etiquetas de los parametros
print(saludar_alguien_adicional(adicional=":)",
                                quien="Andres"))  # Hola Andres:)


# retornar mas de 1 valor
def retornar_varios_valores():
    return "Cesar", "Diaz", 40, "Pereira"


valores = retornar_varios_valores()
nombre, apellido, edad, ciudad = valores
print(nombre, apellido, edad, ciudad, sep="\n")
"""
Cesar
Diaz
40
Pereira """
