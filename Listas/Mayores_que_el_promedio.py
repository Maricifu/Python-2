num_datos = int(input("Ingrese cuántos datos ingresará: "))

datos = []
for i in range(num_datos):
    dato = float(input(f"Ingrese el dato {i + 1}: "))
    datos.append(dato)

promedio = sum(datos) / len(datos)

mayores_al_promedio = sum(1 for dato in datos if dato > promedio)

print(f"El promedio de los datos es: {promedio:.2f}")
print(f"{mayores_al_promedio} dato(s) es/son mayor(es) que el promedio.")
