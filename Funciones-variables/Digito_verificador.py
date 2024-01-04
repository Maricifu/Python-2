def calcular_digito_verificador(rol_sin_digito):
    
    rol_invertido = rol_sin_digito[::-1]

    suma = 0
    secuencia = [2, 3, 4, 5, 6, 7]
    
    for i, digito in enumerate(rol_invertido):
        multiplicador = secuencia[i % len(secuencia)]
        suma += int(digito) * multiplicador

    resto = suma % 11
    digito_verificador = 11 - resto

    if digito_verificador == 10:
        digito_verificador = 'k'
    elif digito_verificador == 11:
        digito_verificador = 0

    return digito_verificador

rol_sin_digito = input("Ingrese el rol sin guión ni dígito verificador: ")

digito_verificador = calcular_digito_verificador(rol_sin_digito)
print(f"El dígito verificador es: {digito_verificador}")

rol_completo = f"{rol_sin_digito}-{digito_verificador}"
print(f"El rol completo con dígito verificador es: {rol_completo}")
 