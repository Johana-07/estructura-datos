def nombre_completo(nombre, apellido="Abad"):
    """generacion del nombre completo de la persona
    Parametros
        nombre (_type_): _description_
        apellido (str, optional): _description_. Defaults to "Abad".
    Retorna
        La unin de los dos arametros ingresados
    """
    completo = nombre + " " + apellido
    return completo


print(nombre_completo("Cesar", "Diaz"))  # Cesar Diaz
print(nombre_completo("Andrea", "Martinez"))  # Andrea Martinez
print(nombre_completo(apellido="Noriega", nombre="Paola"))  # Paola Noriega
print(nombre_completo("Cesar"))  # Cesar Abad
print(nombre_completo.__doc__)  # imprime la documentacion de la funcion
