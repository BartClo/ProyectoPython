# Ejecuta un bloque de código por x veces

for x in range(1, 11):
    print(x)
    
    
for x in reversed(range(1, 11)):
    print(x)
print("Feliz año nuevo!!")

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)
    
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)
        
for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)