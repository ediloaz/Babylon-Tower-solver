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
stage = 0


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location



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

def setBackgroundLoading():
    path = "./images/background/stage0.png"
    BackGround = Background(path, [0,0])
    Screen().fill([255, 255, 255])
    Screen().blit(BackGround.image, BackGround.rect)
def CreateScreenLoading():
    global screen
    screen = pygame.display.set_mode((400,180))
    pygame.display.set_caption("Babylon Tower Solver: Loading")
    screen = SetIcon(screen)
    return screen
# First screen 
def runLoading():
    screen = CreateScreenLoading()
    print("Configurando componentes visuales")
    setBackgroundLoading()
    pygame.display.flip()
    components.ConfigTowers()
    print("Interfaz cargada")
    components.NextStage()
        

def SetBackgroundForm():
    path = "./images/background/pattern.png"
    BackGround = Background(path, [0,0])
    Screen().fill([255, 255, 255])
    Screen().blit(BackGround.image, BackGround.rect)
def CreateScreenForm():
    global screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Babylon Tower Solver: Form")
    screen = SetIcon(screen)
    return screen
def runForm():
    screen = CreateScreenForm()
    # clock = pygame.time.Clock()
    running = True
    while running and (components.Stage() == 1):
        #time_passed = clock.tick(30)
        # --- events --- #
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False;
            # --- Keydown events --- #
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    print("Escape: El jugador va a salir")
                    components.setStage(4)
                    running = False
            # --- button events --- #
            button_accept.event_handler(event)
            button_upload.event_handler(event)
            components.initial_tower.event_handler(event)
            components.goal_tower.event_handler(event)
        # --- Draws --- #
        SetBackgroundForm()                         # set pattern as background
        button_accept.draw(screen)
        button_upload.draw(screen)
        components.initial_tower.draw(screen)
        components.goal_tower.draw(screen)
        pygame.display.flip()
    
        

def SetBackgroundThinking():
    path = "./images/background/pattern.png"
    BackGround = Background(path, [0,0])
    Screen().fill([255, 255, 255])
    Screen().blit(BackGround.image, BackGround.rect)
def CreateScreenThinking():
    global screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Babylon Tower Solver: Thinking")
    screen = SetIcon(screen)
    return screen
def runThinking():
    screen = CreateScreenThinking()
    # --- events --- #
    for i in range(6):
        print("Pasda i",i)
        if (i==3):
            components.Stage2()
        else:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    running = False;
                # --- Keydown events --- #
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_ESCAPE):
                        print("Escape: El jugador va a salir")
                        components.setStage(4)
                # --- button events --- #
                #button_accept.event_handler(event)
            # --- Draws --- #
            SetBackgroundThinking()                         # set pattern as background
            # button_accept.draw(screen)
            pygame.display.flip()
    components.NextStage()


def SetBackgroundAnswer():
    path = "./images/background/stage0.png"
    BackGround = Background(path, [0,0])
    Screen().fill([255, 255, 255])
    Screen().blit(BackGround.image, BackGround.rect)
def CreateScreenAnswer():
    global screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Babylon Tower Solver: Answer")
    screen = SetIcon(screen)
    return screen
def runAnswer():
    screen = CreateScreenAnswer()
    print("Answer")
    while (components.Stage() == 3):
        # --- events --- #
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False;
            # --- Keydown events --- #
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_ESCAPE):
                    print("Escape: El jugador va a salir")
                    components.setStage(4)
            # --- button events --- #
        # --- Draws --- #
        SetBackgroundForm()                         # set pattern as background
        pygame.display.flip()
        


def run():
    global stage
    pygame.init()
    components.setStage(0)
    stage = 0
    while stage < 4:
        print("stageee: ", stage)
        stage = components.Stage()
        print("stageee desyes: ", stage)
        if (stage == 0):
            runLoading()
        elif (stage == 1):
            runForm()
        elif (stage == 2):
            runThinking()
        elif (stage == 3):
            runAnswer() 
    ExitGame()
            

button_accept = components.Button(SCREEN_SIZE, (200, 600), "accept")
button_upload = components.Button(SCREEN_SIZE, (200, 500), "upload")


running = False
run()



