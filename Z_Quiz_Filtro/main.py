from principal.utils import *
from principal.Menus import *
from info.actores import *
from info.formatos import *
from info.generos import *
from info.informes import *
from info.peliculas import *


# functions generos
def generos():      
    limpiar_pantalla()
    op=generos_menu()
    if op==1:
       crear_genero()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       listar_generos()
       input("Clic cualquier teclas [continuar]: ")


# functions actores
def actores():      
    limpiar_pantalla()
    op=actores_menu()
    if op==1:
       crear_actor()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       listar_actores()
       input("Clic cualquier teclas [continuar]: ")

    
# functions formatos
def formatos():      
    limpiar_pantalla()
    op=formatos_menu()
    if op==1:
       crear_formato()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       listar_formatos()
       input("Clic cualquier teclas [continuar]: ")


# functions peliculas
def peliculas():      
    limpiar_pantalla()
    op=peliculas_menu()
#   if op==1:
#      agergar_pelicula()
#      input("Clic cualquier teclas [continuar]: ")
#   if op==2:
#      editar_pelicula()
#      input("Clic cualquier teclas [continuar]: ")
#   if op==3:
#      eliminar_pelicula()
#      input("Clic cualquier teclas [continuar]: ")
#   if op==4:
#      eliminar_actor()
#      input("Clic cualquier teclas [continuar]: ")
#   if op==5:
#      buscar_pelicula()
#      input("Clic cualquier teclas [continuar]: ")
#   if op==6:
#      listar_peliculas()
#      input("Clic cualquier teclas [continuar]: ")


# functions informes
def informes():      
    limpiar_pantalla()
    op=informes_menu()
    if op==1:
      listar_peliculas_genero()
      input("Clic cualquier teclas [continuar]: ")
#   if op==2:
#      listar_pleiculas_silvester()
#      input("Clic cualquier teclas [continuar]: ")


#start principal menu
while True: 
   limpiar_pantalla()
   op=main_menu()
   if  op==1:
       generos()
   elif op==2:
       actores()
   elif op==3:
       formatos()
   elif op==4:
       informes()
   elif op==5:
       peliculas()
   elif op==6:
       print("Saliendo")
       break
