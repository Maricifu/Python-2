import json
import os

#importar y guardar lista json campers
def load_campers_json():
    try:
        with open(os.path.join("Python-2","x_Taller","Data","Campers.json"), 'r') as archivo_json:        
            lista_campers = json.load(archivo_json)
            print("La lista de campers ha sido guardada")
            return lista_campers
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")

lista_campers = load_campers_json()

#Registrar datos de camper
def crear_camper():
    Nombre= input("Ingrese el nombre del cliente: ")
    Apellido= (input("Ingrese el apellido del cliente: "))
    Identificacion= int(input("Ingrese la identificación del cliente: "))
    Direccion= (input("Ingrese la dirección del cliente: "))
    Telefono= int(input("Ingrese el teléfono del cliente: "))
    Acudiente= (input("Ingrese el/la acudiente del cliente: "))
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
    guardar_json_campers()


#Guardar archivo json de campers
def guardar_json_campers():
    try:
      with open(os.path.join("Python-2","x_Taller","Data","Campers.json"), 'w') as archivo_json:
        json.dump(lista_campers, archivo_json, indent=2)
        print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
      

      
#listado de campers 
def listar_camper():

    if not lista_campers:
        print("No hay campers registrados.")
    else:
        print("Listado de campers:")
        for camper in lista_campers:
            print(f"Nombre: {camper.get('nombre')}")
            print(f"Apellido: {camper.get('apellido')}")
            print(f"Identificación: {camper.get('identificacion')}")
            print(f"Dirección: {camper.get('direccion')}")
            print(f"Teléfono: {camper.get('telefono')}")
            print(f"Acudiente: {camper.get('acudiente')}")
            print(f"NotaP: {camper.get('notaP')}")
            print(f"NotaT: {camper.get('notaT')}")
            print("------------------------")


# modificar camper
def modificar_camper():

    if not lista_campers:
        print("No hay campers registrados.")
        return

    identificacion_buscar = (input("Ingrese la identificación del camper que desea modificar: "))

    encontrado = False

    for camper in lista_campers:
        if camper.get('identificacion') == identificacion_buscar:
            print(f"Información actual del camper con identificación {identificacion_buscar}:")
            print(camper)

            # Solicitar al usuario las modificaciones
            nueva_direccion = input("Nueva dirección del camper (Enter para mantener la actual): ")
            nuevo_telefono = input("Nuevo teléfono del camper (Enter para mantener el actual): ")
            nuevo_acudiente = input("Nuevo acudiente del camper (Enter para mantener el actual): ")
            nueva_notaP = input("Nueva notaP del camper (Enter para mantener la actual): ")
            nueva_notaT = input("Nueva notaT del camper (Enter para mantener la actual): ")

            # Aplicar las modificaciones si se proporcionan nuevos valores
            if nueva_direccion:
                camper['direccion'] = nueva_direccion
            if nuevo_telefono:
                camper['telefono'] = nuevo_telefono
            if nuevo_acudiente:
                camper['acudiente'] = nuevo_acudiente
            if nueva_notaP:
                camper['notaP'] = nueva_notaP
            if nueva_notaT:
                camper['notaT'] = nueva_notaT

            print("Camper modificado con éxito.")
            encontrado = True
            break

    if not encontrado:
        print(f"No se encontró un camper con la identificación {identificacion_buscar}.")

    guardar_json_campers()
