from principal.utils import validar_opcion

def main_menu():
    print("(----------- MENÚ PRINCIPAL -----------)")
    print("  1. Administrador de géneros")
    print("  2. Administrador de actores")
    print("  3. Administrador de formatos")
    print("  4. Gestor de informes")
    print("  5. Gestor de películas")
    print("  6. Salir")    
    print("(--------------------------------------)")   
    op=validar_opcion("Opcion: ",1,6)
    return op

def generos_menu ():
    print("(----------- GESTOR DE GÉNEROS -----------)")
    print("  1. Crear género")
    print("  2. Listar géneros")
    print("  3. Menú principal")    
    print("(-----------------------------------------)")   
    op=validar_opcion("Opcion: ",1,3)
    return op    

def actores_menu ():
    print("(----------- GESTOR DE ACTORES -----------)")
    print("  1. Crear actor")
    print("  2. Listar actores")
    print("  3. Menú principal")    
    print("(-----------------------------------------)")   
    op=validar_opcion("Opcion: ",1,3)
    return op    

def formatos_menu ():
    print("(----------- GESTOR DE FORMATOS -----------)")
    print("  1. Crear formato")
    print("  2. Listar formatos")
    print("  3. Menú principal")    
    print("(------------------------------------------)")   
    op=validar_opcion("Opcion: ",1,3)
    return op    


def peliculas_menu ():
    print("(----------- GESTOR DE PELÍCULAS -----------)")
    print("  1. Agergar película")
    print("  2. Editar película")
    print("  3. Eliminar película")    
    print("  4. Eliminar actor")
    print("  5. Buscar película")    
    print("  6. Listar películas") 
    print("  7. Menú principal")       
    print("(-------------------------------------------)")   
    op=validar_opcion("Opcion: ",1,7)
    return op    


def informes_menu ():
    print("(----------- GESTOR DE INFORMES -----------)")
    print("  1. Listar peliculas por género")
    print("  2. Listar las películas del actor Silvester stallone")
    print("  3. Menú principal")    
    print("(------------------------------------------)")   
    op=validar_opcion("Opcion: ",1,3)
    return op    
