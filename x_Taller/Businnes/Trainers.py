import json
import os

#importar y guardar lista json trainers
def load_trainers_json():
    try:
      with open(os.path.join("Data", "Trainers.json"), 'r') as archivo_json:        
        lista_trainers= json.load(archivo_json)
        print("La lista de Trainers ha sido guardada")
        return lista_trainers
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")

lista_trainers = load_trainers_json()

#Registrar datos de trainers
def crear_trainer():
    Nombre= input("Ingrese el nombre del trainer: ")
    Apellido= int(input("Ingrese la apellido del trainer: "))
    Horario= int(input("Ingrese el horario del trainer: "))
    Ruta= int(input("Ingrese la ruta del trainer"))

    trainer = {
        'nombre': Nombre,
        'apellido': Apellido,
        'horario': Horario,
        'ruta': Ruta
    }

    lista_trainers.append(trainer)
    print("Se creó el trainer con éxito")
    #llama la funcion de guardar trainers json
    guardar_json()

#Guardar archivo json de trainers
def guardar_json():
    try:
      with open(os.path.join("Data", "Trainers.json"), 'w') as archivo_json:
        json.dump(lista_trainers, archivo_json, indent=2)
        print("La lista de trainers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya trainers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
      


#busqueda de trainers
def buscar_trainer():
    print("Los trainers en campus son:")
    def nom_ap_p(file):
        try:
            with open(file, 'r') as archivo_json:
                data = json.load(archivo_json)

                if all(entry.get('Nombre') is not None and entry.get('Apellido') is not None for entry in data):

                    names_and_surnames = [(entry['Nombre'], entry['Apellido']) for entry in data]
                    return names_and_surnames
                else:
                    print("El archivo JSON no tiene la estructura esperada (nombre y apellido).")
                    return []
        except FileNotFoundError:
            print(f"El archivo  no fue encontrado.")
            return []
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).name}: {e}")
            return []

    json_path = os.path.join("python-2","x_Taller","Data","Trainers.json")

    nombres_apellidos = nom_ap_p(json_path)

    for Nombre, Apellido in nombres_apellidos:
            print(f"{Nombre} {Apellido}")


# Buscar y mostrar trainers con el mismo nombre
    trainers_encontrados = buscar_trainer(lista_trainers, Nombre)
    if trainers_encontrados:
        print(f"Trainers encontrados para el nombre {Nombre}:")
        for found_trainer in trainers_encontrados:
            print(buscar_trainer)

buscar_trainer()
