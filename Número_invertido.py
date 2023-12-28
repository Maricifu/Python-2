
print ("ELija el programa de 3 dígitos o el de n dígitos")
programa= (input("3 digítos o n dígitos:"))

while programa== "3 dígitos":

    while True:
        numero = int(input("Ingrese un entero de tres dígitos: "))
        
        if 100 <= numero <= 999:
            break 
        else:
            print("Por favor, ingrese un entero de tres dígitos.")

    digito_cientos = numero // 100
    digito_decenas = (numero % 100) // 10
    digito_unidades = numero % 10

    numero_inverso = digito_unidades * 100 + digito_decenas * 10 + digito_cientos

    print(f"El número con los dígitos en orden inverso es: {numero_inverso}")

while programa== "n dígitos":

    while True:
        try:
            n = int(input("Ingrese un entero de cualquier cantidad de dígitos: "))
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    lista_digitos = [int(digito) for digito in str(n)]

    lista_digitos.reverse()

    numero_inverso = int(''.join(map(str, lista_digitos)))

    print(f"El número con los dígitos en orden inverso es: {numero_inverso}")

while (not programa==("3 dígitos") or programa==("n dígitos") ):
    print("Indique correctamente el programa")
    break
