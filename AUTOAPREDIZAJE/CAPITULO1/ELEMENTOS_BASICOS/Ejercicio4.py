#Hacer un programa para ingresar el radio de un circulo y se reporte su area y la longitud de la 
# circunferencia
#r = radio
#area = pi * r**2
# circunferencialongitud = 2 * pi * r

import math  # importar modulo mach y dentro de ese esta el valor de pi

radio = float(input("Por favor digite el radio del circulo:"))

area = math.pi * radio**2  
longitud = 2* math.pi * radio

print(f"El area es:{area:.2f}") # .2f se coloca para cortar el valor de los decimales en el resultado y q solo salgan 2 decimales
print(f"La longitud de la circunferencia es:{longitud:.2f}")# .2f se coloca para cortar el valor de los decimales en el resultado
