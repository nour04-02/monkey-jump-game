#nour abu bayder
#166542


import pygame
from MonkeyPlayer import MonkeyPlayerclass
from PlatForms import Platform
from Enemy import *
import random

pygame.init()

height = 610
width = 420
tickingC = pygame.time.Clock()
framerate = 60

# gravity
numberOfplatforms = 10
scroll = 0
score = 0
highScoreVariable = 0
animateCounter = 0
f=open("highScore.txt","r")
highScoreVariable=int(f.read())
falls = False
backgroundscroll = 0
window = pygame.display.set_mode((width, height))


run = True

pygame.display.set_caption("MONKEY JUMP Game")

background = pygame.image.load("pics/back1.jpg").convert_alpha()
MonkeyImage = pygame.image.load("pics/nope1.png").convert_alpha()
floor_image = pygame.image.load("pics/floor.png").convert_alpha()
enemy = pygame.image.load("pics/enemy.png").convert_alpha()
fontsSmall=pygame.font.SysFont("Lucida Sans",22)
fontBig=pygame.font.SysFont("Lucida Sans",26)
enemysheet=enemyImagesheet(enemy)



# creating starting platform
platform_group = pygame.sprite.Group()
platform = Platform(width // 2 - 50, height - 90, 85, False, floor_image, height)
platform_group.add(platform)
player = MonkeyPlayerclass(width // 2, height - 150, MonkeyImage, width, platform_group, window)

enemy_group = pygame.sprite.Group()


def placetextinWindow(text, font, textcol, x, y):
    img = font.render(text, True, textcol)
    window.blit(img, (x, y))





def drawGameOver():
    placetextinWindow("Game Over!", fontBig, (255, 0, 0), 130, 200)
    placetextinWindow("SCORE " + str(score), fontBig, (255, 255, 0), 130, 250)
    placetextinWindow("press space to play again", fontBig, (0, 0, 255), 40, 350)
    placetextinWindow("High score :" + str(highScoreVariable), fontBig, (0, 255, 0), 130, 300)



while run:

    tickingC.tick(framerate)
    if not falls:

        scroll=player.move()
        if backgroundscroll>=610:

            backgroundscroll+=scroll
        window.blit(background, (0, backgroundscroll))

        if len(platform_group) < numberOfplatforms:
            platformRandomWidth=random.randint(60, 100)
            positionX=random.randint(0, width - platformRandomWidth)
            positionY=platform.rect.y -random.randint(70,105)
            platformType=random.randint(0,1)
            if platformType==0:
                platformMoving=True
            else:
                platformMoving=False
            if score>100:
                platform = Platform(positionX, positionY, platformRandomWidth, platformMoving, floor_image, height)
            else:
                platform = Platform(positionX, positionY, platformRandomWidth, False, floor_image, height)








            platform_group.add(platform)



        platform_group.update(scroll)
        #generate enemy
        if len(enemy_group)==0 and score >150:
            enemy=Enemy(width, 100, enemysheet, 1.2)
            enemy_group.add(enemy)
        enemy_group.update(scroll)

        if scroll>0:
            score+=1


        pygame.draw.line(window, (0,255,0), (0, score - highScoreVariable + 200), (width, score - highScoreVariable + 200), 2)
        placetextinWindow("HIGH SCORE " + str(highScoreVariable), fontsSmall, (0, 0, 0), width - 200, score - highScoreVariable + 200)
        platform_group.draw(window)

        enemy_group.draw(window)

        player.draw()

        placetextinWindow("score " + str(score), fontsSmall, (0, 0, 0), 0, 0)

        if player.rect.top>height:
            falls=True

        if pygame.sprite.spritecollide(player,enemy_group,False):
            falls=True
    else:
        if animateCounter<width:
            animateCounter+=12
            pygame.draw.rect(window, (0,0,0), (0, 0, animateCounter, height))


        drawGameOver()



        if score>highScoreVariable:
            highScoreVariable=score

            f=open("highScore.txt","w")
            f.write(str(highScoreVariable))
            f.close()


        if pygame.key.get_pressed()[pygame.K_SPACE]:
            falls=False
            score=0
            scroll=0
            animateCounter=0

            player.rect.center=(width // 2, height - 150)

            platform_group.empty()
            enemy_group.empty()

            platform = Platform(width // 2 - 50, height - 100, 80, False, floor_image=floor_image, screenHeight=height)
            platform_group.add(platform)


    for x in pygame.event.get():
        if x.type ==pygame.QUIT:
            run=False


    #update window
    pygame.display.update()

