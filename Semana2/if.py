#if = Hace algo solo IF alguna condicion es Verdadera. ELSE De lo contrario hace otra cosa

edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
elif edad < 0:
    print("No existes")
elif edad >= 100:
    print("Eres muy viejo")
else:
    print("No eres mayor de edad")