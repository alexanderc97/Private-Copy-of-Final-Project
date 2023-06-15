import pygame

class Boss_class(pygame.sprite.Sprite):
    #Init Sprite
    attack_timer = 5*30
    direction = 1
    attack = 1
    def __init__(self,startX,startY):
        super().__init__()
        self.img_left = pygame.image.load("sprite_images/boss_left.png")
        self.img_left =  pygame.transform.scale(self.img_left , (150, 190)).convert_alpha()
        self.img_right = pygame.image.load("sprite_images/boss_right.png")
        self.img_right = pygame.transform.scale(self.img_right , (150, 190)).convert_alpha()
        self.image = self.img_left
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))