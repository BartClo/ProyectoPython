

menu = int(input("Ingresa la operación a realizar:\n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n 5. Salir \n"))

while menu in range(0, 6):
    if menu == 1:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        print(f"La suma de ambos números es {n1 + n2}")
        menu = int(input("Ingresa la operación a realizar:\n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n 5. Salir \n"))
    elif menu == 2:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        print(f"La resta de ambos números es {n1 - n2}")
        menu = int(input("Ingresa la operación a realizar:\n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n 5. Salir \n"))
    elif menu == 3:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))     
        print(f"La multiplicación de ambos números es {n1 * n2}")
        menu = int(input("Ingresa la operación a realizar:\n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n 5. Salir \n"))
    elif menu == 4:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        print(f"La división entre ambos números es {n1 / n2}")
        menu = int(input("Ingresa la operación a realizar:\n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n 5. Salir \n"))
    elif menu == 5:
        print("ADIOS!!")
        break
else:
    print("Operación no valida!!")
    menu = int(input("Ingresa la operación a realizar:\n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n 5. Salir \n"))    
        



