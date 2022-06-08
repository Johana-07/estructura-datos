#Contruir un programa que simule el funcionamiento de una calculadora que pueda realizar cuatro operaciones
# artimeticas basicas (suma , resta , multiplicacion y division) .El usuario debe especificar la 
# operacion con el primer caracter del nombre de la operacion
'''
S ,s - suma 
R ,r - resta
P ,p , M , m - Multiplicacion
D ,d - Division'''
calcular = input("Por favor indique que operacion desea realizar: ").upper()

num1 = float(input("Por favor ingrese el primer numero: "))
num2 = float(input("Por favor ingrese el segundo numero: "))



if calcular == "S":
  suma = num1 + num2 
  print(f"\nla suma de esos dos numeros es :{suma} ")
elif calcular == "R":
  resta = num1 - num2 
  print(f"\nla resta de esos dos numeros es :{resta} ")
elif calcular == "P" or calcular =="M":
  multiplicacion = num1 * num2 
  print(f"\nla multiplicacion de esos dos numeros es :{multiplicacion:.2f} ")
elif calcular == "D":
  division = num1 / num2 
  print(f"\nla division de esos dos numeros es :{division:.2f} ")
else:
  print(f"\nla operacion no es valida")

print("Finalizo el programa")