import math
n = int(input("Ingrese n: "))
cantidad_productos = int(input("Ingrese la cantidad de productos: "))

precio_total = 0
descuento_total = 0

for i in range(1, cantidad_productos + 1):
    precio_producto = float(input(f"Ingrese el precio del producto {i}: "))
    precio_total += precio_producto

    if i <= n:
        descuento = 0.2  
    else:
        descuento = descuento / 2  

    descuento_producto = math.floor(precio_producto * descuento)
    descuento_total += descuento_producto

precio_final = precio_total - descuento_total

print(f"Precio total: {precio_total:.2f} pesos")
print(f"Descuento total: {descuento_total:.2f} pesos")
print(f"Precio final después del descuento: {precio_final:.2f} pesos")  
