def invertir_digitos(n):
    numero_invertido = int(str(n)[::-1])
    return numero_invertido

def es_palindromo(n):
    return n == invertir_digitos(n)

numero = int(input("Ingrese n: "))

if es_palindromo(numero):
    print("Es palíndromo")
else:
    print("No es palíndromo") 
