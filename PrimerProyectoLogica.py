import numpy as np
import Tabla as Tabla
#funciones


        


def Algoritmo():
    #Formula D = (abs(i-i) + abs(j-j) if j==3 then j=1)
    #g + 1/20 * Sum(D)
    pass
def main():
    


    
    Tabla.PrintTorre()

    Tabla.GirarFilaIzquierda(1)
    Tabla.PrintTorre()
    Tabla.GirarFilaDerecha(2)
    #Tabla.RotarElOAbajo(0,0)

    #Tabla.RotarElOArriba(1, 0)
    Tabla.PrintTorre()

    #se agrega el espacio donde entra una bola
    Extra = 'E'


#Se crea la matriz
colores = ['B','G','Y','R'] 
Filas = 4
Columnas = Filas+1


idnuevo=1
Tabla = Tabla.Tabla(0,idnuevo)



    
main()
