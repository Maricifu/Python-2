import json
import os
from Commons.menus import *
from Commons.utils import *


def campers_inscritos():
    print("Los campers inscritos son:")  
    def nom_ap(file):
        try:
            with open(file, 'r') as archivo_json:
                data = json.load(archivo_json)
                
                if all(entry.get('nombre') is not None and entry.get('apellido') is not None for entry in data):
               
                    names_and_surnames = [(entry['nombre'], entry['apellido']) for entry in data]
                    return names_and_surnames
                else:
                    print("El archivo JSON no tiene la estructura esperada (nombre y apellido).")
                    return []
        except FileNotFoundError:
            print(f"El archivo  no fue encontrado.")
            return []
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
            return []
    
    json_path = os.path.join("Python-2","x_Taller","Data","Campers.json")

    nombres_apellidos = nom_ap(json_path)

    for nombre, apellido in nombres_apellidos:
            print(f"{nombre} {apellido}")


def campers_aprobados():
    print("Los campers aprobados son:")
    def ap(file_path):
        try:
            with open(file_path, 'r') as archivo_json:
                data = json.load(archivo_json)

                if all(entry.get('nombre') is not None and entry.get('apellido') is not None and
                       entry.get('notaT') is not None and entry.get('notaP') is not None for entry in data):
                   
                    info_campers = [(entry['nombre'], entry['apellido'], entry['notaT'], entry['notaP']) for entry in data]
                    return info_campers
                else:
                    print("El archivo JSON no tiene la estructura esperada (nombre, apellido, notaT, notaP).")
                    return []
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
            return []
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
            return []

    json_path = os.path.join("Python-2","x_Taller","Data","Campers.json")

    info_campers = ap(json_path)

    for nombre, apellido, notaT, notaP in info_campers:
        promedio = (notaT + notaP) / 2
        if promedio > 60:
            print(f"{nombre} {apellido} - Promedio: {promedio}")

def lista_trainers_repo():
    print("Los trainers en campus son:")
    def nom_ap_p(file):
        try:
            with open(file, 'r') as archivo_json:
                data = json.load(archivo_json)
                
                if all(entry.get('nombre') is not None and entry.get('apellido') is not None for entry in data):
                  
                    names_and_surnames = [(entry['nombre'], entry['apellido']) for entry in data]
                    return names_and_surnames
                else:
                    print("El archivo JSON no tiene la estructura esperada (nombre y apellido).")
                    return []
        except FileNotFoundError:
            print(f"El archivo  no fue encontrado.")
            return []
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
            return []
    
    json_path = os.path.join("Python-2","x_Taller","Data","Trainers.json")

    nombres_apellidos = nom_ap_p(json_path)

    for nombre, apellido in nombres_apellidos:
            print(f"{nombre} {apellido}")


def camper_bajo_rendimiento():
    print("Los campers con bajo rendimiento son:")
    def bajo_ren(file_path):
        try:
            with open(file_path, 'r') as archivo_json:
                data = json.load(archivo_json)

                if all(entry.get('nombre') is not None and entry.get('apellido') is not None and
                       entry.get('notaT') is not None and entry.get('notaP') is not None for entry in data):
                
                    info_campers = [(entry['nombre'], entry['apellido'], entry['notaT'], entry['notaP']) for entry in data]
                    return info_campers
                else:
                    print("El archivo JSON no tiene la estructura esperada (nombre, apellido, notaT, notaP).")
                    return []
        except FileNotFoundError:
            print("El archivo no fue encontrado.")
            return []
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
            return []

    json_path = os.path.join("Python-2","x_Taller","Data","OldCampers.json")

    info_campers = bajo_ren(json_path)

    for nombre, apellido, notaT, notaP in info_campers:
        promedio = (notaT + notaP) / 2
        if promedio < 60:
            print(f"{nombre} {apellido} - Promedio: {promedio}")


def camper_ent_ruta1():
    def mostrar_campers_con_ruta(json_path):
        try:
            with open(json_path, 'r') as archivo_json:
                data = json.load(archivo_json)

                if all(entry.get('nombre') is not None and entry.get('apellido') is not None and
                    entry.get('profesor') is not None and entry.get('ruta') is not None for entry in data):
            
                    campers_nodejs = [(entry['nombre'], entry['apellido'], entry['profesor']) for entry in data if entry['ruta'] == 'NodeJS']

                    for nombre, apellido, profesor in campers_nodejs:
                        print(f"Nombre: {nombre}, Apellido: {apellido}, Profesor: {profesor}")

                else:
                    print("El archivo JSON no tiene la estructura esperada (nombre, apellido, profesor, ruta).")
        except FileNotFoundError:
            print(f"El archivo '{json_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")

    json_path = os.path.join("Python-2","x_Taller","Data","OldCampers.json")
    mostrar_campers_con_ruta(json_path)


def camper_ent_ruta2():
    def mostrar_campers_con_ruta(json_path):
        try:
            with open(json_path, 'r') as archivo_json:
                data = json.load(archivo_json)

                if all(entry.get('nombre') is not None and entry.get('apellido') is not None and
                    entry.get('profesor') is not None and entry.get('ruta') is not None for entry in data):
            
                    campers_nodejs = [(entry['nombre'], entry['apellido'], entry['profesor']) for entry in data if entry['ruta'] == 'Java']

                    for nombre, apellido, profesor in campers_nodejs:
                        print(f"Nombre: {nombre}, Apellido: {apellido}, Profesor: {profesor}")

                else:
                    print("El archivo JSON no tiene la estructura esperada (Nombre, Apellido, profesor, Ruta).")
        except FileNotFoundError:
            print(f"El archivo '{json_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")

    json_path = os.path.join("Python-2","x_Taller","Data","OldCampers.json")
    mostrar_campers_con_ruta(json_path)


def camper_ent_ruta3():
    def mostrar_campers_con_ruta(json_path):
        try:
            with open(json_path, 'r') as archivo_json:
                data = json.load(archivo_json)

                if all(entry.get('nombre') is not None and entry.get('apellido') is not None and
                    entry.get('profesor') is not None and entry.get('ruta') is not None for entry in data):
            
                    campers_nodejs = [(entry['nombre'], entry['apellido'], entry['profesor']) for entry in data if entry['ruta'] == 'NetCore']

                    for nombre, apellido, profesor in campers_nodejs:
                        print(f"Nombre: {nombre}, Apellido: {apellido}, Profesor: {profesor}")

                else:
                    print("El archivo JSON no tiene la estructura esperada (Nombre, Apellido, profesor, Ruta).")
        except FileNotFoundError:
            print(f"El archivo '{json_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")

    json_path = os.path.join("Python-2","x_Taller","Data","OldCampers.json")
    mostrar_campers_con_ruta(json_path)


def camp_trainer():
    limpiar_pantalla() 
    op=menu_rutas()
    if op ==1:
        camper_ent_ruta1()
    elif op==2:
        camper_ent_ruta2()
    elif op==3:
        camper_ent_ruta3()

def camp_ruta1():
    def mostrar_campers_con_ruta(json_path):
        try:
            with open(json_path, 'r') as archivo_json:
                data = json.load(archivo_json)

             
                if all(entry.get('nombre') is not None and entry.get('apellido') is not None and
                    entry.get('profesor') is not None and entry.get('ruta') is not None and
                    entry.get('notaT') is not None and entry.get('notaP') is not None for entry in data):

                    campers_nodejs = [(entry['nombre'], entry['apellido'], entry['notaT'], entry['notaP']) for entry in data if entry['ruta'] == 'NodeJS']

                    for nombre, apellido, notaT, notaP in campers_nodejs:
              
                        nota_final = 0.3 * notaT + 0.6 * notaP
                 
                        estado = "Aprobado" if nota_final > 60 else "En Riesgo"

                        print(f"Nombre: {nombre}, Apellido: {apellido}, Nota Final: {nota_final:.2f}, Estado: {estado}")

                else:
                    print("El archivo JSON no tiene la estructura esperada (Nombre, Apellido, profesor, Ruta, NotaT, NotaP).")
        except FileNotFoundError:
            print(f"El archivo '{json_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
         
    json_path = os.path.join("Python-2","x_Taller","Data","OldCampers.json")

    mostrar_campers_con_ruta(json_path)


def camp_ruta2():
    def mostrar_campers_con_ruta(json_path):
            try:
                with open(json_path, 'r') as archivo_json:
                    data = json.load(archivo_json)

                
                    if all(entry.get('nombre') is not None and entry.get('apellido') is not None and
                        entry.get('profesor') is not None and entry.get('ruta') is not None and
                        entry.get('notaT') is not None and entry.get('notaP') is not None for entry in data):

                        campers_nodejs = [(entry['nombre'], entry['apellido'], entry['notaT'], entry['notaP']) for entry in data if entry['ruta'] == 'Java']

                        for nombre, apellido, notaT, notaP in campers_nodejs:
                
                            nota_final = 0.3 * notaT + 0.6 * notaP
                    
                            estado = "Aprobado" if nota_final > 60 else "En Riesgo"

                            print(f"Nombre: {nombre}, Apellido: {apellido}, Nota Final: {nota_final:.2f}, Estado: {estado}")

                    else:
                        print("El archivo JSON no tiene la estructura esperada (Nombre, Apellido, profesor, Ruta, NotaT, NotaP).")
            except FileNotFoundError:
                print(f"El archivo '{json_path}' no fue encontrado.")
            except Exception as e:
                print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
            
    json_path = os.path.join("Python-2","x_Taller","Data","OldCampers.json")

    mostrar_campers_con_ruta(json_path)


def camp_ruta3():
    def mostrar_campers_con_ruta(json_path):
        try:
            with open(json_path, 'r') as archivo_json:
                data = json.load(archivo_json)

             
                if all(entry.get('nombre') is not None and entry.get('apellido') is not None and
                    entry.get('profesor') is not None and entry.get('ruta') is not None and
                    entry.get('notaT') is not None and entry.get('notaP') is not None for entry in data):
                    campers_nodejs = [(entry['nombre'], entry['apellido'], entry['notaT'], entry['notaP']) for entry in data if entry['ruta'] == 'NetCore']

                    for nombre, apellido, notaT, notaP in campers_nodejs:
              
                        nota_final = 0.3 * notaT + 0.6 * notaP
                 
                        estado = "Aprobado" if nota_final > 60 else "En Riesgo"

                        print(f"Nombre: {nombre}, Apellido: {apellido}, Nota Final: {nota_final:.2f}, Estado: {estado}")
                else:
                    print("El archivo JSON no tiene la estructura esperada (Nombre, Apellido, Profesor, Ruta, NotaT, NotaP).")
        except FileNotFoundError:
            print(f"El archivo '{json_path}' no fue encontrado.")
        except Exception as e:
            print(f"Error al cargar el archivo JSON: {type(e).__name__}: {e}")
         
    json_path = os.path.join("Python-2","x_Taller","Data","OldCampers.json")

    mostrar_campers_con_ruta(json_path)


def camp_ap_rep_ruta():
    limpiar_pantalla() 
    op=menu_rutas()
    if op ==1:
        camp_ruta1()
    elif op==2:
        camp_ruta2()
    elif op==3:
        camp_ruta3()
