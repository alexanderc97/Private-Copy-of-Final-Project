import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self,startX,startY,timer,image_left,image_right,width,height,health):
        super().__init__()
        self.timer = timer
        self.reset = timer
        self.health = health
        self.img_left = pygame.image.load(image_left)
        self.img_left =  pygame.transform.scale(self.img_left , (width, height)).convert_alpha()
        self.img_right = pygame.image.load(image_right)
        self.img_right = pygame.transform.scale(self.img_right , (width, height)).convert_alpha()
        self.image = self.img_left
        self.mask  = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(topleft=(startX,startY))
      
    def move(self,x,y):
       self.rect.x += x
       self.rect.y += y
       
    def track(self,x,y):
        self.timer -=1 
        if self.timer <= 0:
            self.timer = self.reset
        #ENEMY tracking PLAYER
            if self.rect.x > x:
                self.move(-1,0)
                self.image = self.img_right
            if self.rect.x < x:
                self.move(1,0)
                self.image = self.img_left
            if self.rect.y > y:
                self.move(0,-1)
            if self.rect.y < y:
                self.move(0,1)
    
    #Collision update method
    def update(self,player,enemy_dmg):
      self.collision(player,enemy_dmg)

    #ENEMY collide with PLAYER   
    def collision(self,player,enemy_dmg):
        collided_sprites = pygame.sprite.spritecollide(self, player, False, collided=pygame.sprite.collide_mask)
        if len(collided_sprites) >0:
            collided_sprites[0].health_lower(enemy_dmg)
            
            
            
    #Enemy health lower when hit by sword
    def health_lower(self,sword_dmg,enemy_count):
        self.health -= sword_dmg
        if self.health <= 0:
            self.kill()
            enemy_count -=1
            
class Enemy_bullet(pygame.sprite.Sprite):
    def __init__(self, startX,startY,width,height,color):
        super().__init__()
        self.image = pygame.Surface([width, height],pygame.SRCALPHA).convert_alpha()
        pygame.draw.rect(self.image,(color),(0,0,width,height))
        self.rect = self.image.get_rect(topleft =(startX,startY))
        self.mask = pygame.mask.from_surface(self.image)
   
    def update(self,collision_mask,player_group,enemy_dmg,player,direction):
        self.shoot(collision_mask,player_group,enemy_dmg,player,direction)
           
    def shoot(self,collision_mask,player_group,enemy_dmg,player,direction):
       
        if pygame.sprite.spritecollide(self, collision_mask, False, collided=pygame.sprite.collide_mask):
            self.kill()
        if pygame.sprite.spritecollide(self, player_group, False, collided=pygame.sprite.collide_mask):
            player.health_lower(enemy_dmg)
            self.kill()
        if direction == 1:
            self.rect.y+=4
        elif direction == 2:
            self.rect.y-=4
        elif direction == 3:
            self.rect.x+=4
        elif direction == 4:
            self.rect.x-=4
