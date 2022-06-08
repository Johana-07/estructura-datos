# hacer un programa que simule un cajero automatico con un saldo inicial de $1000 y tendra el siguiente menu
# de opciones

#  1 : ingrese dinero en la cuenta 
# 2 : Retire dinero de la cuenta 
# 3 : Mostrar dinero disponible 
# 4 : Salir  

saldo = 1000 

print("\t.:MENU:.")
print("1 = ingrese dinero en la cuenta")
print("2 = Retire dinero de la cuenta") 
print("3 = Mostrar dinero disponible")
print("4 = Salir")
opcion = int(input("Digite una opcion de menu: "))

print()

if opcion == 1:
  extra = float(input("Cuanto dinero desea entregar : "))
  saldo += extra
  print(f"Dinero en la cuenta {saldo}")
elif opcion == 2:
  retiro = float(input("Cuanto dinero desea retirar: "))
  if retiro>saldo:
    print("No tiene cantidad de dinero")
  else:
    saldo -= retiro
    print(f"Dinero en la cuenta {saldo} ")
elif opcion == 3:
  print(f"Su saldo es : {saldo}")
elif opcion == 4:
  print("Gracias por utilizar su cajero automatico")
else:
  print("Se equivoco de opcion de menu")