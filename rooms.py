#Made By: Alex Canning, Carter Belnap, Hayden
#Date: May 23 2023
#Purpose: Room file, runs all of our combat, shop, and boss rooms.

#Imports
import pygame,sys
from custom_objects.collision_mask import Mask_class
from custom_objects.player import *
from custom_objects.boss import *
from custom_objects.enemy import *

#Pygame Setup
fps=60
pygame.init()
font = pygame.font.Font('ttf/DungeonChunk.ttf', 40)
pause_font = pygame.font.Font('ttf/DungeonChunk.ttf', 50)

#Object setup
collision_mask = pygame.sprite.Group()
player_group = pygame.sprite.Group()
sword_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()

def attack(player):
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            sword_sprite = Sword(player.rect.x+player.direction*15,player.rect.y+10,player.direction)
            sword_group.add(sword_sprite) 

#Pops up a pause menu when in game, this can be used to leave the game or close the menu
def pause_menu(window, fpsClock):
    pause=True
    while pause:
        pause_box=pygame.draw.rect(window,(200,200,200),(300,100,400,500))
        window.blit(pause_font.render("PAUSED", True, (0, 0, 0)), (430, 120))
        btn_title = window.blit(font.render("[Exit to Title]", True, (0, 140, 86)), (387, 280))
        btn_close = window.blit(font.render("[Back to Game]", True, (0, 140, 86)), (385, 380))
        for event in pygame.event.get():
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                sys.exit()
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
                        
                if btn_title.collidepoint(pos):
                    back=True
                    pause=False
                if btn_close.collidepoint(pos):
                    back=False
                    pause=False
                
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw
    return back
    
def scene_room_1(save_slot,window,connection,fpsClock,update_db,player_stats):
    player = Player(200,590,player_stats[0][2])
    player_group.add(player)
    room_1=True
    background_image='images/scene_1_bg.png'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    mask = Mask_class(0,0,1000,700,'masks/scene_1_mask.png')
    collision_mask.add(mask)
    while room_1:
        window.fill((255,255,255))
        collision_mask.draw(window)
        window.blit(background,(0, 0))
        player_group.draw(window)
        sword_group.draw(window)
        for event in pygame.event.get():
    # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                sys.exit()
            sword_group.update(player.rect.y+10,player.rect.x+player.direction*15)
            if len(sword_group)<1:
                attack(player)    
        player.move()
        if pygame.sprite.spritecollide(player, collision_mask, False, collided=pygame.sprite.collide_mask):
                player.collide()     
                
        if player.rect.x>1000-20:
            update_db(connection,"player",["Save_Point='2'"],f"id={save_slot}")
            room_1=False      
        
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_ESCAPE]:  
            back=pause_menu(window, fpsClock)
            if back:
                room_1=False
        else:
            back=False
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw
    collision_mask.remove(mask)
    player_group.remove(player)
    return back
    
def combat_room_1(save_slot,window,connection,fpsClock,update_db,player_stats):
    player = Player(45,240,player_stats[0][2])
    player_group.add(player)
    combat_room_1=True
    background_image='images/zone_1_bg.png'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    mask = Mask_class(0,0,1000,700,'masks/combat_mask.png')
    collision_mask.add(mask)
    while combat_room_1:
        window.fill((255,255,255))
        collision_mask.draw(window)
        window.blit(background,(0, 0))
        player_group.draw(window)
        sword_group.draw(window)
        for event in pygame.event.get():
    # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                sys.exit()
            sword_group.update(player.rect.y+10,player.rect.x+player.direction*15)
            if len(sword_group)<1:
                attack(player)
        player.move()
        if pygame.sprite.spritecollide(player, collision_mask, False, collided=pygame.sprite.collide_mask):
                player.collide()
        
        if player.rect.x>1000-20:
            update_db(connection,"player",["Save_Point='3'"],f"id={save_slot}")
            combat_room_1=False        
        
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_ESCAPE]:  
            back=pause_menu(window, fpsClock)
            if back:
                combat_room_1=False
        else:
            back=False
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw
    collision_mask.remove(mask)
    player_group.remove(player)
    return back

def shop_room_1(save_slot,window,connection,fpsClock,update_db,player_stats):
    player = Player(45,240,player_stats[0][2])
    player_group.add(player)
    background_image='images/shop_bg.png'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    mask = Mask_class(0,0,1000,700,'masks/shop_mask.png')
    collision_mask.add(mask)
    shop_room_1=True
    while shop_room_1:
        window.fill((255,255,255))
        collision_mask.draw(window)
        window.blit(background,(0, 0))
        player_group.draw(window)
        sword_group.draw(window)
        for event in pygame.event.get():
    # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                sys.exit()
            sword_group.update(player.rect.y+10,player.rect.x+player.direction*15)
            if len(sword_group)<1:
                attack(player)
        player.move()
        if pygame.sprite.spritecollide(player, collision_mask, False, collided=pygame.sprite.collide_mask):
                player.collide()      
        
        if player.rect.x>1000-20:
            update_db(connection,"player",["Save_Point='4'"],f"id={save_slot}")
            shop_room_1=False      
        
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_ESCAPE]:  
            back=pause_menu(window, fpsClock)
            if back:
                shop_room_1=False
        else:
            back=False  
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw
    collision_mask.remove(mask)
    player_group.remove(player)
    return back
def boss_room_1(save_slot,window,connection,fpsClock,update_db,player_stats):
    player = Player(45,240,player_stats[0][2])
    player_group.add(player)
    boss = Boss_class(420, 210,3,'sprite_images/boss_left.png','sprite_images/boss_right.png',150,190,120)
    boss_group.add(boss)
    boss_room_1=True
    background_image='images/zone_1_bg.png'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    mask = Mask_class(0,0,1000,700,'masks/combat_mask.png')
    collision_mask.add(mask)
    while boss_room_1:
        window.fill((255,255,255))
        collision_mask.draw(window)
        window.blit(background,(0, 0))
        player_group.draw(window)
        sword_group.draw(window)
        boss_group.draw(window)
        for event in pygame.event.get():
    # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                sys.exit()
            sword_group.update(player.rect.y+10,player.rect.x+player.direction*15)
            if len(sword_group)<1:
                attack(player)
        player.move()
        if pygame.sprite.spritecollide(player, collision_mask, False, collided=pygame.sprite.collide_mask):
                player.collide() 
        
        if player.rect.x>1000-20:
            update_db(connection,"player",["Save_Point='5'"],f"id={save_slot}")
            boss_room_1=False   
        
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_ESCAPE]:  
            back=pause_menu(window, fpsClock)
            if back:
                boss_room_1=False
        else:
            back=False     
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw
    collision_mask.remove(mask)
    player_group.remove(player)
    return back
def final_scene_room(save_slot,window,connection,fpsClock,update_db):
    final_scene_room=True
    while final_scene_room:
        window.fill((0,0,0))
        for event in pygame.event.get():
    # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                sys.exit()
        window.blit(font.render("To be Continued in...", True, (225,225,225)), (350, 250))
        window.blit(font.render("Shadows of the Forgotten: Ancient Shadows DLC", True, (225,225,225)), (100, 300))
        window.blit(font.render("Preorder: $79.99", True, (0,150,0)), (375, 400))
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw
        
