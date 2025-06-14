import pygame
import random



class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y,w,moving,floor_image,screenHeight):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(floor_image,(w,12))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.moving=moving
        self.moving_counter=random.randint(0,50)
        self.dir=random.choice([-1,1])
        self.screenHeight=screenHeight




    def update(self,scroll):
        if self.moving:
            self.moving_counter+=1
            self.rect.x+=self.dir
        if self.moving_counter>=150:
            self.dir=self.dir*-1
            self.moving_counter=0


        #update  floores
        self.rect.y+=scroll

        # check platform gone out of scree
        if self.rect.top > self.screenHeight:
            self.kill()
