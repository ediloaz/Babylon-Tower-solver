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
import Logic as Logic
import time

# True:  Working in the logic part
# False: Not Working in the logic part
def SendTablesToLogic(initial_table, goal_table):
    print()
    print("Tablas recibidas")
    initial_table.PrintTorreDetallada()
    goal_table.PrintTorreDetallada()
    Logic.RecibirInformacionDesdeInterfaz(initial_table, goal_table)
    return Logic.GetSolution()
    # Aquí va a durar una eternidad, entonces hay que
    # pintar una interfaz de "cargando" desde la Interfaz

def SendSolutionToInterface():
    return Logic.EnviarInformacionHaciaInterfaz()
    
def GetNextTableSolution():
    return Logic.EnviarSiguienteTablaSolucion()

def GetPreviousTableSolution():
    return Logic.EnviarAnteriorTablaSolucion()

def LongSolution():
    return Logic.LargoSolucion()

def getIdSolucion():
    return Logic.getIdSolucion()

def GetSolutionList():
    return Logic.GetSolution()
