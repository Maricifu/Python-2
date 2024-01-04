def mapear(f, valores):
    return [f(x) for x in valores]

def filtrar(f, valores):
    return [x for x in valores if f(x)]

def cuadrado(x):
    return x ** 2

def es_larga(palabra):
    return len(palabra) > 4

resultado_mapear = mapear(cuadrado, [5, 2, 9])
print(resultado_mapear)  # Resultado esperado: [25, 4, 81]

palabras = ['arroz', 'leon', 'oso', 'mochila']
resultado_filtrar = filtrar(es_larga, palabras)
print(resultado_filtrar)  # Resultado esperado: ['arroz', 'mochila']


print(palabras)  # ['arroz', 'leon', 'oso', 'mochila']
