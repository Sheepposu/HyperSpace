#Imports
import pygame
import time
import random
import pickle
from pathlib import Path


pygame.init()

#Sounds


#Variables/Shortcuts
d = Path().resolve().parent
fileO = open(str(d) + '/HyperSpace!/HyperSpace Stuff/HyperSpaceData.txt', 'rb')
HighScore = pickle.load(fileO)
OrHighScore = HighScore
pd = pygame.display
fps = 100
display_width = 1000
display_height = 600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
darker_red = (200,0,0)
green = (0,255,0)
blue = (0,0,255)
ColorList = [black, red, green, blue]
CustomColor1 = (48,150,140)
CustomColor2 = (36,112.5,105)
CustomColor3 = (0,0,0)
Unique_Color = (190,140,210)
Score = 0
carImg = pygame.image.load(str(d) + '/HyperSpace!/HyperSpace Stuff/RaceCar.png')
carImgLeft = pygame.image.load(str(d) + '/HyperSpace!/HyperSpace Stuff/RaceCarLeft.png')
carImgRight = pygame.image.load(str(d) + '/HyperSpace!/HyperSpace Stuff/RaceCarRight.png')
car_width = 55
car_height = 50

#Game Start up
gD = pygame.display.set_mode((display_width,display_height))

#Game Conifgurations
pd.set_caption('HyperSpace!')
clock = pygame.time.Clock()
gD.fill(white)

#Functions
def car(img, x, y):
    gD.blit(img, (x,y))

def CrashDisplay(score, val):
    gD.fill(random.choice(ColorList))
    
    if val == True:
        message_display('You Crashed. Your Score was %s' %score)
        time.sleep(10)
    else:
        message_display2('Your score is - %s - Highscore is %s' %(score, HighScore))
    
def message_display(text):
    font = pygame.font.SysFont('arial', 50)
    textSurf, TextRect = text_objects(text, font)
    TextRect.center = ((display_width/2),(display_height/2))
    gD.blit(textSurf, TextRect)

    pygame.display.update()

    time.sleep(10)

def message_display2(text):
    font = pygame.font.SysFont('arial', 30)
    textSurf, TextRect = text_objects(text, font)
    TextRect.center = ((display_width/2),(20))
    gD.blit(textSurf, TextRect)
    pygame.display.update()
    
def ScoreKeeper(pts):
    global Score
    Score += pts

def text_objects(text, font):
    textSurface = font.render(text, True, Unique_Color)
    return textSurface, textSurface.get_rect()

def obstacle(obstX, obstY, obstW, obstH, color):
    pygame.draw.rect(gD, color, [obstX, obstY, obstW, obstH])

def pyquit():
    pygame.quit()

def pythquit():
    quit()
    
def StartScreen():
    intro = True

    while intro == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gD.fill(white)
        font = pygame.font.SysFont('arial', int(display_width/10))
        textSurf, TextRect = text_objects('HyperSpace!', font)
        TextRect.center = ((display_width/2),(display_height/2))
        gD.blit(textSurf, TextRect)
        Button(round(display_width * .3), round(display_height * .7), round(display_width * .4), round(display_height * .2), CustomColor1, CustomColor2, 'Start!', 50, blue, 'arial', game_loop)
        Button(round(display_width * .8), round(display_height * .8), round(display_width * .2), round(display_height * .1), red, darker_red, "Quit", 20, blue, 'arial', highDump, pythquit, pyquit)
        pygame.display.update()
        clock.tick(15)

def Button(Butx, Buty, Butx2, Buty2, Butcolor, ShadowColor, text, textsize, textcolor, textFont, command=None, command2=None, command3=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    smallText = pygame.font.SysFont(textFont, textsize)
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ((Butx + (Butx2/2)), Buty + (Buty2/2))
    pygame.draw.rect(gD, Butcolor, (Butx, Buty, Butx2, Buty2))
    gD.blit(textSurf, textRect)
    if Butx + Butx2 > mouse[0] > Butx and Buty + Buty2 > mouse[1] > Buty: 
        pygame.draw.rect(gD, ShadowColor, (Butx, Buty, Butx2, Buty2))
        gD.blit(textSurf, textRect)
        if click[0] == 1:
            if command != None:
                command()
            if command2 != None:
                command2()
            if command3 != None:
                command3()
    else:
        pygame.draw.rect(gD, Butcolor, (Butx, Buty, Butx2, Buty2))
        gD.blit(textSurf, textRect)

def highDump():
    if HighScore > OrHighScore:
        file = open(str(d) + '/HyperSpace!/HyperSpace Stuff/HyperSpaceData.txt', 'wb')
        pickle.dump(HighScore, file)
        file.close()

def Pause():
    pause = True
    message_display('Game is Paused')
    while pause:
         for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
#Main
def game_loop():
    global carImg
    play = True
    global Score
    x = (display_width * 0.5)
    y = (display_height * 0.8)

    x_change = 0
    

    obst_startX = random.randint(0, display_width)
    obst_startY = -600
    obst_speed = 2
    min_width = 100
    max_width = 100
    obst_width = 0
    obst_height = 0
    obst_height = random.randint(round(display_width/8), round(display_width/2))
    obst_color = random.choice(ColorList)

    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                StartScreen()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -5
                    carImg = pygame.image.load(str(d) + '/HyperSpace!/HyperSpace Stuff/RaceCarLeft.png')
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = +5
                    carImg = pygame.image.load(str(d) + '/HyperSpace!/HyperSpace Stuff/RaceCarRight.png')
                elif event.key == pygame.K_p:
                    Pause()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_d or event.key == pygame.K_a:
                    x_change = 0
                    carImg = pygame.image.load(str(d) + '/HyperSpace!/HyperSpace Stuff/RaceCar.png')
                
        Score += 1
        x += x_change

        CrashDisplay(Score, False)
        obstacle(obst_startX, obst_startY, random.randint(min_width, max_width), obst_height, obst_color)
        
        obst_startY += obst_speed
        car(carImg, x, y)

        if x > display_width - 76 or x < -5:
            CrashDisplay(Score, True)
            StartScreen()

        if obst_startY > display_height:
            obst_startY = 0 - obst_height
            obst_startX = random.randint(0, display_width)
            obst_width = random.randint(min_width, max_width)
            obst_height = random.randint(round(display_width/8), round(display_width/2))
            obst_color = random.choice(ColorList)
            min_width += 10
            max_width += 11
        if y <= obst_startY + obst_height:
            if x > obst_startX and x < obst_startX + obst_width or x + car_width > obst_startX and x + car_width < obst_startX + obst_width:
                CrashDisplay(Score, True)
                StartScreen()


        if Score == 2000:
            obst_speed = 3

        elif Score == 4000:
            obst_speed = 4

        elif Score == 6000:
            obst_speed = 5

        elif Score == 8000:
            obst_speed = 6

        elif Score == 10000:
            obst_speed = 7

        elif Score == 12000:
            obst_speed = 8

        elif Score == 14000:
            obst_speed = 9

        elif Score == 16000:
            obst_speed = 10

        elif Score == 18000:
            obst_speed = 11

        elif Score == 20000:
            obst_speed = 12
        pygame.display.update()
        clock.tick(fps)
StartScreen()
highDump()
pygame.quit()
quit()
