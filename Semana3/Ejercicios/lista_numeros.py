#De la siguiente lista, con un bucle, itera todos sus valores y muestra una frase como "El valor del elemento es: 356".
#Quiero que omitas todos los valores 10.

#Además, quiero que rompas la ejecución del bucle cuando se encuentre el valor 356, pero se tienen que imprimir el resto de valores de la lista.

lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]

for x in lista_numeros:
    if x == 10 or x == 356:
        continue
    else:
        print(f"El valor del elemento es: {x}")