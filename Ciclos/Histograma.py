positivos = 0
negativos = 0

print("Ingrese valores enteros (ingrese 0 para finalizar):")

while True:
    valor = int(input("Ingrese un valor: "))

    if valor == 0:
        break

    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

print(f"Se ingresaron {positivos} valores positivos.")
print(f"Se ingresaron {negativos} valores negativos.") 

