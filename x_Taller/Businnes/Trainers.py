import json
import os

#importar y guardar lista json trainers
def load_trainers_json():
    try:
        with open(os.path.join("Python-2","x_Taller","Data","Trainers.json"), 'r') as archivo_json:        
            lista_trainers= json.load(archivo_json)
            print("La lista de Trainers ha sido guardada")
            return lista_trainers
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")

lista_trainers = load_trainers_json()

#Registrar datos de trainers
def crear_trainer():
    Nombre= input("Ingrese el nombre del trainer: ")
    Apellido= (input("Ingrese el apellido del trainer: "))
    Horario= (input("Ingrese el horario del trainer: "))
    Ruta= (input("Ingrese la ruta del trainer"))

    trainer = {
        'nombre': Nombre,
        'apellido': Apellido,
        'horario': Horario,
        'ruta': Ruta
    }

    lista_trainers.append(trainer)
    print("Se creó el trainer con éxito")
    #llama la funcion de guardar trainers json
    guardar_json_trainers()


#Guardar archivo json de trainers
def guardar_json_trainers():
    try:
      with open(os.path.join("Python-2","x_Taller","Data","Trainers.json"), 'w') as archivo_json:
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
    
    if not lista_trainers:
        print("No hay trainers registrados.")
        return

    nombre_buscar = input("Ingrese el nombre del trainer que desea buscar: ")

    encontrado = False

    for trainer in lista_trainers:
        if trainer.get('nombre') == nombre_buscar:
            print(f"Información del trainer {nombre_buscar}:")
            print(f"Nombre: {trainer.get('nombre')}")
            print(f"Apellido: {trainer.get('apellido')}")
            print(f"Horario: {trainer.get('horario')}")
            print(f"Ruta: {trainer.get('ruta')}")
            encontrado = True
            break

    if not encontrado:
        print(f"No se encontró un trainer con el nombre {nombre_buscar}.")


#Modificar trainer
def modificar_trainer():

    if not lista_trainers:
        print("No hay trainers registrados.")
        return

    nombre_trainer = input("Ingrese el nombre del trainer que desea modificar: ")

    for trainer in lista_trainers:
        if trainer['nombre'] == nombre_trainer:
            # Imprime los datos actuales del trainer
            print(f"Datos actuales del trainer {nombre_trainer}:")
            print(trainer)

            # solicita al usuario las modificaciones
            nuevo_horario = input("Nuevo horario del trainer (Enter para mantener el actual): ")
            nueva_ruta = input("Nueva ruta del trainer (Enter para mantener la actual): ")

            # aplica las modificaciones si se proporcionan nuevos valores
            if nuevo_horario:
                trainer['horario'] = nuevo_horario
            if nueva_ruta:
                trainer['ruta'] = nueva_ruta

            print("Trainer modificado con éxito.")
            # guarda los cambios en el archivo JSON
            guardar_json_trainers()
            return

    print(f"No se encontró un trainer con el nombre {nombre_trainer}.")
