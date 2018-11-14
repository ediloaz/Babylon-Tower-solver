# File of components for PyGame
#   write here the components
#
# For create big text (doom effect): https://www.messletters.com/en/big-text/
# 

import pygame, sys
from pygame.locals import *
from pygame import *
import tkinter as tk
from tkinter import filedialog
import Tabla as Tabla
import CSV_Manager as csv
import Controller as Controller


# Global variables/constants
stage = 0
# INSTRUCTIONS = ["asd","qwe","swqas","fasd","21ew"]
# LENINSTRUCTIONS = Controller.LongSolution()
# Contains all tables of the solution
SOLUTION = []
id_SOLUTION = 0

def hex2rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    rgb_code = tuple(int(hex_code[i:i+2], 16) for i in (0, 2 ,4))
    return rgb_code;

def setStage(p_stage):
    global stage
    stage = p_stage

def NextStage():
    global stage
    stage = Stage()+1

def Stage():
    global stage
    return stage

def Stage2():
    global SOLUTION, id_SOLUTION
    id_SOLUTION = 0
    initial_tower.SaveDataToInitialTable()
    goal_tower.SaveDataToGoalTable()
    SOLUTION = Controller.SendTablesToLogic(Tabla.getTablaInicial(), Tabla.getTablaMeta())

def NextTableSolution():
    global SOLUTION, id_SOLUTION
    id_SOLUTION += 1
    return (SOLUTION[id_SOLUTION], id_SOLUTION)

def PreviousTableSolution():
    global SOLUTION, id_SOLUTION
    id_SOLUTION -= 1
    return (SOLUTION[id_SOLUTION], id_SOLUTION)

def ActualTableSolution():
    global SOLUTION, id_SOLUTION
    return (SOLUTION[id_SOLUTION], id_SOLUTION)

def LenSolution():
    global SOLUTION
    return len(SOLUTION)

def getMessage(code):
    if (code == 0):
        return "this is the initial table"
    elif (code == 1):
        return "turn LEFT the row 1"
    elif (code == 2):
        return "turn LEFT the row 2"
    elif (code == 3):
        return "turn LEFT the row 3"
    elif (code == 4):
        return "turn LEFT the row 4"
    elif (code == 5):
        return "turn LEFT the row 5"
    elif (code == 6):
        return "turn RIGHT the row 1"
    elif (code == 7):
        return "turn RIGHT the row 2"
    elif (code == 8):
        return "turn RIGHT the row 3"
    elif (code == 9):
        return "turn RIGHT the row 4"
    elif (code == 10):
        return "turn RIGHT the row 5"
    elif (code == 11):
        return "turn EMPTY SPACE to UP"
    elif (code == 12):
        return "turn EMPTY SPACE to DOWN"
    elif (code == 13):
        return "this is the goal table"
    else:
        print("\n\n\n " + str(code) + "\n\n\n ")
        return "nothing, nothing :)"

    
##  ______         _    _                   _____  _                  
##  | ___ \       | |  | |                 /  __ \| |                 
##  | |_/ / _   _ | |_ | |_   ___   _ __   | /  \/| |  __ _  ___  ___ 
##  | ___ \| | | || __|| __| / _ \ | '_ \  | |    | | / _` |/ __|/ __|
##  | |_/ /| |_| || |_ | |_ | (_) || | | | | \__/\| || (_| |\__ \\__ \
##  \____/  \__,_| \__| \__| \___/ |_| |_|  \____/|_| \__,_||___/|___/                                                                                                            
##
## 
class Button(object):
    def __init__(self, position, type_of):

        # Definition: set of images
        self._images = self.DefineImages(type_of)

        # Definition: Size and Pos as object's variable
        self._size = self._images["normal"].get_rect().size
        width = position[0]
        height = position[1]                        # 
        self._position = (width, height)
        self._type_of = type_of
        self._button_active = False
        
        # Definition: Position and Size of Component
        self._rect = pygame.Rect(self._position,  self._size)
        
        # Initial State
        self._index = "normal"

        # Draw the component
        pygame.display.set_mode(self._images["normal"].get_rect().size,0,32)

        # Convert from images to objects
        self._images["normal"].convert()
        self._images["hover"].convert()
        self._images["active"].convert()

    def GetWidth(self, image):
        return image.get_rect().size[0]

    def GetHeight(self, image):
        return image.get_rect().size[1]

    def GetNewDimensions(self, image):
        height_destiny = 45             # Define the HEIGHT size
        width_source = self.GetWidth(image)
        height_source = self.GetHeight(image)
        width_destiny = width_source*height_destiny/height_source
        size_destiny = (int(width_destiny), int(height_destiny))
        return size_destiny
        
    def LoadImage(self, path):
        image = pygame.image.load(path)
        return image

    def DefineImages(self, text):
        if text == "accept":
            dictionary = {
                "normal" : self.LoadImage("./images/buttons/button_accept_normal.png"),
                "hover" : self.LoadImage("./images/buttons/button_accept_hover.png"),
                "active" : self.LoadImage("./images/buttons/button_accept_active.png"),
                "check" : self.LoadImage("./images/buttons/check_towers.png")
                }
        elif text == "upload":
            dictionary = {
                "normal" : self.LoadImage("./images/buttons/button_upload_normal.png"),
                "hover" : self.LoadImage("./images/buttons/button_upload_hover.png"),
                "active" : self.LoadImage("./images/buttons/button_upload_active.png")
                }
        elif text == "save":
            dictionary = {
                "normal" : self.LoadImage("./images/buttons/button_save_normal.png"),
                "hover" : self.LoadImage("./images/buttons/button_save_hover.png"),
                "active" : self.LoadImage("./images/buttons/button_save_active.png")
                }
        elif text == "again":
            dictionary = {
                "normal" : self.LoadImage("./images/buttons/button_again_normal.png"),
                "hover" : self.LoadImage("./images/buttons/button_again_hover.png"),
                "active" : self.LoadImage("./images/buttons/button_again_active.png")
                }
        elif text == "arrow_left":
            dictionary = {
                "normal" : self.LoadImage("./images/buttons/arrow_left_normal.png"),
                "hover" : self.LoadImage("./images/buttons/arrow_left_hover.png"),
                "active" : self.LoadImage("./images/buttons/arrow_left_active.png")
                }
        elif text == "arrow_right":
            dictionary = {
                "normal" : self.LoadImage("./images/buttons/arrow_right_normal.png"),
                "hover" : self.LoadImage("./images/buttons/arrow_right_hover.png"),
                "active" : self.LoadImage("./images/buttons/arrow_right_active.png")
                }
        else:
            print("Sucedió un error del sistema")
            exit()
        return dictionary

    
    def draw(self, screen):
        if (self._type_of == "arrow_right" and (ActualTableSolution()[1]+2 > LenSolution())): # last 7 y showing 8
        #if (self._type_of == "arrow_right" and Controller.getIdSolucion() > (LENINSTRUCTIONS-2)):
            pass
        #elif (self._type_of == "arrow_left" and Controller.getIdSolucion() < 2):
        elif (self._type_of == "arrow_left" and (ActualTableSolution()[1] < 1)):    # first 0 showing 1
            pass
        elif (self._type_of == "accept" ):
            initial_tower.SaveDataToInitialTable()
            goal_tower.SaveDataToGoalTable()
            if (Tabla.TablaInicial.CorrectFormat()[0]==False or Tabla.TablaMeta.CorrectFormat()[0]==False):
                screen.blit(self._images["check"], self._rect)
            else:
                screen.blit(self._images[self._index], self._rect)
        else:
            screen.blit(self._images[self._index], self._rect)

    def ChooseFile(self):
        root = tk.Tk()
        root.withdraw()
        try:
            file_path = filedialog.askopenfilename(filetypes=(("Babylon files", "*.by"),("All files", "*.*") ))
            csv_object = csv.CSV_Manager()
            answer = csv_object.LoadCSV(file_path)
            print("answer: ",answer)
            if (answer == 0):   ## Worked
                print("Definimos estas nuevas tablas:")
                initial_tower.DefineBalls(csv_object.getInitialTable())
                goal_tower.DefineBalls(csv_object.getGoalTable())
                print("Hasta acá")
            elif (answer == -1):
                pass
            elif (answer == -2):
                print("The path is wrong... I will close it", file_path)
                # exit()
        except:
            pass
        root.destroy()

    def Accept(self):
        setStage(2)

    def ListToString(self):
        global SOLUTION
        text =  "Starting from the initial table, \n"
        text += "these are the movements:\n"
        print(SOLUTION)
        print(SOLUTION[0])
        print(SOLUTION[0].getMovimiento())
        count = 1
        for i in SOLUTION:
            text += "  " +str(count) + ". " + str(getMessage(i.getMovimiento())) + ".\n"
            count += 1
        return text
    
    def SaveFile(self):
        root = tk.Tk()
        root.withdraw()
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        print(33,f)
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        text = self.ListToString()
        f.write(text)
        f.close() # `()` was missing.
        root.destroy()
        
    def event_handler(self, event):
        # Clicked
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (self._rect.collidepoint(event.pos)):
            self._index = "active"
            if (self._type_of == "upload"):         # UPLOAD - - 
                self._button_active = True
                self.ChooseFile()
                self._button_active = False
            elif (self._type_of == "accept"):       # ACCEPT - -
                initial_tower.SaveDataToInitialTable()
                goal_tower.SaveDataToGoalTable()
                condition1 = Tabla.TablaInicial.CorrectFormat()[0]
                condition2 = Tabla.TablaMeta.CorrectFormat()[0]
                if (condition1 and condition2):
                    print("Tablas bien configuradas")
                    self.Accept()
                elif (condition1):  # Solo la tabla inicial está mal
                    texto = "Tabla meta está mal configurada"
                    print(texto)
                elif (condition2):  # Solo la tabla meta está mal
                    texto = "Tabla inicial está mal configurada"
                    print(texto)
                else:
                    texto = "Ambas tablas están mal configuradas"
                    print(texto)
            elif (self._type_of == "arrow_right"):  # ARROW RIGHT - -
                if (ActualTableSolution()[1] < (LenSolution()-1)): #last:7, showing 8
                    tupla    = NextTableSolution()
                    table    = tupla[0]
                    id_table = tupla[1]
                    SetTableToAnswerTable(table)
                    SetActualNumberToAnswer(id_table+1)
            elif (self._type_of == "arrow_left"):  # ARROW LEFT - -
                if (ActualTableSolution()[1] > 0): # 0 is the first table 
                    tupla    = PreviousTableSolution()
                    table    = tupla[0]
                    id_table = tupla[1]
                    SetTableToAnswerTable(table)
                    SetActualNumberToAnswer(id_table+1)
            elif (self._type_of == "save"):         # SAVE - - 
                self._button_active = True
                self.SaveFile()
                self._button_active = False
            elif (self._type_of == "again"):        # AGAIN - -
                setStage(0)
            
                
        # Hover
        elif self._rect.collidepoint(pygame.mouse.get_pos()):
            self._index = "hover"
        # Normal
        else:
            if self._button_active == False:
                self._index = "normal"


    ## End of the class
    ## 














##  ______         _  _   _____  _                  
##  | ___ \       | || | /  __ \| |                 
##  | |_/ /  __ _ | || | | /  \/| |  __ _  ___  ___ 
##  | ___ \ / _` || || | | |    | | / _` |/ __|/ __|
##  | |_/ /| (_| || || | | \__/\| || (_| |\__ \\__ \
##  \____/  \__,_||_||_|  \____/|_| \__,_||___/|___/
##
##  
class Ball(object):
    def __init__(self):
        
        # Definition: set of images
        self.images = []
        self.DefineImages()
        
        # Definition: Size and Pos as object's variable
        self.size = self.images["blue"].get_rect().size
        self.position = 0
        
        # Initial State
        self.index = "blue"

    def setPosition(self, position):
        self.position = position
        # Definition: Position and Size of Component
        self.rect = pygame.Rect(self.position,  self.size)

    def GetWidth(self, image):
        return image.get_rect().size[0]

    def GetHeight(self, image):
        return image.get_rect().size[1]

    def GetNewDimensions(self, image):
        height_destiny = 40             # Define the HEIGHT size
        width_source = self.GetWidth(image)
        height_source = self.GetHeight(image)
        width_destiny = width_source*height_destiny/height_source
        size_destiny = (int(width_destiny), int(height_destiny))
        return size_destiny
        
    def LoadImage(self, path):
        image = pygame.image.load(path)
        new_size = self.GetNewDimensions(image)
        image = pygame.transform.scale(image, new_size)
        return image
        
    def DefineImages(self):
        self.images = {
            "red" : self.LoadImage("./images/balls/red.png"),
            "red_hover" : self.LoadImage("./images/balls/red_hover.png"),
            "green" : self.LoadImage("./images/balls/green.png"),
            "green_hover" : self.LoadImage("./images/balls/green_hover.png"),
            "blue" : self.LoadImage("./images/balls/blue.png"),
            "blue_hover" : self.LoadImage("./images/balls/blue_hover.png"),
            "yellow" : self.LoadImage("./images/balls/yellow.png"),
            "yellow_hover" : self.LoadImage("./images/balls/yellow_hover.png"),
            "x" : self.LoadImage("./images/balls/x.png"),
            "x_hover" : self.LoadImage("./images/balls/x_hover.png"),
            "o" : self.LoadImage("./images/balls/o.png"),
            "o_hover" : self.LoadImage("./images/balls/o_hover.png")
            }
        
    def setIndex(self, index):
        self.index = index

    def getIndex(self):
        return self.index
    
    def getColor(self):
        if (self.getIndex()[0] == "r"):
            return "R"
        elif (self.getIndex()[0] == "g"):
            return "G"
        elif (self.getIndex()[0] == "b"):
            return "B"
        elif (self.getIndex()[0] == "y"):
            return "Y"
        elif (self.getIndex()[0] == "x"):
            return "X"
        elif (self.getIndex()[0] == "o"):
            return "O"
        else:
            print("Se encontro el color: ", self.getIndex()[0])
            return "Y"
            
    def setColor(self, color):
        if (color == "R"):
            self.setIndex("red")
        elif (color == "G"):
            self.setIndex("green")
        elif (color == "B"):
            self.setIndex("blue")
        elif (color == "Y"):
            self.setIndex("yellow")
        elif (color == "X"):
            self.setIndex("x")
        elif (color == "O"):
            self.setIndex("o")
        else:
            print("Error in setColor()", self.index, color)
            self.setIndex(self.index)
    
    def setHover(self):
        if not (self.index[-5:] == "hover"):
            self.index += "_hover"

    def setNormal(self):
        if (self.index[-5:] == "hover"):
            self.index = self.index[:-6]

    def NextIndex(self):
        if (self.index[0] == "r"):
            self.setIndex("green")
        elif (self.index[0] == "g"):
            self.setIndex("blue")
        elif (self.index[0] == "b"):
            self.setIndex("yellow")
        elif (self.index[0] == "y"):
            self.setIndex("x")
        elif (self.index[0] == "x"):
            self.setIndex("o")
        elif (self.index[0] == "o"):
            self.setIndex("red")
        else:
            print("Error in NextIndex()", self.index)
            self.setIndex(self.index)

    def draw(self, screen):
        screen.blit(self.images[self.index], self.rect)

    def event_handler(self, event):
        # Clicked
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (self.rect.collidepoint(event.pos)):
            self.NextIndex()
            
        # Hover
        elif self.rect.collidepoint(pygame.mouse.get_pos()):
            self.setHover()
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_r or event.key == pygame.K_1):
                    self.setIndex("red")
                elif (event.key == pygame.K_g or event.key == pygame.K_2):
                    self.setIndex("green")
                elif (event.key == pygame.K_b or event.key == pygame.K_3):
                    self.setIndex("blue")
                elif (event.key == pygame.K_y or event.key == pygame.K_4):
                    self.setIndex("yellow")
                elif (event.key == pygame.K_x or event.key == pygame.K_5):
                    self.setIndex("x")
                elif (event.key == pygame.K_o or event.key == pygame.K_6):
                    self.setIndex("o")
        # Normal
        else:
            self.setNormal()

    
    ## End of the class
    ## 











##   _____                                _____  _                  
##  |_   _|                              /  __ \| |                 
##    | |    ___  __      __  ___  _ __  | /  \/| |  __ _  ___  ___ 
##    | |   / _ \ \ \ /\ / / / _ \| '__| | |    | | / _` |/ __|/ __|
##    | |  | (_) | \ V  V / |  __/| |    | \__/\| || (_| |\__ \\__ \
##    \_/   \___/   \_/\_/   \___||_|     \____/|_| \__,_||___/|___/
##                                                                  
##                                                                  
class Tower(object):
    def __init__(self):
        self.balls = []
        self.type = ""
        self.x_start = 1        # First pixel in the X axis
        self.y_start = 1        # First pixel in the Y axis
        self.message = "Hello"  # Explication of move
        self.answer_number = -1

    def setXStart(self, pos):
        self.x_start = pos

    def getXStart(self):
        return self.x_start

    def setYStart(self, pos):
        self.y_start = pos

    def getYStart(self):
        return self.y_start

    def setType(self, _type):
        self.type = _type

    def getAnswerNumber(self):
        return self.answer_number

    def setAnswerNumber(self, number):
        self.answer_number = number

    def getMessage(self):
        return self.message
        
    def setMessage(self, code):
        if (code == 0):
            self.message = "this is the initial table"
        elif (code == 1):
            self.message = "turn LEFT the row 1"
        elif (code == 2):
            self.message = "turn LEFT the row 2"
        elif (code == 3):
            self.message = "turn LEFT the row 3"
        elif (code == 4):
            self.message = "turn LEFT the row 4"
        elif (code == 5):
            self.message = "turn LEFT the row 5"
        elif (code == 6):
            self.message = "turn RIGHT the row 1"
        elif (code == 7):
            self.message = "turn RIGHT the row 2"
        elif (code == 8):
            self.message = "turn RIGHT the row 3"
        elif (code == 9):
            self.message = "turn RIGHT the row 4"
        elif (code == 10):
            self.message = "turn RIGHT the row 5"
        elif (code == 11):
            self.message = "turn EMPTY SPACE to UP"
        elif (code == 12):
            self.message = "turn EMPTY SPACE to DOWN"
        elif (code == 13):
            self.message = "this is the goal table"
        else:
            self.message = "nothing, nothing :)"
    
    def SaveDataToInitialTable(self):
        table = Tabla.getTablaInicial()
        lista_de_colores = []
        for ball in self.balls:
            lista_de_colores += [ball.getColor()]
        table.Llenar(lista_de_colores)
        Tabla.setTablaInicial(table)
        
    def SaveDataToGoalTable(self):
        table = Tabla.getTablaMeta()
        lista_de_colores = []
        for ball in self.balls:
            lista_de_colores += [ball.getColor()]
        table.Llenar(lista_de_colores)
        Tabla.setTablaMeta(table)
        
    def setPosition(self, position):
        self.setXStart(position[0])
        self.setYStart(position[1])
        
    def addBall(self, ball):
        self.balls.append(ball)

    def removeBalls(self):
        del self.balls[:]
        
    def DefineBalls(self, Tabla):
        self.removeBalls()
        width  = 55     # width of the image + Space between
        height = 45     # height of the image + Space between
        for i in range(5):
            for j in range(4):
                #Tabla.PrintTorreDetallada()
                #print(i,j)
                color = Tabla.getColor(i,j)
                new_ball = Ball()
                new_ball.setColor(color)
                x_pos = self.getXStart() + (j*width) # i starts at 0
                y_pos = self.getYStart() + (i*height)# i starts at 0
                position = (x_pos, y_pos)
                new_ball.setPosition(position)
                self.addBall(new_ball)
                

    def DefineBallsTesting(self):
        width  = 55     # width of the image + Space between
        height = 45     # height of the image + Space between
        for i in range(4):
            for j in range(5):
                new_ball = Ball()
                x_pos = self.getXStart() + (i*width) # i starts at 0
                y_pos = self.getYStart() + (j*height)# i starts at 0
                position = (x_pos, y_pos)
                new_ball.setPosition(position)
                self.addBall(new_ball)

    def getCountColors(self):
        color_list = [0,0,0,0,0,0]  #[R,G,B,Y,X,O]
        for ball in self.balls:
            if (ball.getColor() == "R"):
                color_list[0] += 1
            elif (ball.getColor() == "G"):
                color_list[1] += 1
            elif (ball.getColor() == "B"):
                color_list[2] += 1
            elif (ball.getColor() == "Y"):
                color_list[3] += 1
            elif (ball.getColor() == "X"):
                color_list[4] += 1
            elif (ball.getColor() == "O"):
                color_list[5] += 1
            else:
                color_list[0] = -99
        return color_list

    def drawErrorMessages(self, screen):
        initial_tower.SaveDataToInitialTable()
        goal_tower.SaveDataToGoalTable()
        if (Tabla.TablaInicial.CorrectFormat()[0]==False or Tabla.TablaMeta.CorrectFormat()[0]==False):
            color_back = hex2rgb("#16A085")
            color_font = hex2rgb("#E74C3C")
            myfont = pygame.font.SysFont('Open Sans', 24)
            pygame.draw.rect(screen, color_back, (100,530,300,50), 0)
            screen.blit(myfont.render("! check the towers", False, color_font),(110,530))
            
        
    
    def drawNumbers(self, screen):
        color_list = self.getCountColors()
        pygame.font.init()
        myfont = pygame.font.SysFont('Open Sans', 16)
        # Coordinates
        color_back = hex2rgb("#9EA6AF")
        color_bad = hex2rgb("#E74C3C")
        color_white = hex2rgb("#2C3E50")
        y1 = 495
        y2 = 528
        if (self.type == 0):
            x1 = 575
            x2 = 655
            x3 = 732
            # Red
            pygame.draw.rect(screen, color_back, (x1,y1,20,20), 0)
            if (color_list[0] == 4):
                screen.blit(myfont.render(str(color_list[0]), False, color_white),(x1,y1))
            else:
                screen.blit(myfont.render(str(color_list[0]), False, color_bad),(x1,y1))
            # Green
            pygame.draw.rect(screen, color_back, (x1,y2,20,20), 0)
            if (color_list[1] == 4):
                screen.blit(myfont.render(str(color_list[1]), False, color_white),(x1,y2))
            else:
                screen.blit(myfont.render(str(color_list[1]), False, color_bad),(x1,y2))
            # Blue
            pygame.draw.rect(screen, color_back, (x2,y2,20,20), 0)
            if (color_list[2] == 4):
                screen.blit(myfont.render(str(color_list[2]), False, color_white),(x2,y1))
            else:
                screen.blit(myfont.render(str(color_list[2]), False, color_bad),(x2,y1))
            # Yellow
            pygame.draw.rect(screen, color_back, (x2,y2,20,20), 0)
            if (color_list[3] == 4):
                screen.blit(myfont.render(str(color_list[3]), False, color_white),(x2,y2))
            else:
                screen.blit(myfont.render(str(color_list[3]), False, color_bad),(x2,y2))
            # Block
            pygame.draw.rect(screen, color_back, (x3,y2,20,20), 0)
            if (color_list[4] == 3):
                screen.blit(myfont.render(str(color_list[4]), False, color_white),(x3,y1))
            else:
                screen.blit(myfont.render(str(color_list[4]), False, color_bad),(x3,y1))
            # Empty
            pygame.draw.rect(screen, color_back, (x3,y2,20,20), 0)
            if (color_list[5] == 1):
                screen.blit(myfont.render(str(color_list[5]), False, color_white),(x3,y2))
            else:
                screen.blit(myfont.render(str(color_list[5]), False, color_bad),(x3,y2))
        else:
            x1 = 575+298
            x2 = 655+298
            x3 = 732+298
            # Red
            pygame.draw.rect(screen, color_back, (x1,y1,20,20), 0)
            if (color_list[0] == 4):
                screen.blit(myfont.render(str(color_list[0]), False, color_white),(x1,y1))
            else:
                screen.blit(myfont.render(str(color_list[0]), False, color_bad),(x1,y1))
            # Green
            pygame.draw.rect(screen, color_back, (x1,y2,20,20), 0)
            if (color_list[1] == 4):
                screen.blit(myfont.render(str(color_list[1]), False, color_white),(x1,y2))
            else:
                screen.blit(myfont.render(str(color_list[1]), False, color_bad),(x1,y2))
            # Blue
            pygame.draw.rect(screen, color_back, (x2,y2,20,20), 0)
            if (color_list[2] == 4):
                screen.blit(myfont.render(str(color_list[2]), False, color_white),(x2,y1))
            else:
                screen.blit(myfont.render(str(color_list[2]), False, color_bad),(x2,y1))
            # Yellow
            pygame.draw.rect(screen, color_back, (x2,y2,20,20), 0)
            if (color_list[3] == 4):
                screen.blit(myfont.render(str(color_list[3]), False, color_white),(x2,y2))
            else:
                screen.blit(myfont.render(str(color_list[3]), False, color_bad),(x2,y2))
            # Block
            pygame.draw.rect(screen, color_back, (x3,y2,20,20), 0)
            if (color_list[4] == 3):
                screen.blit(myfont.render(str(color_list[4]), False, color_white),(x3,y1))
            else:
                screen.blit(myfont.render(str(color_list[4]), False, color_bad),(x3,y1))
            # Empty
            pygame.draw.rect(screen, color_back, (x3,y2,20,20), 0)
            if (color_list[5] == 1):
                screen.blit(myfont.render(str(color_list[5]), False, color_white),(x3,y2))
            else:
                screen.blit(myfont.render(str(color_list[5]), False, color_bad),(x3,y2))

        
    def draw(self, screen):
        for ball in self.balls:
            ball.draw(screen)
            #screen.blit(ball.images[ball.index], ball.rect)
        if (self.type < 2):
            self.drawNumbers(screen)
        else:
            myfont = pygame.font.SysFont('Copperplate Gothic', 24)
            color_font = hex2rgb("#2C3E50")
            color_back = hex2rgb("#F7E5E4")
            # Instruction
            pygame.draw.rect(screen, color_back, (465,118,676,37), 0)
            screen.blit(myfont.render(self.getMessage(), False, color_font),(470,122))
            # Number x:804 and y:456
            color_font = hex2rgb("#2C3E50")
            color_back = hex2rgb("#FFFFFF")
            pygame.draw.rect(screen, color_back, (700,450, 240,70), 0)
            actual_number = str(self.getAnswerNumber())
            total_number = "of  " + str(LenSolution())
            myfont = pygame.font.SysFont('Open Sans', 24)
            screen.blit(myfont.render(actual_number, False, color_font),(800,443)) # Actual number
            myfont = pygame.font.SysFont('Open Sans', 16)
            screen.blit(myfont.render(total_number, False, color_font),(875,448)) # Total number
            
            

    def event_handler(self, event):
        if (self.type < 2):
            for ball in self.balls:
                ball.event_handler(event)

    ## End of the class
    ## 


def SetTableToAnswerTable(table):
    answer_tower.DefineBalls(table)
    code = table.getMovimiento()
    answer_tower.setMessage(code)

def SetActualNumberToAnswer(actual_number):
    answer_tower.setAnswerNumber(actual_number)

def CreateTowerFromTable(table):
    global answer_tower
    code = table.getMovimiento()
    answer_tower.setType(2)
    answer_tower.setAnswerNumber(1)
    answer_tower.setMessage(code)
    answer_tower.setPosition((710,210))
    answer_tower.DefineBalls(table)
    
def ConfigTowerInitial():
    global initial_tower
    initial_table = Tabla.Tabla(-1, 0)
    initial_table.Llenar("inicial")
    initial_tower.setType(0)
    initial_tower.setPosition((550,236))
    initial_tower.DefineBalls(initial_table)

def ConfigTowerGoal():
    global goal_tower
    goal_table = Tabla.Tabla(-1, -2)
    goal_table.Llenar("meta")
    goal_tower.setType(1)
    goal_tower.setPosition((850,236))
    goal_tower.DefineBalls(goal_table)

def ConfigTowers():
    ConfigTowerInitial()
    ConfigTowerGoal()


# At the start of the program
# Initial Tower
initial_tower = Tower()
# Goal Tower
goal_tower  = Tower()
# Answer tower
answer_tower = Tower()
