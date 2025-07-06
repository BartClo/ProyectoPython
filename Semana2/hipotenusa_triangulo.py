import math

print("Bienvenido a la calculadora de la hipotenusa de un triangulo!!")

a = float(input("Ingresa el valor del lado A: "))
b = float(input("Ingresa el valor del lado B: "))

c = math.sqrt(a**2 + b**2)

print(f"La hipotenusa del triangulo con lados {a} y {b} es {c}")