# escriba un programa donde tenga una lista y que a continuacion ,elimine los elementos repetidos
# por ultimo mostrar la lista


# 1.forma de solucionar
lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista)
print(lista.sort())  # ordeno los elementos ascendentemente
print(lista.count(2))  # indica q el 2 esta 2 veces
print(lista.remove(2))  # se elimina el numero 2
print(lista)
print(lista.count(4))  # indica q el 4 esta 2 veces
print(lista.remove(4))  # se elimina el numero 2
print(lista)
print(lista.count(6))  # indica q el 6 esta 2 veces
print(lista.remove(6))  # se elimina el numero 2
print(lista)
print(lista.count(8))  # indica q el 8 esta 2 veces
print(lista.remove(8))  # se elimina el numero 2
print(lista)
print(lista.count(10))  # indica q el 10 esta 2 veces
print(lista.remove(10))  # se elimina el numero 2
print(lista)


# 2.forma de solucionar
lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
conjunto = set(lista)  # se convierte la lista en un conjunto
lista = list(conjunto)  # se convierte el conjunto en una lista
print(conjunto)  # se imprime la listasin duplicados


# 3.forma de solucionar
lista = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = list(set(lista))
print(lista)
