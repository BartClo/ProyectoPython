# Evaluan multiples condiciones (or, and, not)
#or = Al menos una condicion debe ser verdadera
#and = Ambas condiciones deben ser verdaderas
#not = Invierte la condición (not False, not True)

#temp = 36
#is_raining = False

#if temp > 35 or temp < 0 or is_raining:
 #   print("El evento al airelibre es cancelado")
#else:
 #   print("El evento aún está agendado")
    
temp = 29
is_sunny = True

if temp >= 28 and is_sunny:
    print("Hace calor afuera")
    print("Está soleado")
elif temp <= 0 and is_sunny:
    print("Hace frio afuera")
    print("Está soleado")
elif temp >= 28 and not is_sunny:
    print("Hace calor afuera")
    print("Está nublado")
