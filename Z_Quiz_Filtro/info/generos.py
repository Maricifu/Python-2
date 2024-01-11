import json
import os

def load_peliculas_json():
    try:
        archivo_path = os.path.join("Python-2", "Z_Quiz_Filtro", "data", "peliculas.json")
        with open(archivo_path, 'r') as archivo_json:        
            diccionario = json.load(archivo_json)
            print("El archivo de películas ha sido cargado")
            return diccionario
    except FileNotFoundError:
        print(f"El archivo {archivo_path} no fue encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo JSON: {archivo_path}")
        return None  
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None

diccionario = load_peliculas_json()

# crear género
def crear_genero():

    Id= input("ingrese el id del genero: ")
    Nombre= input("Ingrese el nombre del género: ")

    nuevo_genero = {
            "id": Id,
            "nombre": Nombre
        }

    diccionario["blockbuster"]["peliculas"]["P01"]["generos"] = nuevo_genero
    # Guardar el diccionario actualizado en el archivo JSON
    guardar_json_peliculas(diccionario)


# Guardar archivo JSON de películas
def guardar_json_peliculas(diccionario):
    try:
        with open("peliculas.json", "w") as archivo:
            json.dump(diccionario, archivo, indent=2)
        print("La lista ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya películas guardadas.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")


# Listar géneros JSON
def listar_generos():
    try:
        generos = diccionario["blockbuster"]["peliculas"]["P01"]["generos"]

        for id_genero, info_genero in generos.items():
            print(f"ID del género: {id_genero}")
            print(f"Nombre del género: {info_genero['nombre']}")
            print("-----------------------")
    except Exception as e:
        print(f"Error al listar géneros: {e}")



