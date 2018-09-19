
import Tabla as Tabla

#funciones


def CalcularDistancia (iacutal, jactual, idestino, jdestino):
    j = abs(jactual-jdestino) 
    if (j==3):
        j=1
    D = abs(iacutal-idestino) + j
    return D 



def Algoritmo(g):
    Sum=0
    for i in range(Columnas):
        for j in range(Filas):
            #color que queremos sacarle la distancia
            color = Tabla.ObtenerColor(i,j)
            if (color != 'X' or color != 'O' ):
                (idestino,jdestino) = Tabla.CalcularIJdelColorMasCercano(i,j)
                DistanciaCalculada = CalcularDistancia(i, j, idestino, jdestino)
                print (DistanciaCalculada)
                Sum = Sum + DistanciaCalculada
    
    print ((g + (1/20) * Sum))
    #Tabla.GuardarPeso(self, (g + 1/20 * Sum))

    
    pass
def main():
    


    
    Tabla.PrintTorre()
    Algoritmo(1)
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


idnuevo=1
Tabla = Tabla.Tabla(0,idnuevo)




    
main()
    
