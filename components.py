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


def AAfilledRoundedRect(rect,color,radius=0.4):

    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect         = Rect(rect)
    color        = Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = Surface(rect.size,SRCALPHA)

    circle       = Surface([min(rect.size)*3]*2,SRCALPHA)
    draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)

    return rectangle


# --- Classes ---

class ButtonPrimary(object):
    def __init__(self, position):
        self._size = (120,30)
        self._images = {
            "normal" : pygame.image.load("./images/buttons/button_primary_normal.png"),
            "hover" : pygame.image.load("./images/buttons/button_primary_hover.png"),
            "active" : pygame.image.load("./images/buttons/button_primary_active.png")
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



class ButtonSuccess(object):
    def __init__(self, position):
        self._position = position

        size = (100, 25)
        # Static, hover, pressed
        self._images = [
            pygame.Surface(size),    
            pygame.Surface(size),    
            pygame.Surface(size),    
        ]

        # define colors
        light_color = hex2rgb("#28A745")
        dark_color = hex2rgb("#218838")
        
        # fill images with color
        self._images[0].fill(light_color)
        self._images[1].fill(dark_color)
        self._images[2].fill(dark_color)

        # get image size and position
        self._rect = pygame.Rect(position, size)
        

        # select first image
        self._index = 0

        # text of the button
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 16)
        self._textsurface = myfont.render("Seleccionar", False, (255,255,255))

        

    def draw(self, screen):
        # draw selected image
        screen.blit(self._images[self._index], self._rect)
        screen.blit(self._textsurface,self._position+(100,0))

    def event_handler(self, event):
        # Hover
        if self._rect.collidepoint(pygame.mouse.get_pos()):
            self._index = 1
        # Clicked
        elif event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
            if event.button == 1: # is left button clicked
                if self._rect.collidepoint(event.pos): # is mouse over button
                    self._index = 2 # change image
        # None
        else:
            self._index = 0;

