# hacer un programa que pida 3 numero y determine cual es el mayor

num1 = int(input("Por favor digite el primer numero:"))
num2 = int(input("Por favor digite el segundo numero:"))
num3 = int(input("Por favor digite el tercer numero:"))

if num1 >= num2 and num1 >= num3:
  print(f"El numero {num1} es mayor que los demas")
elif num2 >= num1 and num2 >= num3:
  print(f"El numero {num2} es mayor que los demas")
elif num3 >= num1 and num3 >=num2:
  print(f"El numero {num3} es mayor que los demas")