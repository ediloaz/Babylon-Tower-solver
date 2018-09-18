#Se crea la matriz
colores = ['B','G','Y','R'] 
Filas = 4
Columnas = Filas+1

class celda(object):
    def __init__(self , idtabla ):
        self.id
        self.idtabla
        self.color
        self.distaciaColumna
        self.distaciaFila

class Tabla(object):
    def __init__(self , idpadre, idnuevo ):
        self.id = idnuevo
        self.idpadre = idpadre
        self.peso = 4
        self.tabla = []
        
        for i in range(Columnas):
            a = ['x'] * Filas
            self.tabla.append(a)

        #Se llena de datos
        self.tabla[0][0]= 'O'
        for i in range(Columnas-1):
            for j in range(Filas):
                self.tabla[i+1][j]= colores[j]


    
    #Rotar Filas
    #solo se gira un movimiento en las filas
    def rotate(self,l, n):
        return l[n:] + l[:n]

    def GirarFilaIzquierda(self,NumeroFilaGirar):
        lista = self.tabla[NumeroFilaGirar]
        self.tabla[NumeroFilaGirar] = self.rotate(lista, 1)
        

    def GirarFilaDerecha(self , NumeroFilaGirar):
        lista = self.tabla[NumeroFilaGirar]
        self.tabla[NumeroFilaGirar] = self.rotate(lista, 3)
        
        
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


    def RotarElOArriba(self, PosicionI, PosicionJ):
        if (PosicionI == 0 or self.tabla[PosicionI][PosicionJ] != 'O' ):
            print ('Error')
        else:
            color = self.tabla[PosicionI][PosicionJ]
            self.tabla[PosicionI][PosicionJ] = self.tabla[PosicionI-1][PosicionJ]
            self.tabla[PosicionI-1][PosicionJ] = color

    def RotarElOAbajo(self, PosicionI, PosicionJ):
        if (PosicionI == Columnas-1 or self.tabla[PosicionI][PosicionJ] != 'O' ):
            print ('Error')
        else:
            color = self.tabla[PosicionI][PosicionJ]
            
            self.tabla[PosicionI][PosicionJ] = self.tabla[PosicionI+1][PosicionJ]
            
            self.tabla[PosicionI+1][PosicionJ] = color
    def PrintTorre(self):
        for i in range(5):
            print (self.tabla[i])
        print ('\n  -------  \n')


