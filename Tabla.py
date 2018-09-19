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

    def setColor(self, color):
        self.color = color
     

class ListaDeTablas(object):
    def __init__(self):
         self.lista = []
         
    def Agregar(self, Tabla):
        self.lista.append(Tabla)

    def Comparar(self, Tabla):
        for tabla_de_lista in self.lista:
            print("list")
            tabla_de_lista.PrintTorre()
            print("nueva")
            Tabla.PrintTorre()
            print()
            if (tabla_de_lista.tabla == Tabla.tabla):
                return True
        return False

class Tabla(object):
    def __init__(self , idpadre, idnuevo ):
        self.id = idnuevo
        self.idpadre = idpadre
        self.peso = 0
        self.tabla = []
        self.g = 0
        
        
        for i in range(Columnas):
            a = [celda(self.id, 'X')] * Filas
            self.tabla.append(a)


    def getID(self):
        return self.id
    def setID(self, ID):
        self.id = ID
    def getIDpadre(self):
        return self.id
    def setIDpadre((self, ID):
        self.id = ID
    

    def getTabla(self):
        return self.tabla
    
    def setTabla(self, matriz):
        self.tabla = matriz
        
    def EsLaTablaMeta(self):
        if (TablaMeta.tabla == self.tabla):
            return True
        else:
            return False
    
    def Llenar(self, tipo):
        #Se llena de datos
        self.tabla[0][0]= celda(self.id, 'O')
        if (tipo == "inicial"):
            for i in range(Columnas-1):
                for j in range(Filas):
                    self.tabla[i+1][j]= celda(self.id, colores[j])  #colores[j]

        elif (tipo == "final"):
            for i in range(Columnas-1):
                for j in range(Filas):
                    self.tabla[i+1][j]= celda(self.id, colores[(j+2)%4])  #colores[j]
        
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
    
    
    def CalcularDistancia (self, iacutal, jactual, idestino, jdestino):
        j = abs(jactual-jdestino) 
        if (j==3):
            j=1
        D = abs(iacutal-idestino) + j
        return D


    def CalcularIJdelColorMasCercano(self, i1,j1):
        
        ColorBuscando = self.tabla[i1][j1].getColor()
        Distancia = 99
        iFinal = 0
        jFinal = 0
        for i in range(Columnas):
            for j in range(Filas):
                # Color de la tabla meta
                ColorActual = TablaMeta.tabla[i][j].getColor()
                if ( ColorBuscando == ColorActual ):
                    DistanciaActual = self.CalcularDistancia (i1, j1, i, j)
                    if (DistanciaActual < Distancia ):
                        Distancia = DistanciaActual
                        iFinal = i
                        jFinal = j
                    
        return (iFinal,jFinal)

    def CopiarTabla(self, Fuente):
        for i in range(5):
            for j in range(4):
                print(222222, Fuente.tabla[i][j].color)
                self.tabla[i][j].color = Fuente.tabla[i][j].color
                print(1111111, self.tabla[i][j].color)
        
    def PrintTorre(self):
        for i in range(5):
            texto = ""
            for j in range(4):
                texto += str(self.tabla[i][j].getColor()) + " "
            print(texto)
        print ('\n  -------  \n')
        
    def ObtenerColor(self,i,j):
       return self.tabla[i][j].getColor()
        
        
    def GuardarPeso(self, peso):
        self.peso = peso

# definir id y idpadre

TablaMeta = Tabla(-1,9999999999)

def LlenarTablaMeta():
    TablaMeta.Llenar("final")

def PrintTablaMeta():
    TablaMeta.PrintTorre()


