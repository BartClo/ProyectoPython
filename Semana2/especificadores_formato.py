#Forma de insertar valores a un string

precio1 = 3.14159
precio2 =-987.65
precio3 = 12.34

print(f"Precio 1 es ${precio1:10}")
print(f"Precio 2 es ${precio2:.1f}")

print(f"Precio 3 es ${precio3:<10}") 
print(f"Precio 3 es ${precio3:>10}") 
print(f"Precio 3 es ${precio3:^10}") 
print(f"Precio 3 es ${precio3:+}") 
print(f"Precio 3 es ${precio3: }") 