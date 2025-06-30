'''una tienda desea calcular el total de una compra de tres productos se deben ingresar los precios de cada uno y mostrar el total a pagar
 Si compra un producto cobrar el 100%
 Si compra dos productos el 70&
 Si compra tres productps el 65%'''

# declaramos las variables y pedimos ingresar datos por teclado
producto_1 = float(input("ingrese el valor del primer producto: "))
producto_2 = float(input("ingrese el valor del segundo producto: "))
producto_3 = float(input("ingrese el valor del tercer producto: "))

# declaramos una variable para calcular el valor total de la compra
total = producto_1 + producto_2 + producto_3
#total *= 0.65

# declarando una variable para el descuento

descuento = 0.65
 
total_a_pagar = total * descuento

# mostramos el total por consola
#print(f"el total a pagar de su compra es: ${total}")

print(f"su compra ha sido de tres producto debe pagar: ${total_a_pagar}")

