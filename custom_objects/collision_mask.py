#Made By: Alex Canning
#Date: May 5 2023
#Purpose: Has custom transparency mask model to be called to and used in programs

import pygame
import sys

#Custom object for player sprite
class Mask_class(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,image_load):
        super().__init__() 
        img = pygame.image.load(image_load) 
        self.image = pygame.transform.scale(img, (width, height)).convert_alpha()
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))