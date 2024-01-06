def dia_siguiente(fecha):
    anno, mes, dia = fecha
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
        dias_mes[1] = 29  # Año bisiesto

    if dia < dias_mes[mes - 1]:
        return (anno, mes, dia + 1)
    elif mes < 12:
        return (anno, mes + 1, 1)
    else:
        return (anno + 1, 1, 1)

def dias_entre(f1, f2):
    fecha1 = f1
    fecha2 = f2

    if fecha1 > fecha2:
        fecha1, fecha2 = fecha2, fecha1

    dias = 0
    while fecha1 < fecha2:
        fecha1 = dia_siguiente(fecha1)
        dias += 1

    return dias

# Programa principal
nacimiento = (
    int(input("Ingrese su fecha de nacimiento.\nDia: ")),
    int(input("Mes: ")),
    int(input("Anno: "))
)

hoy = (
    int(input("\nIngrese la fecha de hoy.\nDia: ")),
    int(input("Mes: ")),
    int(input("Anno: "))
)

edad = dias_entre(nacimiento, hoy)
print(f"\nUsted tiene {edad} días de edad.")
