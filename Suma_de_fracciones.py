# Solicitar al usuario que ingrese un entero de tres dígitos
numero = int(input("Ingrese un entero de tres dígitos: "))

# Verificar si el número tiene tres dígitos
if 100 <= numero <= 999:
    # Convertir el número a cadena, invertir los dígitos y luego volver a convertir a entero
    numero_invertido = int(str(numero)[::-1])

    # Mostrar el resultado
    print(f"Número invertido: {numero_invertido}")
else:
    print("Por favor, ingrese un entero de tres dígitos.")

