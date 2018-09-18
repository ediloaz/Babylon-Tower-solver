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


class ButtonUpload(object):
    def __init__(self, position):
        self._size = (120,30)
        self._images = {
            "normal" : pygame.image.load("./images/buttons/button_upload_normal.png"),
            "hover" : pygame.image.load("./images/buttons/button_upload_hover.png"),
            "active" : pygame.image.load("./images/buttons/button_upload_active.png")
            }

        new_size = (image.get_rect().size)[0]
        self._images["normal"] = pygame.transform.scale(self._images["normal"], (500, 200))

        self._rect = self._images["normal"].get_rect()
        print("size:",self._rect)

        self._index = "normal"

        pygame.display.set_mode(self._images["normal"].get_rect().size,0,32)
        
        self._images["normal"].convert()
        self._images["hover"].convert()
        self._images["active"].convert()

    def draw(self, screen):
        screen.blit(self._images[self._index], self._rect)

    def event_handler(self, event):
        # Hover
        if self._rect.collidepoint(pygame.mouse.get_pos()):
            self._index = "hover"
        # Clicked
        elif event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
            if event.button == 1: # is left button clicked
                if self._rect.collidepoint(event.pos): # is mouse over button
                    self._index = "active" # change image
        # Normal
        else:
            self._index = "normal"


class ButtonAccept(object):
    def __init__(self, position):
        self._size = (120,30)
        self._images = {
            "normal" : pygame.image.load("./images/buttons/button_accept_normal.png"),
            "hover" : pygame.image.load("./images/buttons/button_accept_hover.png"),
            "active" : pygame.image.load("./images/buttons/button_accept_active.png")
            }

        self._rect = self._images["normal"].get_rect()
        print("size:",self._rect)

        self._index = "normal"

        pygame.display.set_mode(self._images["normal"].get_rect().size,0,32)
        
        self._images["normal"].convert()
        self._images["hover"].convert()
        self._images["active"].convert()

    def draw(self, screen):
        screen.blit(self._images[self._index], self._rect)

    def event_handler(self, event):
        # Clicked
        if event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
            self._index = "active" # change image
        # Hover
        elif self._rect.collidepoint(pygame.mouse.get_pos()):
            self._index = "hover"
        # Normal
        else:
            self._index = "normal"



class ButtonUpload(object):
    def __init__(self, position):
        self._size = (120,30)
        self._images = {
            "normal" : pygame.image.load("./images/buttons/button_upload_normal.png"),
            "hover" : pygame.image.load("./images/buttons/button_upload_hover.png"),
            "active" : pygame.image.load("./images/buttons/button_upload_active.png")
            }

        self._rect = self._images["normal"].get_rect()
        print("size:",self._rect)

        self._index = "normal"

        pygame.display.set_mode(self._images["normal"].get_rect().size,0,32)
        
        self._images["normal"].convert()
        self._images["hover"].convert()
        self._images["active"].convert()

    def draw(self, screen):
        screen.blit(self._images[self._index], self._rect)

    def event_handler(self, event):
        
        # Clicked
        if event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
            if event.button == 1: # is left button clicked
                if self._rect.collidepoint(event.pos): # is mouse over button
                    self._index = "active" # change image
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



