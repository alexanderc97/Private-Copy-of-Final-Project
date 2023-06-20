import pygame

class Player(pygame.sprite.Sprite):
    #Init Sprite  
    dash_timer = 10*30
    direction = 1
    attack = 1
    def __init__(self,startX,startY,health):
        super().__init__()
        self.img_left = pygame.image.load("sprite_images/PlayerL.png")
        self.img_left =  pygame.transform.scale(self.img_left , (30, 40)).convert_alpha()
        self.img_right = pygame.image.load("sprite_images/PlayerR.png")
        self.img_right = pygame.transform.scale(self.img_right , (30, 40)).convert_alpha()
        self.image = self.img_left
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.health = health
    #Basic Movement
    def move(self):
        self.dash_timer -=1
        global key_input, t_f_list
        t_f_list = {True : 1, False: 0}
        key_input = pygame.key.get_pressed() 
        self.movex = (t_f_list[key_input[pygame.K_a]] * -3) + (t_f_list[key_input[pygame.K_d]] * 3)
        self.movey = (t_f_list[key_input[pygame.K_w]] * -3) + (t_f_list[key_input[pygame.K_s]] * 3)

    #Dashing Movement
        if pygame.key.get_mods() & pygame.KMOD_SHIFT and (key_input[pygame.K_w] or key_input[pygame.K_s]) and self.dash_timer<0:
            self.movey *=15
            self.dash_timer = 10*30

        if pygame.key.get_mods() & pygame.KMOD_SHIFT and (key_input[pygame.K_a] or key_input[pygame.K_d]) and self.dash_timer<0:
            self.movex *=15
            self.dash_timer = 10*30
            
    #Changing masked images from left to right
        if key_input[pygame.K_a]:
            self.direction = -1
            self.image = self.img_right
            self.mask  = pygame.mask.from_surface(self.image)
            
        if key_input[pygame.K_d]:
            self.direction = 1
            self.image = self.img_left
            self.mask  = pygame.mask.from_surface(self.image)
            
        self.rect.y += self.movey
        self.rect.x += self.movex 
        
    #Object Collision
    def collide(self):
        self.rect.x -= self.movex
        self.rect.y -= self.movey
        
    #Lower player health from enemy 
    def health_lower(self,enemy_dmg):
        self.health -= enemy_dmg
        if self.health <= 0:
            self.kill() 
                  
class Sword(pygame.sprite.Sprite):
    timer=20
    sword_move=0
    #Basic Init
    def __init__(self,startX,startY,direction):
        super().__init__()
        self.img_left = pygame.image.load("sprite_images/SwordL.png")
        self.img_left =  pygame.transform.scale(self.img_left , (30, 10)).convert_alpha()
        self.img_right = pygame.image.load("sprite_images/SwordR.png")
        self.img_right = pygame.transform.scale(self.img_right , (30, 10)).convert_alpha()
        self.image = self.img_left
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
        self.direction = direction
        
        if direction==1:
            self.image = self.img_right
            self.mask  = pygame.mask.from_surface(self.image)
        if direction==-1:
            self.image = self.img_left
            self.mask  = pygame.mask.from_surface(self.image)
            
    #Sword update method to follow player when stabbing and also moving        
    def update(self,y,x,enemy,enemy_count):
        self.timer-=1

        if self.direction ==1:
            speed = 1
        else:
            speed = -1

        if self.timer<=10:
            speed = -speed
            
        self.rect.y = y
        self.rect.x = x
        self.sword_move +=4*speed
        self.rect.x += self.sword_move
        if self.timer==0:
            self.kill()
        self.collision(enemy,enemy_count)
         
    #SWORD collide with ENEMY      
    def collision(self,enemy,enemy_count):
        collided_sprites = pygame.sprite.spritecollide(self, enemy, False, collided=pygame.sprite.collide_mask)
        if len(collided_sprites) >0:
             collided_sprites[0].health_lower(10,enemy_count)
             self.kill()
