# File of components for PyGame
#

# write here the components

import pygame, sys
from pygame.locals import *
from pygame import *

def hex2rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    rgb_code = tuple(int(hex_code[i:i+2], 16) for i in (0, 2 ,4))
    return rgb_code;



# --- Classes ---
def GetNewDimensions(image):
    height_destiny = 40
    width_source = image.get_rect().size[0]
    height_source = image.get_rect().size[1]
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
    else:
        print("Sucedió un error del sistema")
        exit()
    return dictionary

class Button(object):
    def __init__(self, position, type_of):

        # Definition: set of images
        self._images = DefineImages(type_of)

        # Definition: Size and Pos as object's variable
        self._size = self._images["normal"].get_rect().size
        self._position = position
        
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
        # Hover
        elif self._rect.collidepoint(pygame.mouse.get_pos()):
            self._index = "hover"
        # Normal
        else:
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



