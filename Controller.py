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



def SendTablesToLogic(initial_table, goal_table):
    print("Llegué bien")
    initial_table.PrintTorreDetallada()
    goal_table.PrintTorreDetallada()
