principio = 0
tasa = 0
tiempo = 0

while principio <= 0:
    principio = float(input("Ingresa el costo inicial: "))
    if principio <= 0:
        print("No debe ser menor o igual a cero.")
while tasa <= 0:
    tasa = float(input("Ingresa la tasa: "))
    if tasa <= 0:
        print("No debe ser menor o igual a cero.")
while tiempo <=0:
    tiempo = float(input("Ingresa el tiempo en años: "))
    if tiempo <= 0:
        print("No debe ser menor o igual a cero.")
    
    
total = principio * pow(1 + tasa / 100, tiempo)

print(f"El balance luego de {tiempo} año/s: ${total: .2f}")