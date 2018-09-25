# Main file of Babylon Tower Solver
# 
# Tecnológico de Costa Rica
# Computing Engineering School
# Course
#   Artificial Intelligence
#   Teacher Jorge Vargas
# Programmers
#   Edisson López @ediloaz
#   Alonso Rivas
# September, 2018
#

import pygame, sys
from pygame.locals import *
import VisualComponents as components
import Tabla as Tabla
import Controller as controller



# Global variables/constants
SCREEN_SIZE = (1200, 650)
BG_COLOUR   = (250, 250, 250)
screen = 0



class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def SetBackground(stage):
    if (stage == 0):
        pass
    path = "./images/background/pattern.png"
    BackGround = Background(path, [0,0])
    Screen().fill([255, 255, 255])
    Screen().blit(BackGround.image, BackGround.rect)
    

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

def Screen():
    global screen
    return screen

def CreateScreen():
    global screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Babylon Tower Solver")
    screen = SetIcon(screen)
    
    return screen

def run():
    pygame.init()
    screen = CreateScreen()
    clock = pygame.time.Clock()
    running = True;
    # stage = 0;          # "Cargando componentes visuales"
    while running:
        time_passed = clock.tick(30)
        stage = components.interface()
        # Form interface
        if (stage == 0):
            # Not events #
            # Draws #
            print("Configurando componentes visuales")
            SetBackground(0)
            pygame.display.flip()
            components.ConfigTowers()
            components.setStage(1)
            print("Interfaz cargada")
        elif (stage == 1):
            # --- events --- #
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False;
                # --- Keydown events --- #
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_ESCAPE):
                        print("Escape")
                        running = False;

                # --- button events --- #
                button_accept.event_handler(event)
                button_upload.event_handler(event)
                # ball.event_handler(event)
                components.initial_tower.event_handler(event)
                components.goal_tower.event_handler(event)
                        
            # --- Draws --- #
            SetBackground(1)                         # set pattern as background
            button_accept.draw(screen)
            button_upload.draw(screen)
            components.initial_tower.draw(screen)
            components.goal_tower.draw(screen)
            pygame.display.flip()
        
    ExitGame();

button_accept = components.Button(SCREEN_SIZE, (200, 600), "accept")
button_upload = components.Button(SCREEN_SIZE, (200, 500), "upload")




run()



