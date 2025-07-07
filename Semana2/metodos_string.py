nombre = input("Ingresa tú nombre completo: ")

#resultado = len(nombre) #Cuenta cantidad de caracteres
#resultado = nombre.find("M") #Busca la primera posicion del caracter a buscar
#resultado = nombre.rfind("O") #Busca la ultima posicion del caracter a buscar
#resultado = nombre.capitalize() #Primer caracter en mayuscula
#resultado = nombre.upper() #Todo en mayuscula
#resultado = nombre.lower() #Todo en minuscula
#resultado = nombre.isdigit() #Boleano si el string es todo de números
#resultado = nombre.count("o") #Cuenta las veces que sale algun caracter a buscar
resultado = nombre.replace("o", "X") #Reemplaza algún caracter por otro
print(resultado)