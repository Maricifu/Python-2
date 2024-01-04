precio_producto = {'A': 270, 'B': 340, 'C': 390}
valores_monedas = [100, 50, 10]

producto_elegido = input("Elija el producto (A, B o C): ").upper()

if producto_elegido not in precio_producto:
    print("Producto no válido. Programa terminado.")
else:
    precio = precio_producto[producto_elegido]

    monto_ingresado = 0
    while monto_ingresado < precio:
        moneda = int(input(f"Ingrese una moneda ({', '.join(map(str, valores_monedas))}): "))
    
        if moneda not in valores_monedas:
            print("Moneda no válida. Programa terminado.")
            break

        monto_ingresado += moneda

    vuelto = monto_ingresado - precio
    if vuelto > 0:
        print(f"¡Compra exitosa! Vuelto: {vuelto} pesos en monedas:")
        for valor_moneda in valores_monedas:
            while vuelto >= valor_moneda:
                print(valor_moneda)
                vuelto -= valor_moneda
    else:
        print("¡Compra exitosa! No hay vuelto.") 
