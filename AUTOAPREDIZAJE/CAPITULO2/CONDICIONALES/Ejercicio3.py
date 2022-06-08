# hacer un programa que pida un caracter e indique si es una vocal o no

letra = str(input("Por favor ingrese un caracter: ").lower())

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
  print(f"El caracter {letra} es una vocal")
else:
  print(f"El caracter {letra} no es una vocal")