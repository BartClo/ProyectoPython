import random

x = random.randint(1, 100)

n = int(input("Ingresa un número: "))

print(x)
while n != x:
    print("No es el número")
    n = int(input("Ingresa un número: "))
    
else:
    print("GG WP!!")


#El programa elige un número aleatorio entre 1 y 100. El usuario debe adivinarlo.

#Si el número es muy bajo, le dice "Muy bajo".

#Si es muy alto, "Muy alto".

#Termina con break si lo adivina.