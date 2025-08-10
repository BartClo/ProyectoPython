# *args = el * te permite colocar cualquier cantidad de non-key arguments
# **kwargs = el ** te permite colocar cualqer cantidad de keyword-arguments

def add(a, b):
    return a + b

print(add(1, 2))


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
    
print(add(1,2,3))



def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.", 
              city="Detroit", 
              state="MI", 
              zip="54321")