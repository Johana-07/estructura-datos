# hacer un programa que pida 2 numero y se de cuenta cual de ellos es par o si ambos lo son 

num1 = int(input("Digite por favor el primer numero entero: "))
num2 = int(input("Digite por favor el segundo numero entero: "))

""" if num1  % 2 == 0:  # se esta dividiendo el numero 1 en dos y sacando en residuo y q sea igual a cero 
  print("El primer numero es par")
else:
  print("El primer numero es impar")

if num2  % 2 == 0:
  print("El segundo numero es par")
else:
  print("El segundo numero es impar") """
  
if num1 % 2 == 0 and num2 % 2 == 0: # si num1 y num2 son pares 
    print("Ambos numeros son pares")
elif num1 % 2 == 0 and num2 % 2 != 0: #si el num1 es par y el num2 no es par, estamos seguros q num1 es par
  print(f"El  {num1} es par")
elif num1 % 2 != 0 and num2 % 2 == 0:#si el num1 no es par y el num2 es par, estamos seguros de num2 es par
  print(f"El  {num2} es impar")
else: # si nada de lo anterior se cumple 
  print("Ambos numeros son impares")