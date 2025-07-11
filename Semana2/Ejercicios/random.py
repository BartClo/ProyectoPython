import random

x = random.randint(1, 100)

n = int(input("Ingresa un número: "))

print(x)
while n != x:
    print("No es el número")
    n = int(input("Ingresa un número: "))
    
else:
    print("GG WP!!")


