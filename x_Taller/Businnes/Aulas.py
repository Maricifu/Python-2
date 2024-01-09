import json
import os

#importar y guardar lista json aula
def load_aulas_json():
    try:
        with open(os.path.join("Python-2","x_Taller","Data","Aulas.json"), 'r') as archivo_json:        
            lista_aulas = json.load(archivo_json)
            print("La lista de Aulas ha sido cargada")
            return lista_aulas
    except Exception as e:
     print(f"Error al cargar el archivo: {e}")
    return []

lista_aulas = load_aulas_json()
    
#crear datos de aula
def crear_aulas():
    print("Seleccione el aula que desea registrar: ")
    Nombre = input("Ingrese el nombre del aula (Grupo): ")
    Ruta = input("Ingrese la Ruta del aula: ")
    Modulo = input("Ingrese el modulo del aula: ")
    Trainer = input("Ingrese el trainer del aula: ")

    Aula = {
        'nombre':Nombre,
        'ruta': Ruta,
        'modulo': Modulo,
        'trainer': Trainer,
    
    }

    lista_aulas.append(Aula)
    print("Se creó el aula con éxito")
    #llama la funcion de guardar aulas json
    guardar_aulas_json()


#Guardar archivo json de aulas
def guardar_aulas_json():
    try:
      with open(os.path.join("Python-2","x_Taller","Data","Aulas.json"), 'w') as archivo_json:
        json.dump(lista_aulas, archivo_json, indent=2)
        print("La lista de Aulas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya Aulas guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")


#busqueda de aulas
def buscar_aula():
    
    if not lista_aulas:
        print("No hay aulas registradas.")
        return

    nombre_buscar = input("Ingrese el nombre del aula que desea buscar: ")

    encontrado = False

    for Aula in lista_aulas:
        if Aula.get('nombre') == nombre_buscar:
            print(f"Información del aula {nombre_buscar}:")
            print(f"Nombre: {Aula.get('nombre')}")
            print(f"Ruta: {Aula.get('ruta')}")
            print(f"Módulo: {Aula.get('modulo')}")
            print(f"Trainer: {Aula.get('trainer')}")
            encontrado = True
            break

    if not encontrado:
        print(f"No se encontró un Aula con el nombre {nombre_buscar}.")


# modificar aulas
def modificar_aulas():

    if not lista_aulas:
        print("No hay aulas registradas.")
        return

    nombre_aula = input("Ingrese el nombre del aula que desea modificar: ")

    for aula in lista_aulas:
        if aula['nombre'] == nombre_aula:
            # Imprime los datos actuales del aula
            print(f"Datos actuales del aula {nombre_aula}:")
            print(aula)

            # solicita al usuario las modificaciones
            nueva_ruta = input("Nueva ruta del aula (Enter para mantener la actual): ")
            nuevo_modulo = input("Nuevo módulo del aula (Enter para mantener el actual): ")
            nuevo_trainer =input("Nuevo trainer del aula (Enter para mantener el actual)")

            # aplica las modificaciones si se proporcionan nuevos valores
            if nueva_ruta:
                aula['ruta'] = nueva_ruta
            if nuevo_modulo:
                aula['modulo'] = nuevo_modulo
            if nuevo_trainer:
                aula['trainer']= nuevo_trainer

            print("aula modificada con éxito.")
            # guarda los cambios en el archivo JSON
            guardar_aulas_json()
            return

    print(f"No se encontró un aula con el nombre {nombre_aula}.")
