#for x in range(3):
#    for i in range(1,10):
#        print(i, end="")
#    print()



rows = int(input("Ingresa el # de filas: "))
columns = int(input("Ingresa el # de columnas: "))
symbol = input("Ingresa un simbolo para usar: ")

for x in range(rows):
    for i in range(columns):
        print(symbol, end="")
    print()
