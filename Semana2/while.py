# Ejecuta código mientras WHILE alguna condicion sea Verdad

#nombre = input("Ingresa tu nombre: ")

#while nombre == "":
#    print("No ingresaste ningún nombre!!")
#    nombre = input("Ingresa tu nombre: ")
#print(f"Hola, {nombre}!!")


#edad = int(input("Ingresa tu edad: "))

#while edad < 0:
#    print("No puedes tener edad negativa")
#    edad = int(input("Ingresa tu edad: "))
#if edad >=18:
#    print("Eres mayor de edad")
#else:
#    print("Eres menor de edad")

comida = input("Ingresa la comida que te gusta (q para salir): ")

while not comida == "q":
    print(f"Te gusta comer {comida}")
    comida = input("Ingresa otra comida que te gusta (q para salir): ")
print("ADIOS")
