print("-> Pizzería PF <-")

dinero = float(input("Ingrese el dinero disponible para pagar: "))

pizzas = {"Napolitana": 1400,
          "Pepperoni": 1100,
          "4 Quesos": 1350,
          "Margarita": 1600}
extras = {}
print(pizzas)
keys = pizzas.keys()
values = pizzas.values()
print(keys)
print(values)
print("Nuestro catalogo de pizzas son las siguientes:\nNapolitana -> $1400 \nPepperoni -> $1100 \n4 Quesos -> $1350\nMargarita -> $1600")
compra = input("Elija su pizza (Nombre completo e igual): ")

keys = pizzas.keys()
values = pizzas.values()
print(keys)
while compra not in pizzas.keys():
    print("No existe de esa pizza")
    compra = input("Elija su pizza (Nombre completo e igual): ")
else:
    while dinero in pizzas.values():
        
        if dinero < pizzas.values(compra):
            print("No tienes suficiente dinero")
        else:
            print(f"Has seleccionado {compra}")
            
x = input("Desea agregar extras a la pizza (Sí o No): ")

if x is "Sí":
    extras.append(input("Ingrese los ingredientes extras: "))
else:
    print(f"El total a pagar por la {pizzas} es ${pizzas.values(compra)}.\n El pago a sido realizado el vuelto es de ${pizzas.values(compra) - dinero }")
    
            




    


