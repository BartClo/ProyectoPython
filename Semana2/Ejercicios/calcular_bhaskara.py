import math

print("Bienvenido a la calculadora de bhaskara!!")

a = float(input("Ingresa el término a: "))
b = float(input("Ingresa el término b: "))
c = float(input("Ingresa el término c: "))

x = (b**2)-(4*a*c)
if x <= 0:
    print("NT (b**2)-(4*a*c) es < 0")
elif x > 0:
    x1 = (- b + math.sqrt(x)) / (2*a)
    x2 = (- b - math.sqrt(x)) / (2*a)
    print(f"Los resultados son x1 = {x1} y x2 = {x2}")
else:
    print("NT x2")
