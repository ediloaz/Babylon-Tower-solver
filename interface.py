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


import os           # For center the window
import ctypes       # For center the window
import pygame, sys
from pygame.locals import *
import VisualComponents as components
import Tabla as Tabla
import Controller as controller



# Global variables/constants
# SCREEN_SIZE = (1200, 650)
# BG_COLOUR   = (250, 250, 250)
screen = 0
stage = 0


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def hex2rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    rgb_code = tuple(int(hex_code[i:i+2], 16) for i in (0, 2 ,4))
    return rgb_code;

def ExitGame():
    pygame.display.quit()
    pygame.quit()
    sys.exit()
    
def SetIcon(screen):
    icon = pygame.image.load('./images/icons/icon_screen.jpg')
    pygame.display.set_icon(icon)
    return screen

def getResolution():
    user32 = ctypes.windll.user32
    return (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))

def getPositionStart(x_window, y_window):
    x_screen = getResolution()[0]
    y_screen = getResolution()[1]
    x_start = (x_screen-x_window)/2
    y_start = (y_screen-y_window)/2
    return (x_start, y_start)

def Screen():
    global screen
    return screen



#   _                    _  _                                                      
#  | |                  | |(_)                                                     
#  | |  ___    __ _   __| | _  _ __    __ _     ___   ___  _ __   ___   ___  _ __  
#  | | / _ \  / _` | / _` || || '_ \  / _` |   / __| / __|| '__| / _ \ / _ \| '_ \ 
#  | || (_) || (_| || (_| || || | | || (_| |   \__ \| (__ | |   |  __/|  __/| | | |
#  |_| \___/  \__,_| \__,_||_||_| |_| \__, |   |___/ \___||_|    \___| \___||_| |_|
#                                      __/ |                                       
#                                     |___/                                        
def getScreenSizeLoading():
    x = 400
    y = 400
    return (x,y)
def setBackgroundLoading():
    path = "./images/background/Loading.png"
    BackGround = Background(path, [0,0])
    Screen().blit(BackGround.image, BackGround.rect)
def CreateScreenLoading():
    global screen
    x_window = getScreenSizeLoading()[0]
    y_window = getScreenSizeLoading()[1]
    position_start = getPositionStart(x_window, y_window)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % position_start
    screen = pygame.display.set_mode((x_window,y_window))
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
        


#    __                                                                
#   / _|                                                               
#  | |_   ___   _ __  _ __ ___      ___   ___  _ __   ___   ___  _ __  
#  |  _| / _ \ | '__|| '_ ` _ \    / __| / __|| '__| / _ \ / _ \| '_ \ 
#  | |  | (_) || |   | | | | | |   \__ \| (__ | |   |  __/|  __/| | | |
#  |_|   \___/ |_|   |_| |_| |_|   |___/ \___||_|    \___| \___||_| |_|
#                                                                   
def getScreenSizeForm():
    x = 1200
    y = 650
    return (x,y)
def SetBackgroundForm():
    path = "./images/background/Form.png"
    BackGround = Background(path, [0,0])
    Screen().fill([255, 255, 255])
    Screen().blit(BackGround.image, BackGround.rect)
def CreateScreenForm():
    global screen
    x_window = getScreenSizeForm()[0]
    y_window = getScreenSizeForm()[1]
    position_start = getPositionStart(x_window, y_window)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % position_start
    screen = pygame.display.set_mode((x_window,y_window))
    pygame.display.set_caption("Babylon Tower Solver: Form")
    screen = SetIcon(screen)
    return screen
def runForm():
    button_upload = components.Button((120, 425), "upload")
    button_accept = components.Button((120, 550), "accept")
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
    
        

#   _    _      _         _     _                                                      
#  | |  | |    (_)       | |   (_)                                                     
#  | |_ | |__   _  _ __  | | __ _  _ __    __ _     ___   ___  _ __   ___   ___  _ __  
#  | __|| '_ \ | || '_ \ | |/ /| || '_ \  / _` |   / __| / __|| '__| / _ \ / _ \| '_ \ 
#  | |_ | | | || || | | ||   < | || | | || (_| |   \__ \| (__ | |   |  __/|  __/| | | |
#   \__||_| |_||_||_| |_||_|\_\|_||_| |_| \__, |   |___/ \___||_|    \___| \___||_| |_|
#                                          __/ |                                       
#                                         |___/
def getScreenSizeThinking():
    x = 400
    y = 400
    return (x,y)
def SetBackgroundThinking():
    path = "./images/background/Thinking.png"
    BackGround = Background(path, [0,0])
    Screen().fill([255, 255, 255])
    Screen().blit(BackGround.image, BackGround.rect)
def CreateScreenThinking():
    global screen
    x_window = getScreenSizeThinking()[0]
    y_window = getScreenSizeThinking()[1]
    position_start = getPositionStart(x_window, y_window)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % position_start
    screen = pygame.display.set_mode((x_window,y_window))
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
                #button_save.event_handler(event)
            # --- Draws --- #
            SetBackgroundThinking()                         # set pattern as background
            pygame.display.flip()
    components.NextStage()



                                                                                
                                                                                
#    __ _  _ __   ___ __      __  ___  _ __     ___   ___  _ __   ___   ___  _ __  
#   / _` || '_ \ / __|\ \ /\ / / / _ \| '__|   / __| / __|| '__| / _ \ / _ \| '_ \ 
#  | (_| || | | |\__ \ \ V  V / |  __/| |      \__ \| (__ | |   |  __/|  __/| | | |
#   \__,_||_| |_||___/  \_/\_/   \___||_|      |___/ \___||_|    \___| \___||_| |_|
#                                                                                                                                                               
def getScreenSizeAnswer():
    x = 1200
    y = 650
    return (x,y)
def SetBackgroundAnswer():
    path = "./images/background/Answer.png"
    BackGround = Background(path, [0,0])
    Screen().fill([255, 255, 255])
    Screen().blit(BackGround.image, BackGround.rect)
def CreateScreenAnswer():
    global screen
    x_window = getScreenSizeAnswer()[0]
    y_window = getScreenSizeAnswer()[1]
    position_start = getPositionStart(x_window, y_window)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % position_start
    screen = pygame.display.set_mode((x_window,y_window))
    pygame.display.set_caption("Babylon Tower Solver: Answer")
    screen = SetIcon(screen)
    return screen
def runAnswer():
    button_save = components.Button((120, 425), "save")
    button_again = components.Button((120, 550), "again")
    arrow_right  = components.Button((960, 280), "arrow_right")
    arrow_left   = components.Button((598, 280), "arrow_left")
    screen = CreateScreenAnswer()
    answer_table = components.ActualTableSolution()[0]    # 1st table
    components.CreateTowerFromTable(answer_table)       # Create the tower
    print("Answer")
    count = 0
    while (components.Stage() == 3):
        print(count)
        count += 1
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
            button_save.event_handler(event)
            button_again.event_handler(event)
            arrow_right.event_handler(event)
            arrow_left.event_handler(event)
            components.answer_tower.event_handler(event)
        # --- Draws --- #
        SetBackgroundAnswer()
        button_save.draw(screen)
        button_again.draw(screen)
        arrow_right.draw(screen)
        arrow_left.draw(screen)
        components.answer_tower.draw(screen)
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
            


run()



