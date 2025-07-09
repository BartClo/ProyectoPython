# cuota = ((ValorNominal * TasaCupon) / 1 - 1/(1+TasaCupon)**T

valorNominal = float(input("Ingresa el Valor Nominal: "))
tasaCupon = float(input("Ingresa la Tasa Cupón: "))
tiempo = float(input("Ingresa los n° de cuotas: "))

cuota = (valorNominal * tasaCupon) / 1 - (1 / (pow((1+tasaCupon), tiempo)))

print(f"El dividendo mensual a pagar es de {cuota: .2f}")