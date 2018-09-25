# Main controller-file of Babylon Tower Solver
# 
# Tecnológico de Costa Rica
# Computing Engineering School
# Course
#   Inteligencia Artificial
#   Teacher Jorge Vargas
# Programmers
#   Edisson López @ediloaz
#   Alonso Rivas
# September, 2018
#


from copy import deepcopy
import PrimerProyectoLogica as Logic


# True:  Working in the logic part
# False: Not Working in the logic part
def SendTablesToLogic(initial_table, goal_table):
    print()
    print("Tablas recibidas")
    initial_table.PrintTorreDetallada()
    goal_table.PrintTorreDetallada()
    Logic.RecibirInformacionDesdeInterfaz(initial_table, goal_table)
    # Aquí va a durar una eternidad, entonces hay que
    # pintar una interfaz de "cargando" desde la Interfaz

def SendListToInterface(list_solution):
    print("Se recibió una lista de largo ", len(list_solution))
