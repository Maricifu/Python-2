import math

def desviacion_estandar(valores):
    
    promedio = sum(valores) / len(valores)

    suma_cuadrados_diferencias = sum((x - promedio) ** 2 for x in valores)

    varianza = suma_cuadrados_diferencias / len(valores)

    desviacion_estandar = math.sqrt(varianza)

    return desviacion_estandar

valores_ingresados = input("Ingrese los valores separados por espacios: ")
valores = [float(valor) for valor in valores_ingresados.split()]

if len(valores) < 2:
    print("Debe ingresar al menos dos valores para calcular la desviación estándar.")
else:
    resultado = desviacion_estandar(valores)
    print(f"La desviación estándar es: {resultado:.2f}") 


    
