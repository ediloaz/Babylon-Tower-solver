#Se crea la matriz
colores = ['B','G','Y','R'] 
Filas = 4
Columnas = Filas+1

class celda(object):
    def __init__(self , idtabla, color ):
        self.idtabla = idtabla
        self.color = color
        self.distaciaColumna = 99
        self.distaciaFila = 99

    def getColor(self):
        return self.color

class Tabla(object):
    def __init__(self , idpadre, idnuevo ):
        self.id = idnuevo
        self.idpadre = idpadre
        self.peso = 0
        self.tabla = []
        
        for i in range(Columnas):
            a = [celda(self.id, 'X')] * Filas
            self.tabla.append(a)

        #Se llena de datos
        self.tabla[0][0]= celda(self.id, 'O') 
        for i in range(Columnas-1):
            for j in range(Filas):
                self.tabla[i+1][j]= celda(self.id, colores[j])  #colores[j]


    
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
            texto = ""
            for j in range(4):
                texto += str(self.tabla[i][j].getColor()) + " "
            print(texto)
        print ('\n  -------  \n')
        
    def ObtenerColor(self,i,j):
       #self.tabla
        print ('\n  -------  \n')
        
    def GuardarPeso(self, peso):
        self.peso = peso
