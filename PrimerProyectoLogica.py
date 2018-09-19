
import Tabla as Tabla
from copy import deepcopy


#funciones


def CalcularDistancia (iacutal, jactual, idestino, jdestino):
    j = abs(jactual-jdestino) 
    if (j==3):
        j=1
    D = abs(iacutal-idestino) + j
    return D 



def Algoritmo(g, tabla):
    Sum=0
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
    
    print ((g + (1/20) * Sum))
    #Tabla.GuardarPeso(self, (g + 1/20 * Sum))
    return 

def AumentarLastID():
    global last_id
    last_id += 1


def CrearNuevaTablaFila(TablaIntermedia, fila_a_girar):
    AumentarLastID()
    id_padre = TablaIntermedia.GetId() 
    nueva_tabla = Tabla.Tabla(id_padre, last_id)
    nueva_tabla.Llenar("Inicial")
    
    TablaIntermedia.GirarFilaIzquierda(fila_a_girar)
    TablaIntermedia.PrintTorre()
    nueva_tabla = TablaIntermedia.CopiarTabla(nueva_tabla)
    #matriz = TablaIntermedia.getTabla()
    #nueva_tabla.setTabla(matriz)
    TablaIntermedia.GirarFilaDerecha(fila_a_girar)
    
    print("se reci")
    nueva_tabla.PrintTorre()
    return nueva_tabla

# Saca de la lista de no visitados a una tabla y la mete en la de visitados. retorna dicha tabla
def SiguienteTabla():
    pass

def NuevaTablaIzquierda(TablaPadre, numero_fila):
    nueva_tabla = deepcopy(TablaPadre)
    nueva_tabla.setID(last_id)
    nueva_tabla.setIDpadre(TablaPadre.getID())
    nueva_tabla.GirarFilaIzquierda(numero_fila)
    if lista_visitados.Comparar(nueva_tabla):
        return False
    else:
        lista_visitados.Agregar(nueva_tabla)
        return nueva_tabla

def CreacionDeTablas(TablaPadre):
    # Hacia derecha
    for i in range(5):
        nueva_tabla = NuevaTablaIzquierda(TablaPadre, i)
        if (nueva_tabla == False):
            print("se encontro una igual")
        else:
            #Algoritmo(1, nueva_tabla)
            pass
        
        print("nueva")
        nueva_tabla.PrintTorre()
        AumentarLastID
"""
    for i in range(5):
        nueva_tabla = CrearNuevaTablaFila(TablaIntermedia, i)
        if (nueva_tabla.EsLaTablaMeta() ):
            Finalizado(tabla)
        elif (lista_visitados.Comparar(nueva_tabla)):
            print("se encontro una igual")
        else:
            Algoritmo(1, nueva_tabla)
        input()
        
"""            
            
def Finalizado(tabla):
    pass

def main():
    
    print("inicial")
    TablaInicial.Llenar("inicial")   
    TablaInicial.PrintTorre()
    
    
    print("meta")
    Tabla.LlenarTablaMeta()
    Tabla.PrintTablaMeta()

    CreacionDeTablas(TablaInicial)
    
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
lista_visitados.Agregar(TablaInicial)

    
main()
    
