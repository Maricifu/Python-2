n = int(input("Cuantos dias? "))

mayor_alza = 0
precio_anterior = None

for dia in range(1, n + 1):
    precio = float(input(f"Dia {dia}: "))

    if precio_anterior is not None:
        alza = precio - precio_anterior

        if alza > mayor_alza:
            mayor_alza = alza

    precio_anterior = precio

if mayor_alza > 0:
    print(f"La mayor alza fue de {mayor_alza:.2f} pesos")
else:
    print("No hubo alzas")
    