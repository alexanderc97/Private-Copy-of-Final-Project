import pygame

class Player_class(pygame.sprite.Sprite):
    #Init Sprite  
    dash_timer = 5*30
    direction = 1
    attack = 1
    def __init__(self,startX,startY):
        super().__init__()
        self.img_left = pygame.image.load("sprite_images/player_left.png")
        self.img_left =  pygame.transform.scale(self.img_left , (30, 40)).convert_alpha()
        self.img_right = pygame.image.load("sprite_images/player_right.png")
        self.img_right = pygame.transform.scale(self.img_right , (30, 40)).convert_alpha()
        self.image = self.img_left
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))