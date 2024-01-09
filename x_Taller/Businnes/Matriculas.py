import json
import os

#importar y guardar lista json matriculas
def load_matriculas_json():
    try:
        with open(os.path.join("python-2","x_Taller","Data","OldCampers.json"), 'r') as archivo_json:        
            lista_matriculas = json.load(archivo_json)
            print("La lista de matriculas ha sido cargada")
            return lista_matriculas
    except Exception as e:
     print(f"Error al cargar el archivo: {e}")
    return []

lista_matriculas = load_matriculas_json()


# registrar datos de matricula
def crear_matricula():
    print("Ingrese los datos del nuevo Camper")
    Nombre= input("Ingrese el nombre del camper: ")
    Apellido= input("Ingrese el apellido del camper")
    Identificacion = int(input("Ingrese el numero de identificacion del camper"))
    Direccion= input("Ingrese la direccion del Camper")
    Telefono= input("Ingrese el telefono del camper")
    Acudiente= input("Ingrese el nombre del acudiente del camper")
    Ruta= input("Ingrese la ruta del camper")
    Horario= input("Ingrese el horario del camper")
    Trainer = input("Ingrese el trainer asignado")
    Aula= input("Ingrese al aula")
    Modulo= input("Ingrese el modulo")
    Fecha_Inicio= input("Ingrese la fecha de inicio")
    Fecha_Fin= input("Ingrese la fecha estimada para finalizar la formacion")
   
    Matricula = {
        'nombre': Nombre,
        'apellido': Apellido,
        'identificacion': Identificacion,
        'direccion': Direccion,
        'telefono': Telefono,
        'acudiente': Acudiente,
        'ruta': Ruta,
        'horario': Horario,
        'trainer': Trainer,
        'aula': Aula,
        'modulo': Modulo,
        'fecha Inicio': Fecha_Inicio,
        'fecha Fin': Fecha_Fin 
    }

    lista_matriculas.append(Matricula)
    print("Se creó la  matrícula con éxito")
    #llama la funcion de guardar matricula json
    guardar_json_matricula()


# guardar archico json de matriculas
def guardar_json_matricula():
    try:
      with open(os.path.join("python-2","x_Taller","Data","OldCampers.json"), 'w') as archivo_json:
        json.dump(lista_matriculas, archivo_json, indent=2)
        print("La lista de matriculas ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya matriculas guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")


#buscar matriculas
def buscar_matricula():
    lista_matriculas = load_matriculas_json()

    if not lista_matriculas:
        print("No hay matriculas registradas.")
        return

    identificacion_buscar = (input("Ingrese la identificación de la matrícula que desea buscar: "))

    encontrado = False

    for Matricula in lista_matriculas:
        if Matricula.get('identificacion') == identificacion_buscar:
            print(f"Información de la matrícula con identificación {identificacion_buscar}:")
            print(f"Nombre: {Matricula.get('nombre')}")
            print(f"Apellido: {Matricula.get('apellido')}")
            print(f"Identificación: {Matricula.get('identificacion')}")
            print(f"Dirección: {Matricula.get('direccion')}")
            print(f"Teléfono: {Matricula.get('telefono')}")
            print(f"Acudiente: {Matricula.get('acudiente')}")
            print(f"Ruta: {Matricula.get('ruta')}")
            print(f"Horario: {Matricula.get('horario')}")
            print(f"Trainer: {Matricula.get('trainer')}")
            print(f"Aula: {Matricula.get('aula')}")
            print(f"Módulo: {Matricula.get('modulo')}")
            print(f"Fecha de Inicio: {Matricula.get('fecha Inicio')}")
            print(f"Fecha de Fin: {Matricula.get('fecha Fin')}")
            encontrado = True
            break

    if not encontrado:
        print(f"No se encontró una matrícula con la identificación {identificacion_buscar}.")



#modificar matricula
def modificar_matricula():
    lista_matriculas = load_matriculas_json()

    if not lista_matriculas:
        print("No hay matriculas registradas.")
        return

    identificacion_buscar = int(input("Ingrese la identificación de la matrícula que desea modificar: "))

    encontrado = False

    for Matricula in lista_matriculas:
        if Matricula.get('identificacion') == identificacion_buscar:
            print(f"Información actual de la matrícula con identificación {identificacion_buscar}:")
            print(Matricula)

            # Solicitar al usuario las modificaciones
            nuevo_nombre = input("Nuevo nombre del camper (deje en blanco para mantener el actual): ")
            nuevo_apellido = input("Nuevo apellido del camper (deje en blanco para mantener el actual): ")
            nueva_direccion = input("Nueva dirección del camper (deje en blanco para mantener la actual): ")
            nuevo_telefono = input("Nuevo teléfono del camper (deje en blanco para mantener el actual): ")
            nuevo_acudiente = input("Nuevo acudiente del camper (deje en blanco para mantener el actual): ")
            nueva_ruta = input("Nueva ruta del camper (deje en blanco para mantener la actual): ")
            nuevo_horario = input("Nuevo horario del camper (deje en blanco para mantener el actual): ")
            nuevo_trainer = input("Nuevo trainer asignado (deje en blanco para mantener el actual): ")
            nueva_aula = input("Nueva aula (deje en blanco para mantener la actual): ")
            nuevo_modulo = input("Nuevo modulo (deje en blanco para mantener el actual): ")
            nueva_fecha_inicio = input("Nueva fecha de inicio (deje en blanco para mantener la actual): ")
            nueva_fecha_fin = input("Nueva fecha estimada para finalizar la formación (deje en blanco para mantener la actual): ")

            # Aplicar las modificaciones si se proporcionan nuevos valores
            if nuevo_nombre:
                Matricula['nombre'] = nuevo_nombre
            if nuevo_apellido:
                Matricula['apellido'] = nuevo_apellido
            if nueva_direccion:
                Matricula['direccion'] = nueva_direccion
            if nuevo_telefono:
                Matricula['telefono'] = nuevo_telefono
            if nuevo_acudiente:
                Matricula['acudiente'] = nuevo_acudiente
            if nueva_ruta:
                Matricula['ruta'] = nueva_ruta
            if nuevo_horario:
                Matricula['horario'] = nuevo_horario
            if nuevo_trainer:
                Matricula['trainer'] = nuevo_trainer
            if nueva_aula:
                Matricula['aula'] = nueva_aula
            if nuevo_modulo:
                Matricula['modulo'] = nuevo_modulo
            if nueva_fecha_inicio:
                Matricula['fecha Inicio'] = nueva_fecha_inicio
            if nueva_fecha_fin:
                Matricula['fecha Fin'] = nueva_fecha_fin

            print("Matrícula modificada con éxito.")
            encontrado = True
            break

    if not encontrado:
        print(f"No se encontró una matrícula con la identificación {identificacion_buscar}.")

    # Guardar la lista de matriculas actualizada
    guardar_json_matricula()

modificar_matricula()