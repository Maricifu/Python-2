import json
import os
from info.peliculas import*

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

# Registrar datos de género
def crear_actor(diccionario, nombre_genero):
    try:
        nuevo_id_genero = "G" + str(len(diccionario["blockbuster"]["peliculas"]["P01"]["generos"]) + 1)
        
        nuevo_genero = {
            "id": nuevo_id_genero,
            "nombre": nombre_genero
        }

        diccionario["blockbuster"]["peliculas"]["P01"]["generos"][nuevo_id_genero] = nuevo_genero

        # Guardar el diccionario actualizado en el archivo JSON
        guardar_json_peliculas(diccionario)
    except Exception as e:
        print(f"Error al crear género: {e}")




# Listar actores JSON
def listar_actores():
    try:
        generos = diccionario["blockbuster"]["peliculas"]["P01"]["actores"]

        for id_actores, info_actores in generos.items():
            print(f"ID del actor: {id_actores}")
            print(f"Nombre del actor: {info_actores['nombre']}")
            print(f"Rol del actor: {info_actores['rol']}")
            print("-----------------------")
    except Exception as e:
        print(f"Error al listar actores: {e}")
