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

# Global variables/constants
LAST_ID = 1
SOLUCION = []       # AQUÍ VAN LAS TABLAS DE LA SOLUCIÓN
ID_SOLUCION = 1

# Recibe
def RecibirInformacionDesdeInterfaz(initial_table, goal_table):
    ResetLastID()
    Tabla.setTablaInicial(initial_table)
    Tabla.setTablaMeta(goal_table)
    # Aquí llama a main() y main() retorna UNA lista:
    #   1 => Las tablas con la solución
    # lista = main()
    initial_table.setMovimiento(1)
    goal_table.setMovimiento(3)
    global SOLUCION
    tabla1 = deepcopy(initial_table)
    tabla1.setMovimiento(1)
    tabla2 = deepcopy(goal_table)
    tabla2.setMovimiento(2)
    tabla3 = deepcopy(initial_table)
    tabla3.setMovimiento(3)
    tabla4 = deepcopy(goal_table)
    tabla4.setMovimiento(4)
    tabla5 = deepcopy(initial_table)
    tabla5.setMovimiento(5)
    tabla6 = deepcopy(goal_table)
    tabla6.setMovimiento(6)    
    SOLUCION = [initial_table, tabla1, tabla2, tabla3, tabla4, tabla5, tabla6, goal_table]
    # end -- 

def EnviarInformacionHaciaInterfaz():
    global SOLUCION
    return SOLUCION

def EnviarSiguienteTablaSolucion():
    global SOLUCION, ID_SOLUCION
    ID_SOLUCION += 1
    tabla = SOLUCION[ID_SOLUCION]
    return (tabla, ID_SOLUCION)

def EnviarAnteriorTablaSolucion():
    global SOLUCION, ID_SOLUCION
    ID_SOLUCION -= 1
    tabla = SOLUCION[ID_SOLUCION]
    return (tabla, ID_SOLUCION)

def LargoSolucion():
    global SOLUCION
    return len(SOLUCION)

def getIdSolucion():
    global ID_SOLUCION
    return ID_SOLUCION






def CalcularDistancia (iacutal, jactual, idestino, jdestino):
    j = abs(jactual-jdestino) 
    if (j==3):
        j=1
    D = abs(iacutal-idestino) + j
    return D 

# Antes llamada "Algoritmo"
def Peso(tabla):
    Sum = 0
    g = tabla.getG()            # Guarda el g (acumulado) de la tabla
    for i in range(5):          # Filas
        for j in range(4):      # Columnas
            color = tabla.ObtenerColor(i,j)
            (idestino,jdestino) = tabla.CalcularIJdelColorMasCercano(i,j)   # REVISAR NO ESTÁ TRABAJANDO BIEN
                                                                                                                    # Dos celdas distintas no pueden escoger la misma celda destino
            DistanciaCalculada = CalcularDistancia(i, j, idestino, jdestino)
            Sum += DistanciaCalculada
    peso = (g + (1/20) * Sum)
    tabla.GuardarPeso(peso)
    

def AumentarLastID():
    global LAST_ID
    LAST_ID += 1

def LastID():
    global LAST_ID
    return LAST_ID

def ResetLastID():
    global LAST_ID
    LAST_ID = 1
    
def Largo(lista):
    return len(lista.lista)

def Visitado(Tabla):
    lista_NO_visitados.Quitar(Tabla)
    lista_visitados.Agregar(Tabla)


# Saca de la lista de no visitados a una tabla y la mete en la de visitados. retorna dicha tabla
# Busca en la lista de NO visitados, el que tiene peso menor. Y lo devuelve como la tabla Padre
# quitandolo de dicha lista y metiendolo en la lista de SI visitados
def SiguienteNodo():
    # Ahorita solo coge el último
    TablaMenorPeso = lista_NO_visitados.TablaMenorPeso()
    print("\nTabla escogida como la de menor PESO:")
    TablaMenorPeso.PrintTorreDetallada()
    # Visitado(TablaMenorPeso)      # Este visitado se hace al terminar la función "Ramificacion"
    return TablaMenorPeso

def NuevaTablaIzquierda(TablaPadre, numero_fila):
    nueva_tabla = deepcopy(TablaPadre)
    nueva_tabla.setID(LastID())                                      # Asigna ID
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
    nueva_tabla.setID(LastID())                                      # Asigna ID
    nueva_tabla.setIDpadre(TablaPadre.getID())      # Asigna ID padre
    nueva_tabla.setG(TablaPadre.getG()+1)               # Asigna g
    nueva_tabla.GirarFilaDerecha(numero_fila)
    if lista_NO_visitados.Comparar(nueva_tabla):       # ¿Está visitado?
        return False
    else:
        lista_NO_visitados.Agregar(nueva_tabla)            # Se agrega a la lista de visitados
        AumentarLastID()
        return nueva_tabla

def NuevaTablaArriba(TablaPadre, numero_fila):
    nueva_tabla = deepcopy(TablaPadre)
    nueva_tabla.setID(LastID())                                      # Asigna ID
    nueva_tabla.setIDpadre(TablaPadre.getID())      # Asigna ID padre
    nueva_tabla.setG(TablaPadre.getG()+1)               # Asigna g
    (i,j) = TablaPadre.PosO()
    nueva_tabla.RotarElOArriba(i,j)
    if lista_NO_visitados.Comparar(nueva_tabla):       # ¿Está visitado?
        return False
    else:
        lista_NO_visitados.Agregar(nueva_tabla)            # Se agrega a la lista de visitados
        AumentarLastID()
        return nueva_tabla


def NuevaTablaAbajo(TablaPadre, numero_fila):
    nueva_tabla = deepcopy(TablaPadre)
    nueva_tabla.setID(LastID())                                      # Asigna ID
    nueva_tabla.setIDpadre(TablaPadre.getID())      # Asigna ID padre
    nueva_tabla.setG(TablaPadre.getG()+1)               # Asigna g
    (i,j) = TablaPadre.PosO()
    nueva_tabla.RotarElOAbajo(i,j)
    if lista_NO_visitados.Comparar(nueva_tabla):       # ¿Está visitado?
        return False
    else:
        lista_NO_visitados.Agregar(nueva_tabla)            # Se agrega a la lista de visitados
        AumentarLastID()
        return nueva_tabla


# Crea a partir de una tabla las siguientes 12 tablas.
def Ramificacion(TablaPadre):
    
    # Hacia izquierda
    print("- - - - - - - - - - - - - - - - - - ")
    print("Con giro a la izquierda")
    for i in range(5):
        nueva_tabla = NuevaTablaIzquierda(TablaPadre, i)
        if (nueva_tabla == False):
            print("Se encontro una igual. Se omitió la tabla, se cierra el nodo" )
        else:
            nueva_tabla.setMovimiento(1+i)  # Va del 1 al 5
            Peso(nueva_tabla)           # Asigna el peso a la tabla
            print("Nueva tabla: ", i+1)
            print('\n')
            nueva_tabla.PrintTorreDetallada()
    print("Largo de tabla_visitados: ", Largo(lista_visitados))
    print("Largo de tabla_NO_visitados: ", Largo(lista_NO_visitados))
    
            
    # Hacia derecha
    print("- - - - - - - - - - - - - - - - - - ")
    print("Con giro a la derecha")
    for i in range(5):
        nueva_tabla = NuevaTablaDerecha(TablaPadre, i)
        if (nueva_tabla == False):
            print("Se encontro una igual o no es posible hacer el movimiento. Se omitió la tabla, se cierra el nodo" )
        else:
            nueva_tabla.setMovimiento(6+i) # Va del 6 al 10
            Peso(nueva_tabla)       # Asigna el peso a la tabla
            print("Nueva tabla: ", i+6)
            nueva_tabla.PrintTorreDetallada()
    print("Largo de tabla_visitados: ", Largo(lista_visitados))
    print("Largo de tabla_NO_visitados: ", Largo(lista_NO_visitados))


    # Hacia Arriba
    print("- - - - - - - - - - - - - - - - - - ")
    print("Con giro hacia arriba")
    nueva_tabla = NuevaTablaArriba(TablaPadre, i)
    if (nueva_tabla == False):
        print("Se encontro una igual o no es posible hacer el movimiento. Se omitió la tabla, se cierra el nodo" )
    else:
        nueva_tabla.setMovimiento(11)   # 11: Espacio en blanco hacia arriba
        Peso(nueva_tabla)           # Asigna el peso a la tabla
        print("Nueva tabla: ", i+1)
        print('\n')
        nueva_tabla.PrintTorreDetallada()
    print("Largo de tabla_visitados: ", Largo(lista_visitados))
    print("Largo de tabla_NO_visitados: ", Largo(lista_NO_visitados))


    # Hacia Abajo
    print("- - - - - - - - - - - - - - - - - - ")
    print("Con giro hacia abajo")
    nueva_tabla = NuevaTablaAbajo(TablaPadre, i)
    if (nueva_tabla == False):
        print("Se encontro una igual. Se omitió la tabla, se cierra el nodo" )
    else:
        nueva_tabla.setMovimiento(12) # 12: Espacio en blanco hacia abajo
        Peso(nueva_tabla)           # Asigna el peso a la tabla
        print("Nueva tabla: ", i+1)
        print('\n')
        nueva_tabla.PrintTorreDetallada()
    print("Largo de tabla_visitados: ", Largo(lista_visitados))
    print("Largo de tabla_NO_visitados: ", Largo(lista_NO_visitados))


    #Ya se usó, entonces se saca de la lista de NO-visitadas
    Visitado(TablaPadre)

    
    
            
def Finalizado(Tabla):
    if(Tabla.EsLaTablaMeta() ):
        return True
    return False

# Solo ramifica (12 ramas de tablas nuevas) a partir de TABLAPADRE y luego escoge la
# siguiente TABLAPADRE a partir de la lista_NO_visitados
def A_Estrella():
    tabla_padre = Tabla.TablaInicial
    while True:
        print("Pasada por el While True")
        Ramificacion(tabla_padre)
        tabla_padre = SiguienteNodo()
        if (Finalizado(tabla_padre)==True):
            break
        input("\n\n Pasada completa, ENTER para continuar \n\n")

def main():
    print("Tabla inicial")
    Tabla.TablaInicial.Llenar("inicial")
    Tabla.TablaInicial.setG(0)
    Tabla.TablaInicial.PrintTorreDetallada()
    print("Tabla meta")
    Tabla.LlenarTablaMeta()
    Tabla.PrintTablaMetaDetallada()
    print(" - - - - - - - - - - - - ")
    print()
    lista_NO_visitados.Agregar(Tabla.TablaInicial)
    A_Estrella()     # Algoritmo de A estrellas
    print ("Se encontro Resultado")
    # end line -    



lista_visitados = Tabla.ListaDeTablas()
lista_NO_visitados = Tabla.ListaDeTablas()


# main()        # DESCOMENTAR PARA HACER PRUEBAS LOCALES
    



# Códigos para cada movimiento
#
# 1: Giro a la izquierda, fila 1
# 2: Giro a la izquierda, fila 2
# 3: Giro a la izquierda, fila 3
# 4: Giro a la izquierda, fila 4
# 5: Giro a la izquierda, fila 5
# 6: Giro a la derecha, fila 1
# 7: Giro a la derecha, fila 2
# 8: Giro a la derecha, fila 3
# 9: Giro a la derecha, fila 4
# 10: Giro a la derecha, fila 5
# 11: Espacio en blanco hacia arriba
# 12: 
#
