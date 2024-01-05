ventas = [
    ("ProductoA", 10, 150),
    ("ProductoB", 5, 200),
    ("ProductoA", 8, 120),
    ("ProductoC", 12, 80),
    ("ProductoB", 3, 210),
    ("ProductoA", 15, 130),
    ("ProductoC", 7, 85),
]

total_ventas_por_producto = {}
for venta in ventas:
    producto, cantidad, precio_unitario = venta
    total_ventas_por_producto[producto] = total_ventas_por_producto.get(producto, 0) + cantidad

print("1. Total de Ventas por Producto:")
print(total_ventas_por_producto)
print()

productos_mas_de_10_ventas = {producto for producto, cantidad in total_ventas_por_producto.items() if cantidad > 10}

print("2. Productos con Más de 10 Ventas:")
print(productos_mas_de_10_ventas)
print()

ganancia_total = sum(cantidad * precio_unitario for _, cantidad, precio_unitario in ventas)

print("3. Ganancia Total:")
print(ganancia_total)
