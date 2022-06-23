# escribir comillas en una cadena
from traceback import print_tb


cadena = "Esto es una cadena con 'comillas' sencillas "
print(cadena)  # Esto esuna cadena con 'comillas' sencillas


# escribir comillas dobles en una cadena y hacer un salto de linea
cadena2 = "Esto es una cadena \nEstoy en otra \"linea\""
print(cadena2)
# Esto es una cadena
# Estoy en otra "linea"


# OPERADORES PARA CADENAS

# Operador de concantenacion
cadena3 = "Hola "
cadena4 = "mundo"
cadenas_unidas = cadena3 + cadena4
print(cadenas_unidas)  # Hola mundo

# Operador de repeticion
cadenas_repetidas = cadena3 * 4
print(cadenas_repetidas)  # Hola Hola Hola Hola
