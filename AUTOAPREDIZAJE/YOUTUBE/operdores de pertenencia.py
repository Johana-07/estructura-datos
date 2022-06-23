# OPERADORES DE PERTENENCIA =>  Evaluan si un objeto se encuentra dentro de otro
"""
in => se encuentra en
not in => no se encuentra en
"""
cadena = " AcademiaCoder"
print("Aca" in cadena)  # True
print("hola" in cadena)  # False
print("z" in cadena)  # False
print("Co" in cadena)  # True


print("Aca" not in cadena)  # False
print("hola" not in cadena)  # True
print("z" not in cadena)  # True
print("Co" not in cadena)  # False


# OPERADORES DE IDENTIDAD =>  Nos permiten comprobar si un objeto es igual o no a otro objeto
"""
is => es
is not => no es
"""

a = 10
b = 10

print(a is b)  # True
print(a is not b)  # False

print(type(a) is int)   # True
print(a is not float)  # True
