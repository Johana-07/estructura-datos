# una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto 
# debera pagar finalmente por su compra

precio = float(input("Digite por favor el precio de su compra: "))

descuento = precio * 0.15
precio_final = precio - descuento


print(f"El precio final de la compra es de $ {precio_final:.2f}")
