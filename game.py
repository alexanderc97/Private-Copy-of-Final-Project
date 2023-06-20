#Made By: Alex Canning, Carter Belnap, Hayden
#Date: May 23 2023
#Purpose: Main file to run our full scale bullet-hell game.


#Basic PyGame Setup Code and Object Imports
import pygame,sys
from pygame import mixer
from random import *
import sqlite3 
from menu import *
from rooms import *
pygame.init()

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

#Setup of Starting objects
font = pygame.font.Font('ttf/DungeonChunk.ttf', 40)
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pygame.HWSURFACE| pygame.SCALED | pygame.RESIZABLE)
pygame.display.set_caption("Shadows of the Forgotten")
mixer.music.load('game_audio.mp3')
mixer.music.set_volume(0.2)
#Database Functions and Setup
def create_connection(db_file):
    #create a database connection to the SQLite database
    #return: Connection object or None
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn
connection = create_connection('game_database.db') #Connect to the Database

def create_table(conn,table, columns):
    col = ",".join(columns)
    sql = f'''CREATE TABLE IF NOT EXISTS {table}( id INTEGER PRIMARY KEY, {col});'''
    conn.execute(sql)

def insert_db(conn,table, columns,data):
    sql=f'''INSERT INTO {table} {tuple(columns)} VALUES {tuple(data)};'''
    conn.execute(sql)
    conn.commit()     
    
def delete_db(conn,table,column,what_to_remove):
    sql=f'''DELETE FROM {table} WHERE {column} = {what_to_remove}'''
    conn.execute(sql)
    conn.commit()  
  
def select_db(conn,table,columns_and_data=None):
    if not columns_and_data==None:
        col = " AND ".join(columns_and_data)
        sql=f'''SELECT * FROM {table} WHERE {col}'''
        #where 4 is the id i am looking for
        return conn.execute(sql)
    else:
        sql =f"SELECT * from {table}"
        return conn.execute(sql)   

def update_db(conn,table,columns_and_data,where_to_update):
    col = ",".join(columns_and_data)
    sql = f"UPDATE {table} set {col} where {where_to_update}"
    conn.execute(sql)
    conn.commit()  
     
#Main game screen display
def display():
    window.fill((0,0,0))

                     
        
#Activates the title screen on the front layer and activates the main display behind it
def title_menu():    
    title=True
    while title:    
        title_screen(window,fpsClock)
        global save_slot
        save_slot,new,back=save_slot_screen(window,connection,select_db,fpsClock,delete_db) 
        if back:
            title=True
        elif new:
            opening_text(window, connection, insert_db, fpsClock,save_slot)
            opening_game_screen(window,connection,insert_db,fpsClock,save_slot)
            title=False
        else:
            title=False
            
#mixer.music.play()      
title_menu()    
start_game=True
while start_game:
    player_stats=select_db(connection,"player",[f"id='{save_slot}'"]).fetchall()
    enemy1_stats=select_db(connection,"enemy",[f"id='1'"]).fetchall()
    enemy2_stats=select_db(connection,"enemy",[f"id='2'"]).fetchall()
    enemy3_stats=select_db(connection,"enemy",[f"id='3'"]).fetchall()
    enemyb_stats=select_db(connection,"boss",[f"id='1'"]).fetchall()
    
    if player_stats[0][3]==1:
        back=scene_room_1(save_slot,window,connection,fpsClock,update_db,player_stats)
    elif player_stats[0][3]==2:
        back=combat_room_1(save_slot,window,connection,fpsClock,update_db,player_stats,enemy1_stats,enemy2_stats,enemy3_stats)
    elif player_stats[0][3]==3:
        back=shop_room_1(save_slot,window,connection,fpsClock,update_db,player_stats)
    elif player_stats[0][3]==4:
        back=boss_room_1(save_slot,window,connection,fpsClock,update_db,player_stats)
    elif player_stats[0][3]==5:
        back=final_scene_room(save_slot,window,connection,fpsClock,update_db,player_stats)
        
    if back:
        title_menu()
        
    
    
display()
       
#Main Loop
while True:
    display()
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw