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
BG_COLOUR = (255, 255, 255)
LINE_COLOUR = (0, 0, 0)
button = components.ButtonPrimary((50, 5))

def ExitGame():
    pygame.display.quit()
    pygame.quit()
    sys.exit()
    
def ConfigureScreen():
    pass

def CreateScreen():
    SIZE = (800, 500)
    screen = pygame.display.set_mode(SIZE)
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
            button.event_handler(event)
                        

        # --- Draws --- #
        screen.fill(BG_COLOUR)
        button.draw(screen)
        # pygame.draw.aaline(screen, LINE_COLOUR, (1, 1), (639, 399))
        pygame.display.flip()
        
    ExitGame();
run()




