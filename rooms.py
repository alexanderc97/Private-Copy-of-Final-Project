#Made By: Alex Canning, Carter Belnap, Hayden
#Date: May 23 2023
#Purpose: Room file, runs all of our combat, shop, and boss rooms.

#Imports
import pygame,sys
from custom_objects.collision_mask import Mask_class
from custom_objects.player import *
#from player import Player_class

#Pygame Setup
fps=60
pygame.init()
font = pygame.font.Font('ttf/DungeonChunk.ttf', 40)

#Object setup
collision_mask = pygame.sprite.Group()
player_group = pygame.sprite.Group()
sword_group=pygame.sprite.Group()


    
def attack():
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            sword_sprite = Sword(player.rect.x+player.direction*15,player.rect.y+10,player.direction)
            sword_group.add(sword_sprite)    

def scene_room_1(save_slot,window,connection,fpsClock,update_db):
    player = Player_class(100,100)
    player_group.add(player)
    room_1=True
    background_image='images/scene_1_bg.png'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    collision_mask.remove(mask)
    mask = Mask_class(0,0,1000,700,'masks/scene_1_mask.png')
    collision_mask.add(mask)
    while room_1:
        window.fill((255,255,255))
        player_group.draw(window)
        sword_group.draw(window)
        collision_mask.draw(window)
        window.blit(background,(0, 0))
        for event in pygame.event.get():
    # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                sys.exit()
            player.move()
            sword_group.update(player.rect.y+10,player.rect.x+player.direction*15)
            if len(sword_group)<1:
                attack()
        if pygame.sprite.spritecollide(player, collision_mask, False, collided=pygame.sprite.collide_mask):
            player.rect.x-=player.x
        
            
            
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw
    
def combat_room_1(save_slot,window,connection,fpsClock,update_db):
    combat_room_1=True
    background_image='images/zone_1_bg.png'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    collision_mask.remove(mask)
    mask = Mask_class(0,0,1000,700,'masks/combat_mask_1.png')
    collision_mask.add(mask)
    while combat_room_1:
        window.fill((255,255,255))
        window.blit(background,(0, 0))
        player_group.draw(window)
        sword_group.draw(window)
        window.blit(background,(0, 0))
        if pygame.sprite.spritecollide(player, collision_mask, False, collided=pygame.sprite.collide_mask):
            player.rect.x-=player.x
        
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw

def shop_room_1(save_slot,window,connection,fpsClock,update_db,new):
    if new:
        update_db(connection,"player",["Save_Point"],[2])
    background_image='images/shop_bg.png'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    shop_room_1=True
    while shop_room_1:
        window.fill((255,255,255))
        window.blit(background,(0, 0))
        
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw
    
def boss_room_1(save_slot,window,connection,fpsClock,update_db):
    boss_room_1=True
    background_image='images/zone_1_bg.png'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    collision_mask.remove(mask)
    mask = Mask_class(0,0,1000,700,'masks/combat_mask_1.png')
    collision_mask.add(mask)
    while boss_room_1:
        window.fill((255,255,255))
        window.blit(background,(0, 0))
        #if pygame.sprite.spritecollide(player, collision_mask, False, collided=pygame.sprite.collide_mask):
          #  player.rect.x-=player.x
        
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw
    
def scene_room_2(save_slot,window,connection,fpsClock,update_db,new):
    if new:
        update_db(connection,"player",["Save_Point"],[3])
    background_image='images/zone_2_bg.png'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    scene_room_2=True
    collision_mask.remove(mask)
    mask = Mask_class(0,0,1000,700,'masks/scene_2_mask.png')
    collision_mask.add(mask)
    while scene_room_2:
        window.fill((255,255,255))
        window.blit(background,(0, 0))
       # if pygame.sprite.spritecollide(player, collision_mask, False, collided=pygame.sprite.collide_mask):
          #  player.rect.x-=player.x
    

        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw
    
def combat_room_2(save_slot,window,connection,fpsClock,update_db):
    combat_room_2=True
    background_image='images/zone_2_bg.png'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    collision_mask.remove(mask)
    mask = Mask_class(0,0,1000,700,'masks/combat_mask_2.png')
    collision_mask.add(mask)
    while combat_room_2:
        window.fill((255,255,255))
        window.blit(background,(0, 0))
        if pygame.sprite.spritecollide(player, collision_mask, False, collided=pygame.sprite.collide_mask):
            player.rect.x-=player.x

        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw

def mini_boss_room(save_slot,window,connection,fpsClock,update_db):
    mini_boss_room=True
    background_image='images/zone_2_bg.png'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    collision_mask.remove(mask)
    mask = Mask_class(0,0,1000,700,'masks/combat_mask_2.png')
    collision_mask.add(mask)
    while mini_boss_room:
        window.fill((255,255,255))
        window.blit(background,(0, 0))
       # if pygame.sprite.spritecollide(player, collision_mask, False, collided=pygame.sprite.collide_mask):
        #    player.rect.x-=player.x
        
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw

def shop_room_2(save_slot,window,connection,fpsClock,update_db,new):
    if new:
        update_db(connection,"player",["Save_Point"],[4])
    background_image='images/shop_bg.png'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    shop_room_2=True
    while shop_room_2:
        window.fill((255,255,255))
        window.blit(background,(0, 0))
        
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw

def boss_room_2(save_slot,window,connection,fpsClock,update_db):
    boss_room_2=True
    background_image='images/zone_2_bg.png'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    collision_mask.remove(mask)
    mask = Mask_class(0,0,1000,700,'masks/combat_mask_2.png')
    collision_mask.add(mask)
    while boss_room_2:
        window.fill((255,255,255))
        window.blit(background,(0, 0))
       # if pygame.sprite.spritecollide(player, collision_mask, False, collided=pygame.sprite.collide_mask):
        #    player.rect.x-=player.x
        
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw

def final_scene_room(save_slot,window,connection,fpsClock,update_db,new):
    if new:
        update_db(connection,"player",["Save_Point"],[5])
    final_scene_room=True
    background_image='images/final_scene_bg.png'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    collision_mask.remove(mask)
    mask = Mask_class(0,0,1000,700,'masks/final_scene_mask.png')
    collision_mask.add(mask)
    while final_scene_room:
        window.fill((255,255,255))
        window.blit(background,(0, 0))
      #  if pygame.sprite.spritecollide(player, collision_mask, False, collided=pygame.sprite.collide_mask):
       #     player.rect.x-=player.x
        
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw