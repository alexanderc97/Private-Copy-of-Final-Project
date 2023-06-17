#Made By: Alex Canning, Carter Belnap, Hayden
#Date: May 23 2023
#Purpose: Menu file to run all of our menus, including save slot screen and opening sequence.

import pygame,sys
fps=60
pygame.init()
font = pygame.font.Font('ttf/DungeonChunk.ttf', 30)
title_font = pygame.font.Font('ttf/DungeonChunk.ttf', 70)
title_buttons_font = pygame.font.Font('ttf/DungeonChunk.ttf', 50)

#Title screen display   
def title_screen(window,fpsClock):
    title_window=True
    background_image='images/title_background.jpg'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    while title_window:
        window.fill((0,0,0))
        window.blit(background,(0, 0))
        window.blit(title_font.render("Shadows of the", True, (255, 255, 255)), (310, 100))
        window.blit(title_font.render("Forgotten", True, (255, 255, 255)), (380, 170))
        btn_exit = window.blit(title_buttons_font.render("[Exit]", True, (27, 228, 147)), (455, 550))
        btn_controls = window.blit(title_buttons_font.render("[Controls]", True, (27, 228, 147)), (410, 450))
        btn_newgame = window.blit(title_buttons_font.render("[Play Game]", True, (27, 228, 147)), (400, 350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                
                if btn_controls.collidepoint(pos):
                    control_screen(window, fpsClock)
                if btn_exit.collidepoint(pos):
                    pygame.quit()
                    sys.exit() 
                if btn_newgame.collidepoint(pos):
                    title_window=False
                    
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw
 
#Controls screen  
def control_screen(window,fpsClock):
    control_window=True
    background_image='images/title_background.jpg'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    while control_window:
        window.fill((0,0,0))
        window.blit(background,(0, 0))
        window.blit(title_font.render("How to play:", True, (255, 255, 255)), (350, 80))
        window.blit(title_buttons_font.render("Use W, A, S, D to Move", True, (255, 255, 255)), (310, 240))
        window.blit(title_buttons_font.render("Use SHIFT to Dash", True, (255, 255, 255)), (340, 310))
        window.blit(title_buttons_font.render("Use Left Mouse Click to Swing Sword", True, (255, 255, 255)), (150, 380))
        window.blit(title_buttons_font.render("Use ESC to Pause Game", True, (255, 255, 255)), (300, 450))
        btn_exit = window.blit(font.render("[Back to Title]", True, (27, 228, 147)), (20, 20))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                
                if btn_exit.collidepoint(pos):
                    control_window=False 
                    
        
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw 
        
#Save slot display
def save_slot_screen(window,connection,select_db,fpsClock,delete_db):
    save_slot=0
    save_slot_window=True
    id_1_stats=select_db(connection,"player",["id='1'"]).fetchall()
    id_2_stats=select_db(connection,"player",["id='2'"]).fetchall()
    id_3_stats=select_db(connection,"player",["id='3'"]).fetchall()
    background_image='images/title_background.jpg'
    background=pygame.image.load(f'{background_image}')
    background=pygame.transform.scale(background, (1000,700))
    while save_slot_window:
        id_1_check=len(select_db(connection,"player",["id='1'"]).fetchall())
        id_2_check=len(select_db(connection,"player",["id='2'"]).fetchall())
        id_3_check=len(select_db(connection,"player",["id='3'"]).fetchall())
        window.fill((0,0,0))
        window.blit(background,(0, 0))
        window.blit(font.render("Select a Save Slot", True, (255, 255, 255)), (385, 75))
        btn_exit = window.blit(font.render("[Back to Title]", True, (27, 228, 147)), (20, 20))
        save_box1=pygame.draw.rect(window,(215,215,215),(250,120,500,130))
        save_box2=pygame.draw.rect(window,(215,215,215),(250,320,500,130))
        save_box3=pygame.draw.rect(window,(215,215,215),(250,520,500,130))
        if id_1_check==1:
            save_box_text1=window.blit(font.render(f"1. {id_1_stats[0][1]}", True, (0, 0, 0)), (275, 170))
            window.blit(font.render(f"Room: {id_1_stats[0][3]}", True, (0, 0, 0)), (620, 170))
            delete_1=window.blit(font.render("[Delete Save]", True, (27, 228, 147)), (765, 170))
        else:
            save_box_text1=window.blit(font.render("New Game", True, (0, 0, 0)), (445, 170))
            
        if id_2_check==1:
            save_box_text2=window.blit(font.render(f"2. {id_2_stats[0][1]}", True, (0, 0, 0)), (275, 370))
            window.blit(font.render(f"Room: {id_2_stats[0][3]}", True, (0, 0, 0)), (620, 370))
            delete_2=window.blit(font.render("[Delete Save]", True, (27, 228, 147)), (765, 370))
        else:
            save_box_text2=window.blit(font.render("New Game", True, (0, 0, 0)), (445, 370))
            
        if id_3_check==1:
            save_box_text3=window.blit(font.render(f"3. {id_3_stats[0][1]}", True, (0, 0, 0)), (275, 570))
            window.blit(font.render(f"Room: {id_3_stats[0][3]}", True, (0, 0, 0)), (620, 570))
            delete_3=window.blit(font.render("[Delete Save]", True, (27, 228, 147)), (765, 570))
        else:
            save_box_text3=window.blit(font.render("New Game", True, (0, 0, 0)), (445, 570))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
                 
                if btn_exit.collidepoint(pos):
                    back=True
                    save_slot=0
                    new=False
                    save_slot_window=False
                  
                if save_box1.collidepoint(pos) and id_1_check==0:
                    back=False
                    save_slot=1
                    new=True
                    save_slot_window=False
                    
                elif save_box2.collidepoint(pos) and id_2_check==0:
                    back=False
                    save_slot=2
                    new=True
                    save_slot_window=False
                    
                elif save_box3.collidepoint(pos) and id_3_check==0:
                    back=False
                    save_slot=3
                    new=True
                    save_slot_window=False
                    
                if save_box1.collidepoint(pos) and id_1_check==1:
                    back=False
                    save_slot=1
                    new=False
                    save_slot_window=False
                    
                elif save_box2.collidepoint(pos) and id_2_check==1:
                    back=False
                    save_slot=2
                    new=False
                    save_slot_window=False
                    
                elif save_box3.collidepoint(pos) and id_3_check==1:
                    back=False
                    save_slot=3
                    new=False
                    save_slot_window=False
            
                if id_1_check==1:
                    if delete_1.collidepoint(pos):
                        delete_db(connection,"player","id",1)
                if id_2_check==1:   
                    if delete_2.collidepoint(pos):
                        delete_db(connection,"player","id",2)
                if id_3_check==1:
                    if delete_3.collidepoint(pos):
                        delete_db(connection,"player","id",3)
                
                
                       
                                                                  
        pygame.display.update() #update the display
        fpsClock.tick(fps) #speed of redraw 
    return save_slot,new,back
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
        window.blit(font.render("What is your name, Wanderer?", True, (255, 255, 255)), (330, 175))
        text_box=pygame.draw.rect(window,(255,255,255),(265,220,465,100))
        window.blit(font.render(f"{name.upper()}", True, (0, 0, 0)), (name_position, 255))
        btn_confirm=window.blit(font.render("CONFIRM", True, (255, 255, 255)), (445, 350))
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
                    insert_db(connection,"player",["id","Name","Health","Save_Point"],[save_slot,name.upper(),100,1])
                
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