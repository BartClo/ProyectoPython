print("Bienvenido al convertidor de altura!!")

altura = float(input("Ingresa tu altura: "))
unidad = input("Metros o Pies(ft) (M o P): ")

if unidad == "M":
    altura = altura * 3.28084
    unidad = "Pies (ft)"
    print(f"Tu altura es: {round(altura, 3)} {unidad}")
elif unidad == "P":
    altura = altura * 0.3048
    unidad = "Metros"
    print(f"Tu altura es: {round(altura, 3)} {unidad}")
else:
    print(f"{unidad} no valida")
    