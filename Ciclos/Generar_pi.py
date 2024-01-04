import math

def estimar_pi(n):
    suma = 0
    for k in range(n):
        termino = ((-1) ** k) / (2 * k + 1)
        suma += termino

    estimacion_pi = 4 * suma
    return estimacion_pi

n = int(input("Ingrese el número de términos para la estimación de π: "))

pi_estimado = estimar_pi(n)

print(f"La estimación de π con {n} términos es: {pi_estimado}")
print(f"El valor real de π es: {math.pi}")  


