productos = [
    (41419, 'Fideos',        450, 210),
    (70717, 'Cuaderno',      900, 119),
    (78714, 'Jabon',         730, 708),
    (30877, 'Desodorante',  2190,  79),
    (47470, 'Yogur',          99, 832),
    (50809, 'Palta',         500,  55),
    (75466, 'Galletas',      235,   0),
    (33692, 'Bebida',        700,  20),
    (89148, 'Arroz',         900, 121),
    (66194, 'Lapiz',         120, 900),
    (15982, 'Vuvuzela',    12990,  40),
    (41235, 'Chocolate',    3099,  48),
]

clientes = [
    ('11652624-7', 'Perico Los Palotes'),
    ( '8830268-0', 'Leonardo Farkas'),
    ( '7547896-8', 'Fulanita de Tal'),
]

ventas = [
    (1, (2010,  9, 12),  '8830268-0'),
    (2, (2010,  9, 19), '11652624-7'),
    (3, (2010,  9, 30),  '7547896-8'),
    (4, (2010, 10,  1),  '8830268-0'),
    (5, (2010, 10, 13),  '7547896-8'),
    (6, (2010, 11, 11), '11652624-7'),
]

itemes = [
    (1, 89148,  3),
    (2, 50809,  4),
    (2, 33692,  2),
    (2, 47470,  6),
    (3, 30877,  1),
    (4, 89148,  1),
    (4, 75466,  2),
    (5, 89148,  2),
    (5, 47470, 10),
    (6, 41419,  2),
]

def producto_mas_caro(productos):
    producto_caro = max(productos, key=lambda x: x[2])
    return producto_caro[1]

def valor_total_bodega(productos):
    return sum(precio * cantidad for _, _, precio, cantidad in productos)

def ingreso_total_por_ventas(itemes, productos):
    ingreso_total = sum(cantidad * precio for _, codigo_producto, cantidad in itemes
                       for _, nombre, precio, _ in productos if codigo_producto == nombre)
    return ingreso_total

def producto_con_mas_ingresos(itemes, productos):
    ingresos_por_producto = {}
    for _, codigo_producto, cantidad in itemes:
        for _, nombre, precio, _ in productos:
            if codigo_producto == nombre:
                ingresos_por_producto[nombre] = ingresos_por_producto.get(nombre, 0) + cantidad * precio

    producto_mas_ingresos = max(ingresos_por_producto, key=ingresos_por_producto.get)
    return producto_mas_ingresos

def cliente_que_mas_pago(itemes, productos, clientes):
    ingresos_por_cliente = {}
    for numero_boleta, codigo_producto, cantidad in itemes:
        for _, rut_cliente in ventas:
            if rut_cliente not in ingresos_por_cliente:
                ingresos_por_cliente[rut_cliente] = 0
            for _, nombre, precio, _ in productos:
                if codigo_producto == nombre and ventas[numero_boleta - 1][2] == rut_cliente:
                    ingresos_por_cliente[rut_cliente] += cantidad * precio

    cliente_mas_pago = max(ingresos_por_cliente, key=ingresos_por_cliente.get)
    nombre_cliente = next(nombre for rut, nombre in clientes if rut == cliente_mas_pago)
    return nombre_cliente

def total_ventas_del_mes(anio, mes, itemes, productos):
    ventas_del_mes = sum(cantidad * precio for numero_boleta, codigo_producto, cantidad in itemes
                         if ventas[numero_boleta - 1][1][0] == anio and ventas[numero_boleta - 1][1][1] == mes
                         for _, nombre, precio, _ in productos if codigo_producto == nombre)
    return ventas_del_mes

def fecha_ultima_venta_producto(codigo_producto, itemes, ventas):
    ultima_fecha = max(ventas[numero_boleta - 1][1] for numero_boleta, cod_producto, cantidad in itemes
                      if cod_producto == codigo_producto)
    return ultima_fecha

# Pruebas
print(producto_mas_caro(productos))
print(valor_total_bodega(productos))
print(ingreso_total_por_ventas(itemes, productos))
print(total_ventas_del_mes(2010, 10, itemes, productos))
print(fecha_ultima_venta_producto(47470, itemes, ventas))
