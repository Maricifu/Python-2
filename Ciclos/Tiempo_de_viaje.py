tiempo_total = 0

while True:
    try:
        tiempo_tramo = int(input("Duración del tramo: "))
    except ValueError:
        print("Por favor, ingrese un número entero.")
        continue

    if tiempo_tramo == 0:
        break

    tiempo_total += tiempo_tramo

horas_totales = tiempo_total // 60
minutos_totales = tiempo_total % 60

print(f"El tiempo total de viaje es: {horas_totales} horas y {minutos_totales} minutos.") 

