import time

print("-> Pizzería PF <-")

dinero = float(input("Ingrese el dinero disponible para pagar: "))

pizzas = {"Napolitana": 1400,
          "Pepperoni": 1100,
          "4 Quesos": 1350,
          "Margarita": 1600}
extras = []

print("Nuestro catalogo de pizzas son las siguientes:\nNapolitana -> $1400 \nPepperoni -> $1100 \n4 Quesos -> $1350\nMargarita -> $1600")
compra = input("Elija su pizza (Nombre completo e igual): ")


while compra not in pizzas.keys():
    print("No existe de esa pizza")
    compra = input("Elija su pizza (Nombre completo e igual): ")
else:
    precio_pizza = pizzas[compra]
    if dinero >= precio_pizza:
        print(f"Has seleccionado {compra}")
        time.sleep(2)
        x = input("Desea agregar extras a la pizza (Sí o No): ")
        if x == "Sí":
            while True:
                extras.append(input("Ingrese los ingredientes extras (Cada extra cuesta $300) presiona q para terminar: "))
                if extras.append is "q":
                    break
                else:
                    for extra in extras:
                        precio_pizza += 300
                        if precio_pizza > dinero:
                            print("No tienes dinero suficiente para agregar ingredientes")
                        else:
                            print(f"El total a pagar por la {compra} con extra {extras} es ${precio_pizza}.\n El pago a sido realizado el vuelto es de ${dinero - precio_pizza}")
        else:
            print(f"El total a pagar por la {compra} es ${precio_pizza}.\n El pago a sido realizado el vuelto es de ${dinero - precio_pizza}")
    else:
        print("No tienes suficiente dinero")
        












