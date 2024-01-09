from Commons.utils import limpiar_pantalla
from Commons.menus import *
from Businnes.Campers import *
from Businnes.Aulas import *
from Businnes.Matriculas import *
from Businnes.Trainers import *
from Businnes.Reportes import *


# functions Campers
def campers():      
    limpiar_pantalla()
    op=menu_campers()
    if op==1:
       crear_camper()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       listar_camper()
       input("Clic cualquier teclas [continuar]: ")
    if op==3:
       modificar_camper()
       input("Clic cualquier teclas [continuar]: ") 
    

# functions trainers
def trainers():
    limpiar_pantalla()    
    op=menu_trainers()
    if op==1:
       crear_trainer()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       buscar_trainer()
       input("Clic cualquier teclas [continuar]: ")
    if op==3:
       modificar_trainer()
       input("Clic cualquier teclas [continuar]: ") 

# functions matriculas
def matriculas():
    limpiar_pantalla()    
    op=menu_matriculas()
    if op==1:
       crear_matricula()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       buscar_matricula()
       input("Clic cualquier teclas [continuar]: ")
    if op==3:
       modificar_matricula()
       input("Clic cualquier teclas [continuar]: ") 


# functions aulas
def aulas():
    limpiar_pantalla()    
    op=menu_aulas()
    if op==1:
       crear_aulas()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       buscar_aula()
       input("Clic cualquier teclas [continuar]: ")
    if op==3:
       modificar_aulas()
       input("Clic cualquier teclas [continuar]: ") 


# functions reportes
def reportes():
    limpiar_pantalla()    
    op=menu_reportes()
    if op==1:
       campers_inscritos()
       input("Clic cualquier teclas [continuar]: ")
    if op==2:
       campers_aprobados()
       input("Clic cualquier teclas [continuar]: ")
    if op==3:
       lista_trainers_repo()
       input("Clic cualquier teclas [continuar]: ") 
    if op==4:
       camper_bajo_rendimiento()
       input("Clic cualquier teclas [continuar]: ") 
    if op==5:
       camp_trainer()
       input("Clic cualquier teclas [continuar]: ") 
    if op==6:
       camp_ap_rep_ruta()
       input("Clic cualquier teclas [continuar]: ") 
    if op==7:
       print("Saliendo") 


#start menu principal
while True: 
   limpiar_pantalla()
   op=menu_principal()
   if  op==1:
       campers()
   elif op==2:
       trainers()
   elif op==3:
       matriculas()
   elif op==4:
       aulas()
   elif op==5:
       reportes()
   elif op==6:
       print("Saliendo")
       break
       