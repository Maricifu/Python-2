def media_aritmetica(datos):
    return sum(datos) / len(datos)

def media_armonica(datos):
    if 0 in datos:
        return None
    return len(datos) / sum(1 / x for x in datos)

def mediana(datos):
    datos_ordenados = sorted(datos)
    n = len(datos)
    if n % 2 == 0:
        medio1 = datos_ordenados[n // 2 - 1]
        medio2 = datos_ordenados[n // 2]
        return (medio1 + medio2) / 2
    else:
        return datos_ordenados[n // 2]

def modas(datos):
    frecuencias = {}
    for dato in datos:
        frecuencias[dato] = frecuencias.get(dato, 0) + 1

    max_frecuencia = max(frecuencias.values())
    modas = [dato for dato, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]
    return modas

def generar_reporte(datos):
    media_aritmetica_resultado = media_aritmetica(datos)
    media_armonica_resultado = media_armonica(datos)
    mediana_resultado = mediana(datos)
    modas_resultado = modas(datos)

    print("Reporte Estadístico:")
    print(f"Datos ingresados: {datos}")
    print(f"Media Aritmética: {media_aritmetica_resultado:.2f}")

    if media_armonica_resultado is not None:
        print(f"Media Armónica: {media_armonica_resultado:.2f}")

    print(f"Mediana: {mediana_resultado:.2f}")
    print(f"Modas: {modas_resultado}")

num_datos = int(input("Ingrese cuántos datos ingresará: "))
datos_ingresados = []

for i in range(num_datos):
    dato = float(input(f"Ingrese el dato {i + 1}: "))
    datos_ingresados.append(dato)

generar_reporte(datos_ingresados) 
