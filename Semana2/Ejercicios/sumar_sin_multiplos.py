#Usa un for para imprimir los números del 1 al 20, pero usa continue para saltar los múltiplos de 3.

for x in range(0, 21):
    if x % 3 == 0:
        continue
    else:
        print(x)
        