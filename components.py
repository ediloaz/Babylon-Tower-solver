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


def hex2rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    rgb_code = tuple(int(hex_code[i:i+2], 16) for i in (0, 2 ,4))
    return rgb_code;



##  ______         _    _                   _____  _                  
##  | ___ \       | |  | |                 /  __ \| |                 
##  | |_/ / _   _ | |_ | |_   ___   _ __   | /  \/| |  __ _  ___  ___ 
##  | ___ \| | | || __|| __| / _ \ | '_ \  | |    | | / _` |/ __|/ __|
##  | |_/ /| |_| || |_ | |_ | (_) || | | | | \__/\| || (_| |\__ \\__ \
##  \____/  \__,_| \__| \__| \___/ |_| |_|  \____/|_| \__,_||___/|___/                                                                                                            
##
## 
class Button(object):
    def __init__(self, SIZE, position, type_of):

        # Definition: set of images
        self._images = self.DefineImages(type_of)

        # Definition: Size and Pos as object's variable
        self._size = self._images["normal"].get_rect().size

        width_screen = SIZE[0]
        width_object = self.GetWidth(self._images["normal"])
        width = width_screen/2 - width_object/2
        height = position[1]
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
        height_destiny = 30             # Define the HEIGHT size
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

    def DefineImages(self, text):
        if text == "accept":
            dictionary = {
                "normal" : self.LoadImage("./images/buttons/button_accept_normal.png"),
                "hover" : self.LoadImage("./images/buttons/button_accept_hover.png"),
                "active" : self.LoadImage("./images/buttons/button_accept_active.png")
                }
        elif text == "upload":
            dictionary = {
                "normal" : self.LoadImage("./images/buttons/button_upload_normal.png"),
                "hover" : self.LoadImage("./images/buttons/button_upload_hover.png"),
                "active" : self.LoadImage("./images/buttons/button_upload_active.png")
                }
        else:
            print("Sucedió un error del sistema")
            exit()
        return dictionary

    
    def draw(self, screen):
        screen.blit(self._images[self._index], self._rect)

    def ChooseFile(self):
        root = tk.Tk()
        root.withdraw()
        try:
            file_path = filedialog.askopenfilename(filetypes=(("Babylon files", "*.by"),("All files", "*.*") ))
            print (file_path)
        except:
            pass
        root.destroy()

    def event_handler(self, event):
        # Clicked
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (self._rect.collidepoint(event.pos)):
            self._index = "active"
            if (self._type_of == "upload"):
                self._button_active = True
                self.ChooseFile()
                self._button_active = False
            
            
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
        self.x_start = 1     # First pixel in the X axis
        self.y_start = 1     # First pixel in the Y axis

    def setXStart(self, pos):
        self.x_start = pos

    def getXStart(self):
        return self.x_start

    def setYStart(self, pos):
        self.y_start = pos

    def getYStart(self):
        return self.y_start

    def setPosition(self, position):
        self.setXStart(position[0])
        self.setYStart(position[1])
        
    def addBall(self, ball):
        self.balls.append(ball)
        
    def DefineBalls(self, Tabla):
        for i in range(5):
            for j in range(4):
                color = Tabla.tabla[i][j].getColor()    

    def DefineBallsTesting(self):
        for i in range(4):
            for j in range(5):
                new_ball = Ball()
                width  = 55     # width of the image + Space between
                height = 45     # height of the image + Space between
                x_pos = self.getXStart() + (i*width) # i starts at 0
                y_pos = self.getYStart() + (j*height)# i starts at 0
                position = (x_pos, y_pos)
                new_ball.setPosition(position)
                self.addBall(new_ball)
  
    def draw(self, screen):
        for ball in self.balls:
            ball.draw(screen)

    def event_handler(self, event):
        for ball in self.balls:
            ball.event_handler(event)

    ## End of the class
    ## 






