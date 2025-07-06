print("Bienvenido al carrito de compras!!")

producto = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))  #float porque el precio puede ser decimal
cantidad = int(input("Cantidad del producto: ")) #int porque no existen mitades de algún producto solo enteros

total = precio * cantidad

print(f"Usted lleva {cantidad} {producto} a ${precio} cada unidad, por lo que total por pagar es de ${total}")