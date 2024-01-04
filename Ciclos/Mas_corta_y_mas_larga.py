n = int(input("Cantidad de palabras: "))

palabra_mas_larga = ""
palabra_mas_corta = ""

for i in range(1, n + 1):
    palabra = input(f"Palabra {i}: ")
    
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra
    
    if i == 1 or len(palabra) < len(palabra_mas_corta):
        palabra_mas_corta = palabra

print(f"La palabra más larga es {palabra_mas_larga}")
print(f"La palabra más corta es {palabra_mas_corta}") 
