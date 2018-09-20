# Main logical-file of Babylon Tower Solver
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

#
# Área de imports
import Tabla as Tabla
from copy import deepcopy


#
# Área de funciones

def CalcularDistancia (iacutal, jactual, idestino, jdestino):
    j = abs(jactual-jdestino) 
    if (j==3):
        j=1
    D = abs(iacutal-idestino) + j
    return D 

# Antes llamada "Algoritmo"
def Peso(tabla):
    Sum = 0
    g = tabla.getG()
    for i in range(Columnas):
        for j in range(Filas):
            #color que queremos sacarle la distancia
            color = tabla.ObtenerColor(i,j)
            print ("Color: ", color)
            #if (color == "R" or color == "G" or color == "B" or color == "Y" ):
            (idestino,jdestino) = tabla.CalcularIJdelColorMasCercano(i,j)
            DistanciaCalculada = CalcularDistancia(i, j, idestino, jdestino)
            print ("Meta:",idestino,",",jdestino, "distancia",DistanciaCalculada)
            Sum = Sum + DistanciaCalculada
            print()
    peso = (g + (1/20) * Sum)
    Tabla.GuardarPeso(peso)
    return peso

def AumentarLastID():
    global last_id
    last_id += 1

def LastID():
    global last_id
    return last_id

def Largo(lista):
    print("Largo: ", len(lista.lista))

def Visitado(Tabla):
    lista_NO_visitados.Quitar(Tabla)
    lista_visitados.Agregar(Tabla)

# Saca de la lista de no visitados a una tabla y la mete en la de visitados. retorna dicha tabla
# Busca en la lista de NO visitados, el que tiene peso menor. Y lo devuelve como la tabla Padre
# quitandolo de dicha lista y metiendolo en la lista de SI visitados
def SiguienteNodo():
    # Ahorita solo coge el último
    Nodo = lista_NO_visitados.Pop()
    Visitado(Nodo)
    return Nodo

def NuevaTablaIzquierda(TablaPadre, numero_fila):
    nueva_tabla = deepcopy(TablaPadre)
    nueva_tabla.setID(last_id)                                      # Asigna ID
    nueva_tabla.setIDpadre(TablaPadre.getID())      # Asigna ID padre
    nueva_tabla.setG(TablaPadre.getG()+1)               # Asigna g
    nueva_tabla.GirarFilaIzquierda(numero_fila)
    if lista_NO_visitados.Comparar(nueva_tabla):
        return False
    else:
        lista_NO_visitados.Agregar(nueva_tabla)
        AumentarLastID()
        return nueva_tabla

def NuevaTablaDerecha(TablaPadre, numero_fila):
    nueva_tabla = deepcopy(TablaPadre)
    nueva_tabla.setID(last_id)                                      # Asigna ID
    nueva_tabla.setIDpadre(TablaPadre.getID())      # Asigna ID padre
    nueva_tabla.setG(TablaPadre.getG()+1)               # Asigna g
    nueva_tabla.GirarFilaDerecha(numero_fila)
    if lista_NO_visitados.Comparar(nueva_tabla):       # ¿Está visitado?
        return False
    else:
        lista_NO_visitados.Agregar(nueva_tabla)            # Se agrega a la lista de visitados
        AumentarLastID()
        return nueva_tabla

# Crea a parti r de una tabla las siguientes 12 tablas.
def Ramificacion(TablaPadre):
    # Hacia izquierda
    print("- - - - - - - - - - - - - - - - - - ")
    print("Con giro a la izquierda")
    for i in range(5):
        Largo(lista_NO_visitados)
        Largo(lista_visitados)
        nueva_tabla = NuevaTablaIzquierda(TablaPadre, i)
        if (nueva_tabla == False):
            print("Se encontro una igual. Se omitió la tabla, se cierra el nodo" )
        else:
            Peso(nueva_tabla)
            print("Nueva tabla: ", i+1)
            nueva_tabla.PrintTorre()
            
        
    # Hacia derecha
    print("- - - - - - - - - - - - - - - - - - ")
    print("Con giro a la derecha")
    for i in range(4):
        Largo(lista_NO_visitados)
        Largo(lista_visitados)
        nueva_tabla = NuevaTablaDerecha(TablaPadre, i)
        if (nueva_tabla == False):
            print("Se encontro una igual. Se omitió la tabla, se cierra el nodo" )
        else:
            Peso(nueva_tabla)
            print("Nueva tabla: ", i+6)
            nueva_tabla.PrintTorre()

    # Hacia Abajo

    # Hacia Arriba

    
    
            
def Finalizado(tabla):
    pass

def Astar():
    tabla_padre = TablaInicial
    while True:
        print("Pasada por el While True")
        Ramificacion(tabla_padre)
        tabla_padre = SiguienteNodo()

def main():
    print("inicial")
    TablaInicial.Llenar("inicial")
    TablaInicial.setG(0)
    TablaInicial.PrintTorre()
    print("meta")
    Tabla.LlenarTablaMeta()
    Tabla.PrintTablaMeta()
    print(" - - - - - - - - - - - - ")
    print()
    
    Astar()     # Algoritmo de A estrellas
    
    #Tabla.GirarFilaIzquierda(1)
    #Tabla.PrintTorre()
    #Tabla.GirarFilaDerecha(2)
    #Tabla.RotarElOAbajo(0,0)

    #Tabla.RotarElOArriba(1, 0)
    #Tabla.PrintTorre()

    


#Se crea la matriz
colores = ['B','G','Y','R'] 
Filas = 4
Columnas = Filas+1
last_id = 1

    
TablaInicial = Tabla.Tabla(last_id, 0)
TablaMeta = Tabla.Tabla(-1, -1)

lista_visitados = Tabla.ListaDeTablas()
lista_NO_visitados = Tabla.ListaDeTablas()
lista_NO_visitados.Agregar(TablaInicial)    
main()
    
