#Made By: Alex Canning, Carter Belnap, Hayden
#Date: May 23 2023
#Purpose: Menu file to run all of our menus, including save slot screen and opening sequence.

import pygame,sys
fps=60
pygame.init()
font = pygame.font.Font('ttf/DungeonChunk.ttf', 30)
#Title screen display
def title_screen(window,fpsClock):
    title_window=True
    while title_window:
        window.fill((255,255,255))
        btn_exit = window.blit(font.render("[Exit]", True, (200, 0, 255)), (445, 500))
        btn_newgame = window.blit(font.render("[Play Game]", True, (200, 0, 255)), (440, 300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                
                if btn_exit.collidepoint(pos):
                    pygame.quit()
                    sys.exit() 
                if btn_newgame.collidepoint(pos):
                    title_window=False
                    
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw
def save_slot_screen(window,connection,select_db,fpsClock):
    save_slot=0
    save_slot_window=True
    id_1_check=len(select_db(connection,"player",["id='1'"]).fetchall())
    id_2_check=len(select_db(connection,"player",["id='2'"]).fetchall())
    id_3_check=len(select_db(connection,"player",["id='3'"]).fetchall())
    id_1_stats=select_db(connection,"player",["id='1'"]).fetchall()
    id_2_stats=select_db(connection,"player",["id='2'"]).fetchall()
    id_3_stats=select_db(connection,"player",["id='3'"]).fetchall()
    while save_slot_window:
        window.fill((255,255,255))
        window.blit(font.render("Select a Save Slot", True, (0, 0, 0)), (345, 75))
        save_box1=pygame.draw.rect(window,(0,0,0),(250,120,500,130))
        save_box2=pygame.draw.rect(window,(0,0,0),(250,320,500,130))
        save_box3=pygame.draw.rect(window,(0,0,0),(250,520,500,130))
        if id_1_check==1:
            save_box_text1=window.blit(font.render(f"1.{id_1_stats[0][1]}", True, (255, 255, 255)), (275, 170))
            window.blit(font.render(f"Coins:{id_1_stats[0][3]}", True, (255, 255, 255)), (590, 170))
        else:
            save_box_text1=window.blit(font.render("New Game", True, (255, 255, 255)), (435, 170))
            
        if id_2_check==1:
            save_box_text2=window.blit(font.render(f"2.{id_2_stats[0][1]}", True, (255, 255, 255)), (275, 370))
            window.blit(font.render(f"Coins:{id_2_stats[0][3]}", True, (255, 255, 255)), (590, 370))
        else:
            save_box_text2=window.blit(font.render("New Game", True, (255, 255, 255)), (435, 370))
            
        if id_3_check==1:
            save_box_text3=window.blit(font.render(f"3.{id_3_stats[0][1]}", True, (255, 255, 255)), (275, 570))
            window.blit(font.render(f"Coins:{id_3_stats[0][3]}", True, (255, 255, 255)), (590, 570))
        else:
            save_box_text3=window.blit(font.render("New Game", True, (255, 255, 255)), (435, 570))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    
                if save_box1.collidepoint(pos) and id_1_check==0:
                    save_slot=1
                    new=True
                    save_slot_window=False
                    
                elif save_box2.collidepoint(pos) and id_2_check==0:
                    save_slot=2
                    new=True
                    save_slot_window=False
                    
                elif save_box3.collidepoint(pos) and id_3_check==0:
                    save_slot=3
                    new=True
                    save_slot_window=False
                    
                    
                if save_box1.collidepoint(pos) and id_1_check==1:
                    save_slot=1
                    new=False
                    save_slot_window=False
                    
                elif save_box2.collidepoint(pos) and id_2_check==1:
                    save_slot=2
                    new=False
                    save_slot_window=False
                    
                elif save_box3.collidepoint(pos) and id_3_check==1:
                    save_slot=3
                    new=False
                    save_slot_window=False
            
                       
                                                                  
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw 
    return save_slot,new
def opening_text(window, connection, insert_db, fpsClock,save_slot):
    timer= 300
    while timer > 0:
        window.fill((0,0,0))
        start_text=window.blit(font.render("In the depths of an underground realm, a new species", True, (225,225,225)), (25, 25))
        start_text=window.blit(font.render("called Luminari has emerged. They possess the ability", True, (225,225,225)), (25, 75))
        start_text=window.blit(font.render("to mimic languages and lack the need for food. Nobody", True, (225,225,225)), (25, 125))
        start_text=window.blit(font.render("true strength or where they come from. Luminari have", True, (225,225,225)), (25, 175))
        start_text=window.blit(font.render("started leaving the safety of the underworld and", True, (225,225,225)), (25, 225))
        start_text=window.blit(font.render("venturing to the surface, a place where all life", True, (225,225,225)), (25, 275))
        start_text=window.blit(font.render("perishes. You awaken in a cavern, feeling weak and ", True, (225,225,225)), (25, 325))
        start_text=window.blit(font.render("fragmented, driven by an unknown impulse to reach ", True, (225,225,225)), (25, 375))
        start_text=window.blit(font.render("As a Luminari, you embark on a journey through ", True, (225,225,225)), (25, 425))
        start_text=window.blit(font.render("treacherous zones, facing waves of enemies, uncovering ", True, (225,225,225)), (25, 475))
        start_text=window.blit(font.render("the truth about your past, and battling powerful bosses.  ", True, (225,225,225)), (25, 525))
        start_text=window.blit(font.render("Are you ready to explore, fight, and discover the ", True, (225,225,225)), (25, 575))
        start_text=window.blit(font.render("secrets that await in this captivating underground world?", True, (225,225,225)), (25, 625))

        
        timer-=1
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw
    start_text=window.blit(font.render("", True, (0,0,0)), (285, 175))

def opening_game_screen(window,connection,insert_db,fpsClock,save_slot):
    opening_window=True
    first_run=1
    name=""
    name_position=515
    typing=False
    while opening_window:
        window.fill((0,0,0))
        window.blit(font.render("What is your name, Wanderer?", True, (255, 255, 255)), (285, 175))
        text_box=pygame.draw.rect(window,(255,255,255),(285,220,465,100))
        window.blit(font.render(f"{name.upper()}", True, (0, 0, 0)), (name_position, 255))
        btn_confirm=window.blit(font.render("CONFIRM", True, (255, 255, 255)), (455, 350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and text_box.collidepoint(pos):
                typing=True  
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not text_box.collidepoint(pos):
                typing=False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:    
                if btn_confirm.collidepoint(pos) and len(name)>=1:
                    opening_window=False
                    insert_db(connection,"player",["id","Name","Health","Coins","Weapon_LVL","Save_Point"],[save_slot,name.upper(),100,0,1,1])
                
            if typing:
                if event.type == pygame.KEYDOWN:
                    key=(pygame.key.name(event.key))   
                    if key=="backspace":
                        name_position+=8
                        name=name[:-1]
                    if len(name)<15:
                        if key=="space":
                            name_position-=8
                            name+=" "
                        elif len(key)>1:
                            name=name
                        else:
                            name_position-=8
                            name+=key
              
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw