#Se crea la matriz
colores = ['R','G','B','Y'] 
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

    def Quitar(self, Tabla):
        self.lista.remove(Tabla)
        
    def LenLista(self):
        return len(self.lista)
    
    def GetLista(self,i):
        return self.lista[i]
    
    def Pop(self):
        if len(self.lista) > 0:
            return self.lista[-1]
        else:
            print("La lista de NO visitados ya está vacia")
            exit()

    def TablaMenorPeso(self):
        menor_peso    = self.lista[-1].getPeso()
        tabla_escogida = self.lista[-1]
        for tabla in self.lista:
            if (tabla.getPeso() < menor_peso):
                menor_peso    = tabla.getPeso()
                tabla_escogida = tabla
        return tabla_escogida
            
    
    def CompararTabla(self, matriz1, matriz2):
        for i in range(5):
            for j in range(4):
                if matriz1[i][j].color != matriz2[i][j].color:
                    return False
        return True
    
    def Comparar(self, Tabla):
        for tabla_de_lista in self.lista:
##            print("tontera")
##            tabla_de_lista.PrintTorre()
##            Tabla.PrintTorre()
##            print("55'\n\n")
            if self.CompararTabla(tabla_de_lista.tabla,Tabla.tabla):
                return True
        return False

class Tabla(object):
    def __init__(self , idpadre, idnuevo ):
        self.id = idnuevo
        self.idpadre = idpadre
        self.peso = 0
        self.llave = "X"*20
        self.g = 0
        self.movimiento = 0
        
        

    def setMovimiento(self, movimiento):
        self.movimiento = movimiento

    def getMovimiento(self):
        return self.movimiento
    
    def getID(self):
        return self.id
    
    def setID(self, ID):
        self.id = ID
        
    def getIDpadre(self):
        return self.idpadre
    
    def setIDpadre(self, IDpadre):
        self.idpadre = IDpadre

    def getLlave(self):
        return self.llave

    def setLlave(self, nueva_llave):
        self.llave = nueva_llave
    """    
    def getTabla(self):
        return self.tabla
    
    def setTabla(self, matriz):
        self.tabla = matriz
    """
    def getG(self):
        return self.g

    def setG(self, G):
        self.g = G

    def getPeso(self):
        return self.peso

    """
    def EsLaTablaMeta(self):
        texto = ""
        texto1 = ""
        for i in range(5):
            for j in range(4):
                texto += str(self.tabla[i][j].getColor()) + " "
                texto1 += str(TablaMeta.tabla[i][j].getColor()) + " "
        if (texto == texto1):
            print("\n Esta fue la comparacion de la tabla meta: \n",texto,"\n",texto1,"\n")
            return True
        else:
            return False
    """
    def EsLaTablaMeta(self):
        print("\n Esta fue la comparacion de la tabla meta: \n",self.llave,"\n",TablaMeta.llave,"\n")
        if (self.llave == TablaMeta.llave):
            return True
        else:
            return False
    """
    def Llenar(self, tipo):
        #Se llena de datos
        self.tabla[0][0]= celda(self.id, 'O')
        if (tipo == "inicial"):
            for i in range(Columnas-1):
                for j in range(Filas):
                    self.tabla[i+1][j]= celda(self.id, colores[j])  #colores[j]

        elif (tipo == "meta"):
            for i in range(Columnas-1):
                for j in range(Filas):
                    self.tabla[i+1][j]= celda(self.id, colores[j])  #colores[j]
            # 1
            #self.tabla[1][2]= celda(self.id, "Y")  #colores[j]
            #self.tabla[1][0]= celda(self.id, "B")  #colores[j]
            #self.tabla[3][3]= celda(self.id, "R")  #colores[j]
            # 2
            #self.tabla[0][0]= celda(self.id, "X")  #colores[j]
            #self.tabla[0][1]= celda(self.id, "X")  #colores[j]
            #self.tabla[0][2]= celda(self.id, "O")  #colores[j]
            #self.tabla[0][3]= celda(self.id, "X")  #colores[j]
            # 3
            #self.tabla[0][0]= celda(self.id, "R")  #colores[j]
            #self.tabla[4][0]= celda(self.id, "O")  #colores[j]
            # 4
            #self.tabla[1][0]= celda(self.id, "G")  #colores[j]
            #self.tabla[1][1]= celda(self.id, "R")  #colores[j]
            # 5
            self.tabla[1][0]= celda(self.id, "B")  #colores[j]
            self.tabla[1][2]= celda(self.id, "R")  #colores[j]
            
                    # self.tabla[i+1][j]= celda(self.id, colores[(j+2)%4])  #colores[j]
        elif (type(tipo) == list):
            lista_de_colores = tipo
            for i in range(5):
                for j in range(4):
                    self.tabla[i][j]= celda(self.id, lista_de_colores[i*4+j].upper())  #colores[j]
    """
    def Llenar(self,tipo):
        if (tipo == "inicial"):
            self.llave  = "OXXX"
            self.llave += "RGBY"
            self.llave += "RGBY"
            self.llave += "RGBY"
            self.llave += "RGBY"
        elif (tipo == "meta"):
            self.llave  = "OXXX"
            #self.llave += "RGBY"
            self.llave += "GRBY"
            self.llave += "RGBY"
            self.llave += "RGBY"
            self.llave += "RGBY"
        else:
            self.llave  = "XOXX"
            self.llave += "RGBY"
            self.llave += "RGBY"
            self.llave += "RGBY"
            self.llave += "RGBY"
            
    
    # Check the format of Initial table
    """
    def CorrectFormat(self):
        r_color = 0         # it must be 4
        g_color = 0         # it must be 4
        b_color = 0         # it must be 4
        y_color = 0         # it must be 4
        x_color = 0         # it must be 3
        o_color = 0         # it must be 1
        lista_de_colores = []
        for i in range(5):
            temp_lista = []
            for j in range(4):
                temp_lista += [self.tabla[i][j].getColor()]
            lista_de_colores += [temp_lista]
        for row in lista_de_colores:
            r_color += row.count("R")
            g_color += row.count("G")
            b_color += row.count("B")
            y_color += row.count("Y")
            x_color += row.count("X")
            o_color += row.count("O")
        if (r_color == 4 and g_color == 4 and b_color == 4 and
            y_color == 4 and x_color == 3 and o_color == 1):
            tupla = (True, r_color, g_color, b_color, y_color, x_color, o_color)
            return tupla
        else:
            tupla = (False, r_color, g_color, b_color, y_color, x_color, o_color)
            return tupla
    """
    def CorrectFormat(self):
        tupla = (False, 
                self.llave.count("R"),
                self.llave.count("G"),
                self.llave.count("B"),
                self.llave.count("Y"),
                self.llave.count("X"),
                self.llave.count("O"))
        if (tupla[1] == 4 and
            tupla[2] == 4 and
            tupla[3] == 4 and
            tupla[4] == 4 and
            tupla[5] == 3 and
            tupla[6] == 1):
            tupla[0] = True
            return tupla
        else:
            return tupla

    # Conversiones entre posiciones de FILA y STRING
    def NumeroFilaToRangoString(self, numero):
        if (numero == 0):
            return (0,3)
        elif (numero == 1):
            return (4,7)
        elif (numero == 2):
            return (8,11)
        elif (numero == 3):
            return (12,15)
        elif (numero == 4):
            return (16,19)
        else:
            print("ERROR EN NumeroFilaToRangoString()")
            exit()
    def PosicionStringToPosicionMatriz(self, numero):
        i = 0
        while n>3:
            i += 1
            n  = n-4
        j = n
        return (i,j)
    def (self, i, j):
        return (i*4+j)
    
     
    #Rotar Filas
    #solo se gira un movimiento en las filas
    """
    def rotate(self,l, n):
        return l[n:] + l[:n]
    """
    def rotate(self,string, n):
        return string[n:] + string[:n]
    """
    def GirarFilaIzquierda(self,NumeroFilaGirar):
        lista = self.tabla[NumeroFilaGirar]
        self.tabla[NumeroFilaGirar] = self.rotate(lista, 1)
    """
    def GirarFilaIzquierda(self, numeroFilaGirar):
        rango = NumeroFilaToRangoString(numeroFilaGirar)
        fila = self.llave[rango[0]:(rango[1]+1)]
        fila = self.rotate(fila, 1)
        self.llave[rango[0]:(rango[1]+1)] = fila

    """
    def GirarFilaDerecha(self , NumeroFilaGirar):
        lista = self.tabla[NumeroFilaGirar]
        self.tabla[NumeroFilaGirar] = self.rotate(lista, 3)
    """
    def GirarFilaDerecha(self, numeroFilaGirar):
        rango = NumeroFilaToRangoString(numeroFilaGirar)
        fila = self.llave[rango[0]:(rango[1]+1)]
        fila = self.rotate(fila, 3)
        self.llave[rango[0]:(rango[1]+1)] = fila
    
    
    #RotarColumnas
    """
    def PosO(self):
        for i in range(Columnas):
            for j in range(Filas):
                if (self.tabla[i][j].getColor()=='O'):
                    return (i,j)
    """
    def PosicionO(self):
        return self.llave.find("O")
    """
    def RotarElOArriba(self, PosicionI, PosicionJ):
        if (PosicionI == 0 ):
            return False
        elif self.tabla[PosicionI-1][PosicionJ].getColor() == "X":
            return False
        else:
            color = self.tabla[PosicionI][PosicionJ]
            self.tabla[PosicionI][PosicionJ] = self.tabla[PosicionI-1][PosicionJ]
            self.tabla[PosicionI-1][PosicionJ] = color
            return True
    def RotarElOAbajo(self, PosicionI, PosicionJ):
        if (PosicionI == Columnas-1):
            return False
        else:
            color = self.tabla[PosicionI][PosicionJ]
            self.tabla[PosicionI][PosicionJ] = self.tabla[PosicionI+1][PosicionJ]
            self.tabla[PosicionI+1][PosicionJ] = color
            return True
    """
    def RotarElOArriba(self):
        posO = self.PosicionO()
        (i,j) = PosicionStringToPosicionMatriz(posO)
        if (i == 0) or self.llave[posO%4]=="X":
            return False
        pos_destino = PosicionMatrizToPosicionString(i-1,j)
        self.llave[posO] = self.llave[pos_destino]
        self.llave[pos_destino] = "O"

    def RotarElOAbajo(self):
        posO = self.PosicionO()
        (i,j) = PosicionStringToPosicionMatriz(posO)
        if (i == 0) or self.llave[posO%4]=="X":
            return False
        pos_destino = PosicionMatrizToPosicionString(i+1,j)
        self.llave[posO] = self.llave[pos_destino]
        self.llave[pos_destino] = "O"

    
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

        
    def PrintTorre(self):
        for i in range(5):
            texto = ""
            for j in range(4):
                texto += str(self.tabla[i][j].getColor()) + " "
            print(texto)
        print()

    def PrintTorreDetallada(self):
        print("ID: " + str(self.id) )
        print("Padre: " + str(self.idpadre) )
        print("Valor g: " + str(self.g) )
        for i in range(5):
            texto = "|"
            for j in range(4):
                texto += str(self.tabla[i][j].getColor()) + " "
            print(texto + "|")
        print("Peso: " + str(self.peso) )
        
    
        
    def ObtenerColor(self,i,j):
       return self.tabla[i][j].getColor()
        
        
    def GuardarPeso(self, peso):
        self.peso = float("{0:.2f}".format(peso))

        

# ID para tabla inicial: 0
# ID del padre: -1 (no tiene)
TablaInicial = Tabla(-1, 0)
# ID para tabla META: -2
# ID del padre: -1 (no tiene)
TablaMeta = Tabla(-1, -2)

def getTablaInicial():
    global TablaInicial
    return TablaInicial

def setTablaInicial(tabla):
    global TablaInicial
    TablaInicial = tabla

def getTablaMeta():
    global TablaMeta
    return TablaMeta

def setTablaMeta(tabla):
    global TablaMeta
    TablaMeta = tabla

def LlenarTablaMeta():
    TablaMeta.Llenar("meta")

def PrintTablaMeta():
    TablaMeta.PrintTorre()

def PrintTablaMetaDetallada():
    TablaMeta.PrintTorreDetallada()




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
# 12: Espacio en blanco hacia abajo
#
