import pygame
import random

class enemyImagesheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame, width, height, scale, colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		image.set_colorkey(colour)

		return image


class Enemy(pygame.sprite.Sprite):
    def __init__(self,screenWidth,y,sheet,scale):
        pygame.sprite.Sprite.__init__(self)
        self.moving=random.choice([-1,1])
        self.screenWidth=screenWidth
        if self.moving==1:
            self.flip=True
        else:
            self.flip=False

        image=sheet.get_image(0,32,32,scale,(0,0,0))
        image=pygame.transform.flip(image,self.flip,False)
        image.set_colorkey((0,0,0))
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=0

        if self.moving==1:
            self.rect.x=0
        else:
            self.rect.x=self.screenWidth
        self.rect.y=y

    def update(self,scroll):
        self.rect.x+=self.moving*2
        self.rect.y+=scroll
        if self.rect.right <0 or self.rect.left >self.screenWidth: #check if gone out of screen
            self.kill()




