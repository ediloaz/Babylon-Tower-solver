import numpy as np

#funciones

def PrintTorre():
    for i in range(Columnas):
        print (Torre[i])
    print ('\n  -------  \n')
        
#Rotar Filas
#solo se gira un movimiento en las filas
def rotate(l, n):
    return l[n:] + l[:n]

def GirarFilaIzquierda(NumeroFilaGirar):
    lista = Torre[NumeroFilaGirar]
    Torre[NumeroFilaGirar] = rotate(lista, 1)

def GirarFilaDerecha(NumeroFilaGirar):
    lista = Torre[NumeroFilaGirar]
    Torre[NumeroFilaGirar] = rotate(lista, Filas-1)
    
#RotarColumnas
        
def PosO():
    i1=5
    j=5
    for i in range(Columnas):
        try:
            j = (Torre[0].index('O'))
            i1=i
        except ValueError:
            print ('a')
        
    print (i1,j)


def RotarElOArriba(PosicionI, PosicionJ):
    if (PosicionI == 0 or Torre[PosicionI][PosicionJ] != 'O' ):
        print ('Error')
    else:
        color = Torre[PosicionI][PosicionJ]
        
        Torre[PosicionI][PosicionJ] = Torre[PosicionI-1][PosicionJ]
        
        Torre[PosicionI-1][PosicionJ] = color

def RotarElOAbajo(PosicionI, PosicionJ):
    if (PosicionI == Columnas-1 or Torre[PosicionI][PosicionJ] != 'O' ):
        print ('Error')
    else:
        color = Torre[PosicionI][PosicionJ]
        
        Torre[PosicionI][PosicionJ] = Torre[PosicionI+1][PosicionJ]
        
        Torre[PosicionI+1][PosicionJ] = color

#Se crea la matriz
colores = ['A','B','N','R'] 
Filas = 4
Columnas = Filas+1
Torre = []


for i in range(Columnas):
        a = ['x'] * Filas
        Torre.append(a)

#Se llena de datos
Torre[0][0]= 'O'
for i in range(Columnas-1):
    for j in range(Filas):
        Torre[i+1][j]= colores[j]

PrintTorre()

GirarFilaIzquierda(1)
PrintTorre()
GirarFilaDerecha(2)
#RotarElOAbajo(0,0)

#RotarElOArriba(1, 0)
PrintTorre()

#se agrega el espacio donde entra una bola
Extra = 'E'


