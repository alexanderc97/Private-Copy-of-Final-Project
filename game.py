#Made By: Alex Canning, Carter Belnap, Hayden
#Date: May 23 2023
#Purpose: Main file to run our full scale bullet-hell game.


#Basic PyGame Setup Code and Object Imports
import pygame,sys
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
title_screen(window,fpsClock)
save_slot,new=save_slot_screen(window,connection,select_db,fpsClock) 
if new:
    opening_text(window, connection, insert_db, fpsClock,save_slot)
    opening_game_screen(window,connection,insert_db,fpsClock,save_slot) 
    
start_game=True
while start_game:
    player_stats=select_db(connection,"player",[f"id='{save_slot}'"]).fetchall()
    if player_stats[0][5]==1:
        scene_room_1(save_slot,window,connection,fpsClock,update_db)
    elif player_stats[0][5]==2:
        combat_room_1(save_slot,window,connection,fpsClock,update_db,)
    elif player_stats[0][5]==3:
        shop_room_1(save_slot,window,connection,fpsClock,update_db,)
    elif player_stats[0][5]==4:
        boss_room_1(save_slot,window,connection,fpsClock,update_db,)
    elif player_stats[0][5]==5:
        scene_room_2(save_slot,window,connection,fpsClock,update_db,)
    elif player_stats[0][5]==6:
        combat_room_2(save_slot,window,connection,fpsClock,update_db)
    elif player_stats[0][5]==7:
        shop_room_2(save_slot,window,connection,fpsClock,update_db,)
    elif player_stats[0][5]==8:
        boss_room_2(save_slot,window,connection,fpsClock,update_db,)
    elif player_stats[0][5]==9:
        final_scene_room(save_slot,window,connection,fpsClock,update_db,)
    
    
display()
          
#Main Loop
while True:
    display() 
    
    pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw