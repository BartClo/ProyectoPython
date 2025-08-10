print("-> Pizzería PF <-")

dinero = float(input("Ingrese el dinero disponible para pagar: "))

pizzas = ["Napolitana","Pepperoni","4 Quesos"]
costo = [1200, 1000, 1350]
extras = []

print("Nuestro catalogo de pizzas son las siguientes:\nNapolitana -> $1200 \nPepperoni -> $1100 \n4 Quesos -> $1350")
compra = input("Elija su pizza (Nombre completo e igual): ")

while compra != pizzas:
    print("No existe de esa pizza")
    compra = input("Elija su pizza (Nombre completo e igual): ")
else:
    if pizzas > dinero:
        print("No tienes suficiente dinero")
    else:
        print(f"Has seleccionado {compra}")

x = input("Desea agregar extras a la pizza (Sí o No): ")

if x is "Yes":
    extras.append(input("Ingrese los ingredientes extras: "))
else:
    print(f"El total a pagar por la {pizzas} es ${costo}.\n El pago a sido realizado el vuelto es de ${dinero - costo}")
    


