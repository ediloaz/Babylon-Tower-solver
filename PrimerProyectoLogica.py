
import Tabla as Tabla

last_id = 1
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
    last_id += 1

def CrearNuevaTablaFila(TablaIntermedia, fila_a_girar):
    AumentarLastID()
    id_padre = TablaIntermedia.GetId() ####
    nueva_tabla = Tabla.Tabla(id_padre, last_id)
    matriz_nueva = TablaIntermedia.NuevaMatrizFilaGiradaIzquierda(fila_a_girar)
    nueva_tabla.DefinirMatriz(matriz_nueva)
    return nueva_tabla


def CreacionDeTablas(TablaIntermedia):
    
    for i in range(5):
        nueva_tabla = CrearNuevaTablaFila(TablaIntermedia, i)
        if (nueva_tabla.EsLaTablaMeta()): ###
            
    
def main():
    


    
    TablaInicial.Llenar("inicial")
    print("inicial")
    TablaInicial.PrintTorre()
    
    Algoritmo(1, TablaInicial)
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


TablaInicial = Tabla.Tabla(last_id, 0)

TablaMeta = Tabla.Tabla(-1, -1)

print("meta")
Tabla.LlenarTablaMeta()
Tabla.PrintTablaMeta()



    
main()
    
