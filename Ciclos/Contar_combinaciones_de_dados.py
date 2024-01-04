def contar_combinaciones(puntaje):
    combinaciones = 0

    # Bucle para los valores del primer dado
    for dado1 in range(1, 7):
        # Bucle para los valores del segundo dado
        for dado2 in range(1, 7):
            # Verificar si la suma es igual al puntaje dado
            if dado1 + dado2 == puntaje:
                combinaciones += 1

    return combinaciones

puntaje_ingresado = int(input("Ingrese el puntaje: "))

combinaciones_totales = contar_combinaciones(puntaje_ingresado)

print(f"Hay {combinaciones_totales} combinaciones para obtener {puntaje_ingresado}") 

