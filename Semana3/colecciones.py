#colecciones = Una variable que se usa para almacenar multiples valores
# Listas = [] ordenada y cambiable. Acepta duplicados
# Set = {} sin ordenar e inmutable, se puede quitar o eliminar algo. No acepta duplicados
# Tupla = () ordenada e incambiable. Acepta duplicados. Rapida

fruits = ["apple", "orange", "banana"]

#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))

#print(fruits[1])
#fruits[1] = "pineapple"
#fruits.append("pineapple")
#fruits.insert(0, "pineapple")
#fruits.sort()
#fruits.reverse()
print(fruits.index("apple"))



for fruit in fruits:
    print(fruit)