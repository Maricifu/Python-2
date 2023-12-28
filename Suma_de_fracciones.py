potencia = 1
fraccion = 0.5
suma_fracciones = 0

print("Potencia  Fraccion  Suma")

while fraccion > 0.000001:
    
    print(f"{potencia}\t{fraccion}\t{suma_fracciones + fraccion}")

    suma_fracciones += fraccion

    potencia += 1
    fraccion /= 2

print("La fracción decimal es menor o igual a 0.000001.")
