import json
import os

#importar y guardar lista json campers
def load_campers_json():
    try:
      with open(os.path.join("Data", "Campers.json"), 'r') as archivo_json:        
        lista_campers = json.load(archivo_json)
        print("La lista de campers ha sido guardada")
        return lista_campers
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")

lista_campers = load_campers_json()

#Registrar datos de camper
def crear_camper():
    Nombre= input("Ingrese el nombre del cliente: ")
    Apellido= int(input("Ingrese el apellido del cliente: "))
    Identificacion= int(input("Ingrese la identificación del cliente: "))
    Direccion= int(input("Ingrese la dirección del cliente: "))
    Telefono= int(input("Ingrese el teléfono del cliente: "))
    Acudiente= int(input("Ingrese el/la acudiente del cliente: "))
    NotaP= int(input("Ingrese la notaP del cliente: "))
    NotaT= int(input("Ingrese la notaT del cliente: "))

    camper = {
        'nombre': Nombre,
        'apellido': Apellido,
        'identificacion':Identificacion,
        'direccion': Direccion,
        'telefono': Telefono,
        'acudiente': Acudiente,
        'notaP': NotaP,
        'notaT': NotaT
    }

    lista_campers.append(camper)
    print("Se creó el camper con éxito")
    #llama la funcion de guardar campers json
    guardar_json()


#Guardar archivo json de campers
def guardar_json():
    try:
      with open(os.path.join("Data", "Campers.json"), 'w') as archivo_json:
        json.dump(lista_campers, archivo_json, indent=2)
        print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
      

      
#listado de campers 
def listar_campers():
    print("Listado de campers: ")
    for camper in lista_campers:
        print(camper)

