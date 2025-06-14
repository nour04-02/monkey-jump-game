
import pygame
from pygame import mixer
mixer.init()
jump_sound = pygame.mixer.Sound("pics/cartoon-jump-6462.mp3")
jump_sound.set_volume(0.5)


class MonkeyPlayerclass:
    def __init__(self, x, y,monkeyImagem,screenWidth,platformGroup,window):
        image=pygame.transform.scale(monkeyImagem,(50,63))
        self.image = image
        self.width = 40
        self.height = 60
        self.flip = False
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.velocityVertica = 0
        self.screenWidth=screenWidth
        self.platformGroup=platformGroup
        self.window=window


    def draw(self):
        self.window.blit(pygame.transform.flip(self.image, self.flip, False, ),
                    (self.rect.x - 10, self.rect.y))  # -10 to center the monkey inside the rectangle


    def move(self):
        varX = 0
        VarY = 0
        scroll = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            varX -= 5
            self.flip = True
        if key[pygame.K_RIGHT]:
            varX += 5
            self.flip = False

        self.velocityVertica += 1
        VarY += self.velocityVertica


        if self.rect.left + varX < 0:
            varX = self.rect.left

        for platform in self.platformGroup:
            if platform.rect.colliderect(self.rect.x, self.rect.y + VarY, self.width,
                                         self.height):

                if self.rect.bottom < platform.rect.centery:
                    if self.velocityVertica > 0:
                        self.rect.bottom = platform.rect.top
                        jump_sound.play()
                        VarY = 0
                        self.velocityVertica = -22


        if self.rect.right + varX > self.screenWidth:
            varX = self.screenWidth - self.rect.right



        if self.rect.top <= 200:
            if self.velocityVertica < 0:
                scroll = -VarY

        self.rect.x += varX
        self.rect.y += VarY + scroll
        return scroll
