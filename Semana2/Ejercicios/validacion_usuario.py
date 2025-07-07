#validacion input usuario
# nombre de usuario no debe ser mayor a los 12 caracteres
# no debe contener espacios ni digitos

nombre = input("Ingresa tu nombre: ")

if len(nombre) > 12:
    print("El nombre no debe tener más de 12 caracteres")
elif not nombre.find(" ") == -1:
    print("El nombre no debe contener espacios")
elif not nombre.isalpha():
    print("El nombre no debe contener números")
else:
    print(f"Bienvenido {nombre}!!")