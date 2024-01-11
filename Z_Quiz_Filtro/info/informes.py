import json
import os
from info.actores import *
from info.formatos import *
from info.generos import *
from info.peliculas import *

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



def listar_peliculas_genero(nombre_genero):
    try:
        generos = diccionario["blockbuster"]["peliculas"]["P01"]["generos"]
        
        for id_genero, info_genero in generos.items():
            if info_genero["nombre"].lower() == nombre_genero.lower():
                peliculas_del_genero = []

                for id_pelicula, info_pelicula in diccionario["blockbuster"]["peliculas"].items():
                    if id_genero in info_pelicula.get("generos", {}):
                        peliculas_del_genero.append(info_pelicula)

                if peliculas_del_genero:
                    print(f"Películas del género '{info_genero['nombre']}':")
                    for pelicula in peliculas_del_genero:
                        print(f"ID de la película: {pelicula['id']}")
                        print(f"Nombre de la película: {pelicula['nombre']}")
                        print("-----------------------")
                else:
                    print(f"No hay películas para el género '{info_genero['nombre']}'.")
                break
        else:
            print(f"No se encontró el género '{nombre_genero}'.")
    except Exception as e:
        print(f"Error al listar películas por género: {e}")
