def Reversed_rol (rol):
    lista_digitos = [int(digito) for digito in str(rol)]
    lista_digitos.reverse()
    numero_inverso = int(''.join(map(str, lista_digitos)))
    return numero_inverso


while True:
    try:
        rol= str(input("Ingrese el rol UTFSM: "))
        break
    except ValueError:
        print("Ingrese correctamente el rol UTFSM: ")

    



