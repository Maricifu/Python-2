import os

#limpiar pantalla
def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')    


#verificar que se selecione dentro del rango las opciones del menu 
def validar_opcion(enunciando,inferior,superior):
    while True:
        try:
            opcion =int(input(enunciando))
            if opcion>=inferior and opcion<=superior:
                return opcion
            else:
                print(f"Opción no está entre el intervalo de ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número válido. ")
            