# bloque de objeto que se puede ocupar más veces

#return: usado para terminar una función y enviar un resultado devuelta 


def happy_birthday(name, age):
    print(f"Happy Birthday to {name}!")
    print(f"You are {age} years old!")
    
    

happy_birthday("Bro", 20)
happy_birthday("Joe", 30)
happy_birthday("Steve", 25)


def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Marcelo", "Muñoz")
print(full_name)