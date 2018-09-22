# File of components for PyGame
#

# write here the components

import pygame, sys
from pygame.locals import *
from pygame import *
import tkinter as tk
from tkinter import filedialog


def hex2rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    rgb_code = tuple(int(hex_code[i:i+2], 16) for i in (0, 2 ,4))
    return rgb_code;



# --- Classes ---

def GetWidth(thing):
    return thing.get_rect().size[0]

def GetHeight(thing):
    return thing.get_rect().size[1]

def GetNewDimensions(image):
    height_destiny = 40
    width_source = GetWidth(image)
    height_source = GetHeight(image)
    width_destiny = width_source*height_destiny/height_source
    size_destiny = (int(width_destiny), int(height_destiny))
    return size_destiny
    
def LoadImage(path):
    image = pygame.image.load(path)
    new_size = GetNewDimensions(image)
    image = pygame.transform.scale(image, new_size)
    return image

def DefineImages(text):
    if text == "accept":
        dictionary = {
            "normal" : LoadImage("./images/buttons/button_accept_normal.png"),
            "hover" : LoadImage("./images/buttons/button_accept_hover.png"),
            "active" : LoadImage("./images/buttons/button_accept_active.png")
            }
    elif text == "upload":
        dictionary = {
            "normal" : LoadImage("./images/buttons/button_upload_normal.png"),
            "hover" : LoadImage("./images/buttons/button_upload_hover.png"),
            "active" : LoadImage("./images/buttons/button_upload_active.png")
            }
    elif text == "ball":
        dictionary = {
            "blue_normal" : LoadImage("./images/balls/Blue.png"),
            "blue_hover" : LoadImage("./images/balls/Blue.png"),
            "red_normal" : LoadImage("./images/balls/Red.png"),
            "red_hover" : LoadImage("./images/balls/Red.png"),
            "yellow_normal" : LoadImage("./images/balls/Yellow.png"),
            "yellow_hover" : LoadImage("./images/balls/Yellow.png"),
            "green_normal" : LoadImage("./images/balls/Green.png"),
            "green_hover" : LoadImage("./images/balls/Green.png"),
            }
    else:
        print("Sucedió un error del sistema")
        exit()
    return dictionary

class Button(object):
    def __init__(self, SIZE, position, type_of):

        # Definition: set of images
        self._images = DefineImages(type_of)

        # Definition: Size and Pos as object's variable
        self._size = self._images["normal"].get_rect().size

        width_screen = SIZE[0]
        width_object = GetWidth(self._images["normal"])
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





class Ball(object):
    def __init__(self, position):

        # Definition: set of images
        self._images = DefineImages("ball")

        # Definition: Size and Pos as object's variable
        self._size = self._images["normal"].get_rect().size
        self._position = position
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

    def draw(self, screen):
        screen.blit(self._images[self._index], self._rect)

   
       
    def event_handler(self, event):
        # Clicked
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1) and (self._rect.collidepoint(event.pos)):
            self._index = "active"
            self.NextIndex()
            
        # Hover
        elif self._rect.collidepoint(pygame.mouse.get_pos()):
            self._index = "hover"
        # Normal
        else:
            if self._button_active == False:
                self._index = "normal"







class PickColor(object):
    def __init__(self, position):
        self._size = (120,30)
        self._position = position
        
        self._images = [
                pygame.image.load("./images/balls/Blue.png"),
                pygame.image.load("./images/balls/Yellow.png"),
                pygame.image.load("./images/balls/Red.png"),
                pygame.image.load("./images/balls/Green.png")
            ]

        self._rect = self._images[0].get_rect()
        print("size:",self._rect)

        self._index = 0

        pygame.display.set_mode(self._images[0].get_rect().size,0,32)
        
        self._images[0].convert()
        self._images[1].convert()
        self._images[2].convert()
        self._images[3].convert()

    def draw(self, screen):
        screen.blit(self._images[self._index], self._position)

    def event_handler(self, event):
        # Clicked
        if event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
            print("s",event.button)
            if event.button == 1: # is left button clicked
                print("a")
                if self._rect.collidepoint(event.pos): # is mouse over button
                    print("b")
                    self._index = (self._index+1) % 3
        # Hover
        elif self._rect.collidepoint(pygame.mouse.get_pos()):
            pass
        # Normal
        else:
            self._index = self._index



