operacion = input("Ingresa la operación (+ - * /): ")
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))

if operacion == "+":
    print(f"La suma de ambos números es {n1 + n2}")
elif operacion == "-":
    print(f"La resta de ambos números es {n1 - n2}")
elif operacion == "*":
    print(f"La multiplicación de ambos números es {n1 * n2}")
elif operacion == "/":
    print(f"La división de ambos números es {n1 / n2} ")
else:
    print(f"{operacion} no es valida")