# hacer un programa que tenga dos listas y que a continuacion , cree las siguientes listas:
# A.lista de palabras que aparecen en las dos listas
# B.lista de palabras que aparecen en la primera lista , pero no en la segunda
# C.lista de palabras que aparecen en la segunda lista , pero no en la primera
# D.lista de palabras que aparecen en ambas listas

lista1 = [1, 2, 3, 4, 5, "lunes", "martes", "miercoles"]
lista2 = ["lunes", "martes", "miercoles",
          "jueves", "viernes", "sabado", "domingo"]
list1 = set(lista1)  # converti las listas en conjunto
print(type(list1))
list2 = set(lista2)  # converti las listas en conjunto
print(type(list2))

A = list(list1 | list2)
print(f"lista de palabras que aparecen en las dos listas: {A}")

B = list(list1 - list2)
print(
    f"lista de palabras que aparecen en la primera lista, pero no en la segunda: {B}")

C = list(list2 - list1)
print(
    f"lista de palabras que aparecen en la segunda lista, pero no en la primera: {C}")

D = list(list1 & list2)
print(f"lista de palabras que aparecen en ambas listas: {D}")
