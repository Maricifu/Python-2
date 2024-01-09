from Commons.utils import validar_opcion

def menu_principal():
    print("(----------- Menú Principal-----------)")
    print("1. Campers")
    print("2. Trainers")
    print("3. Matriculas")
    print("4. Aulas")
    print("5. Reportes")
    print("6. Salir")       
    op=validar_opcion("Opcion: ",1,6)
    return op


def menu_campers():
    print("(----------- Menú Campers-----------)")
    print("1. Crear campers")
    print("2. listar campers")
    print("3. Modificar campers")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op
    
    
def menu_trainers():
    print("(----------- Menú Trainers-----------)")
    print("1. Crear trainer")
    print("2. Buscar trainer")
    print("3. Modificar trainer")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op
   

def menu_matriculas():
    print("(----------- Menú Matriculas-----------)")
    print("1. Crear Matriculas")
    print("2. Buscar Matriculas")
    print("3. Modificar Matriculas")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op


def menu_aulas():
    print("(----------- Menú Aulas-----------)")
    print("1. Crear Aulas")
    print("2. Buscar Aulas")
    print("3. Modificar Aulas")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op


def menu_reportes():
    print("(----------- Menú Reportes-----------)")
    print("1. Campers estado inscrito")
    print("2. Campers aprobaron examen")
    print("3. Trainers trabajando en campus")
    print("4. Campers bajo rendimiento")
    print("5. Rutas de entrenamiento")
    print("6  Campers aprobados y reprobados según ruta")
    print("7. Salida")
    op=validar_opcion("Opcion: ",1,7)
    return op

# menu de rutas de los reportes
def menu_rutas():
    print("(----------- Menú Rutas-----------)")
    print("1. NodeJS")
    print("2. Java")
    print("3. NodeCore")
    print("4. Salir")
    op=validar_opcion("Opcion: ",1,4)
    return op
