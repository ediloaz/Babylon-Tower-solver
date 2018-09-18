# Main file of Babylon Tower Solver
# 
# Tecnológico de Costa Rica
# Computing Engineering School
# Course
#   Inteligencia Artificial
#   Teacher Jorge Vargas
# Programmers
#   Edisson López @ediloaz
#   Alonso Rivas
# September, 2018
#

import pygame, sys
from pygame.locals import *

import components as components;

# declarations
BG_COLOUR   = (250, 250, 250)
button_accept = components.Button((200, 200), "accept")
button_upload = components.Button((200, 450), "upload")
pick_color    = components.PickColor((220, 0))

def ExitGame():
    pygame.display.quit()
    pygame.quit()
    sys.exit()
    
def ConfigureScreen():
    pass

def SetIcon(screen):
    icon = pygame.image.load('./images/icons/icon_screen.jpg')
    pygame.display.set_icon(icon)
    return screen

def CreateScreen():
    SIZE = (800, 500)
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Babylon Tower Solver")
    screen = SetIcon(screen)
    
    return screen

def run():
    pygame.init()
    
    screen = CreateScreen()
    
    clock = pygame.time.Clock()

    running = True;
    while running:
        #time_passed = clock.tick(30)

        # --- events --- #
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False;
            # --- Keydown events --- #
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    print("Escape")
                    running = False;
                elif (event.key == pygame.K_1):
                    print("Uno")

            # --- button events --- #
            button_accept.event_handler(event)
            button_upload.event_handler(event)
            pick_color.event_handler(event)
                        

        # --- Draws --- #
        screen.fill(BG_COLOUR)
        button_accept.draw(screen)
        button_upload.draw(screen)
        pick_color.draw(screen)
        # pygame.draw.aaline(screen, LINE_COLOUR, (1, 1), (639, 399))
        pygame.display.flip()
        
    ExitGame();
run()




