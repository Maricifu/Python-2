#rectángulo
altura = int(input("Altura del rectángulo: "))
ancho = int(input("Ancho del rectángulo: "))

for i in range(altura):
    print('*' * ancho)

#triángulo
altura = int(input("Altura del triángulo: "))

for i in range(1, altura + 1):
    print('*' * i)

#hexágono
lado = int(input("Lado del hexágono: "))

for i in range(-lado + 1, lado):
    espacios = abs(i)
    asteriscos = lado - espacios
    print(' ' * espacios + '*' * (2 * asteriscos - 1)) 

