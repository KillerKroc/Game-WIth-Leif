# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:19:12 2019

@author: TastyBeanDip
"""

import pygame
import random
from pygame.locals import *

#load sprites
APBar0 = pygame.image.load("APBar.png")
AP = pygame.image.load("AP.png")
field = pygame.image.load("field.png")
fight = pygame.image.load("fight.png")
bow = pygame.image.load("bow.png")
heal = pygame.image.load("heal.png")
tank = pygame.image.load("tank.png")
orc = pygame.image.load("orc.png")
select = pygame.image.load("select.png")



#add system for naming troops by default or players choosing
#implement abilities based on equipment and creatures
#add vehicles/steeds/environment/fortifications



#define variables
playerHP = 10
AP = 0
enemyHP = 10
playerTurn = True
combat = False

#Creates Stats Dictionaries
#the stats of the creatures in the game (some might not be allowed certain equipment implement when we need)
creatures = {
        #damage, health, movement, attacks, range
        "orc": [2, 4, 1, 1, 1],
        "goblin": [3, 2, 1, 1, 1]
        }
#the stats of equipment in the game (might make seperate one for armor, weapons, runes, artifacts, etc)
equipment = {
        #damage, health, movement, attacks, range
        "dogslicer": [1, 2, 1, 0, 0],
        "knives": [0, 2, 2, 1, 0],
        "bow": [2, 0, 0, 0, 2]
        }
#the names of the creatures and equipment in the player's deck
deckList = {
        "name1": "orc",
        "equip1": "dogslicer"
        }
#the stats of the units in the player's deck
deckStats = {
        #damage, health, movement, range, name, equip
        1: [creatures[deckList["name1"]][0] + equipment[deckList["equip1"]][0], creatures[deckList["name1"]][1] + equipment[deckList["equip1"]][1], creatures[deckList["name1"]][2] + equipment[deckList["equip1"]][2], creatures[deckList["name1"]][3] + equipment[deckList["equip1"]][3], creatures[deckList["name1"]][4] + equipment[deckList["equip1"]][4], deckList["name1"], deckList["equip1"]],
        2: [creatures[deckList["name2"]][0] + equipment[deckList["equip2"]][0], creatures[deckList["name2"]][1] + equipment[deckList["equip2"]][1], creatures[deckList["name2"]][2] + equipment[deckList["equip2"]][2], creatures[deckList["name2"]][3] + equipment[deckList["equip2"]][3], creatures[deckList["name2"]][4] + equipment[deckList["equip2"]][4], deckList["name2"], deckList["equip2"]],
        3: [creatures[deckList["name3"]][0] + equipment[deckList["equip3"]][0], creatures[deckList["name3"]][1] + equipment[deckList["equip3"]][1], creatures[deckList["name3"]][2] + equipment[deckList["equip3"]][2], creatures[deckList["name3"]][3] + equipment[deckList["equip3"]][3], creatures[deckList["name3"]][4] + equipment[deckList["equip3"]][4], deckList["name3"], deckList["equip3"]],
        4: [creatures[deckList["name4"]][0] + equipment[deckList["equip4"]][0], creatures[deckList["name4"]][1] + equipment[deckList["equip4"]][1], creatures[deckList["name4"]][2] + equipment[deckList["equip4"]][2], creatures[deckList["name4"]][3] + equipment[deckList["equip4"]][3], creatures[deckList["name4"]][4] + equipment[deckList["equip4"]][4], deckList["name4"], deckList["equip4"]],
        5: [creatures[deckList["name5"]][0] + equipment[deckList["equip5"]][0], creatures[deckList["name5"]][1] + equipment[deckList["equip5"]][1], creatures[deckList["name5"]][2] + equipment[deckList["equip5"]][2], creatures[deckList["name5"]][3] + equipment[deckList["equip5"]][3], creatures[deckList["name5"]][4] + equipment[deckList["equip5"]][4], deckList["name5"], deckList["equip5"]],
        6: [creatures[deckList["name6"]][0] + equipment[deckList["equip6"]][0], creatures[deckList["name6"]][1] + equipment[deckList["equip6"]][1], creatures[deckList["name6"]][2] + equipment[deckList["equip6"]][2], creatures[deckList["name6"]][3] + equipment[deckList["equip6"]][3], creatures[deckList["name6"]][4] + equipment[deckList["equip6"]][4], deckList["name6"], deckList["equip6"]],
        7: [creatures[deckList["name7"]][0] + equipment[deckList["equip7"]][0], creatures[deckList["name7"]][1] + equipment[deckList["equip7"]][1], creatures[deckList["name7"]][2] + equipment[deckList["equip7"]][2], creatures[deckList["name7"]][3] + equipment[deckList["equip7"]][3], creatures[deckList["name7"]][4] + equipment[deckList["equip7"]][4], deckList["name7"], deckList["equip7"]],
        8: [creatures[deckList["name8"]][0] + equipment[deckList["equip8"]][0], creatures[deckList["name8"]][1] + equipment[deckList["equip8"]][1], creatures[deckList["name8"]][2] + equipment[deckList["equip8"]][2], creatures[deckList["name8"]][3] + equipment[deckList["equip8"]][3], creatures[deckList["name8"]][4] + equipment[deckList["equip8"]][4], deckList["name8"], deckList["equip8"]],
        9: [creatures[deckList["name9"]][0] + equipment[deckList["equip9"]][0], creatures[deckList["name9"]][1] + equipment[deckList["equip9"]][1], creatures[deckList["name9"]][2] + equipment[deckList["equip9"]][2], creatures[deckList["name9"]][3] + equipment[deckList["equip9"]][3], creatures[deckList["name9"]][4] + equipment[deckList["equip9"]][4], deckList["name9"], deckList["equip9"]],
        10: [creatures[deckList["name10"]][0] + equipment[deckList["equip10"]][0], creatures[deckList["name10"]][1] + equipment[deckList["equip10"]][1], creatures[deckList["name10"]][2] + equipment[deckList["equip10"]][2], creatures[deckList["name10"]][3] + equipment[deckList["equip10"]][3], creatures[deckList["name10"]][4] + equipment[deckList["equip10"]][4], deckList["name10"], deckList["equip10"]],
        11: [creatures[deckList["name11"]][0] + equipment[deckList["equip11"]][0], creatures[deckList["name11"]][1] + equipment[deckList["equip11"]][1], creatures[deckList["name11"]][2] + equipment[deckList["equip11"]][2], creatures[deckList["name11"]][3] + equipment[deckList["equip11"]][3], creatures[deckList["name11"]][4] + equipment[deckList["equip11"]][4], deckList["name11"], deckList["equip11"]],
        12: [creatures[deckList["name12"]][0] + equipment[deckList["equip12"]][0], creatures[deckList["name12"]][1] + equipment[deckList["equip12"]][1], creatures[deckList["name12"]][2] + equipment[deckList["equip12"]][2], creatures[deckList["name12"]][3] + equipment[deckList["equip12"]][3], creatures[deckList["name12"]][4] + equipment[deckList["equip12"]][4], deckList["name12"], deckList["equip12"]],
        13: [creatures[deckList["name13"]][0] + equipment[deckList["equip13"]][0], creatures[deckList["name13"]][1] + equipment[deckList["equip13"]][1], creatures[deckList["name13"]][2] + equipment[deckList["equip13"]][2], creatures[deckList["name13"]][3] + equipment[deckList["equip13"]][3], creatures[deckList["name13"]][4] + equipment[deckList["equip13"]][4], deckList["name13"], deckList["equip13"]],
        14: [creatures[deckList["name14"]][0] + equipment[deckList["equip14"]][0], creatures[deckList["name14"]][1] + equipment[deckList["equip14"]][1], creatures[deckList["name14"]][2] + equipment[deckList["equip14"]][2], creatures[deckList["name14"]][3] + equipment[deckList["equip14"]][3], creatures[deckList["name14"]][4] + equipment[deckList["equip14"]][4], deckList["name14"], deckList["equip14"]],
        15: [creatures[deckList["name15"]][0] + equipment[deckList["equip15"]][0], creatures[deckList["name15"]][1] + equipment[deckList["equip15"]][1], creatures[deckList["name15"]][2] + equipment[deckList["equip15"]][2], creatures[deckList["name15"]][3] + equipment[deckList["equip15"]][3], creatures[deckList["name15"]][4] + equipment[deckList["equip15"]][4], deckList["name15"], deckList["equip15"]]
        }
#the instance of all units used in a battle
battleDict = {
        #player units
        1: deckStats[1],
        2: deckStats[2],
        3: deckStats[3],
        4: deckStats[4],
        5: deckStats[5],
        6: deckStats[6],
        7: deckStats[7],
        8: deckStats[8],
        9: deckStats[9],
        10: deckStats[10],
        11: deckStats[11],
        12: deckStats[12],
        13: deckStats[13],
        14: deckStats[14],
        15: deckStats[15],
        #enemy units
        16: [],
        17: [],
        18: [],
        19: [],
        20: [],
        21: [],
        22: [],
        23: [],
        24: [],
        25: [],
        26: [],
        27: [],
        28: [],
        29: [],
        30: []
        }

#Creates an array to represent the playinb board
board = ['(', 0, 0, 0, 0, 0, ')',
         '(', 0, 0, 0, 0, 0, ')',
         '(', 0, 0, 0, 0, 0, ')']

#Creates a list to represent the player's deck
playerDeck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#Creates a list to represent the player's hand
playerHand = []

#Creates a list to represent the enemy's deck
enemyDeck = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

#Creates a list to represent the player's hand
enemyHand = []

#draws a card
def drawCard(player):
    if(player == True):
        card = random.randint(0, len(playerDeck)-1)
        playerHand.append(playerDeck[card])
        playerDeck.pop(card)
    if(player == False):
        card = random.randint(0, len(enemyDeck)-1)
        enemyHand.append(enemyDeck[card])
        enemyDeck.pop(card)

#blits board to screen
def blit_board(board, screen):
         screen.blit(field, [0, 0])
         pygame.display.flip()

#define a combat function
def combat():
    if (playerTurn == True):
        board.reverse()
        for unit in board:
            if(unit >= 1 and unit <= 15):
                move = 0
                attacks = battleDict[unit][3]
                ranging = 1
                attacking = True
                while True:
                    if(attacks >= 1):
                        target = board[board.index(unit) - (ranging + move)]
                        if (target == ')'):
                            #resolve attack on player
                            attacks = attacks - 1
                        elif (target >= 16):
                            #resolve attack
                            attacks = attacks - 1
                        elif (target == 0):
                            ranging = ranging + 1
                    if(move <= battleDict[unit][2] - 1 and attacking == False and board[board.index(unit) - (move + 1) == 0]):
                        move = move + 1
                        attacking = True
                    if(ranging == battleDict[unit][4] + 1 or attacks == 0):
                        attacking = False
                        ranging = 1
                    if(attacks == 0 and move == battleDict[unit][2]):
                        break
                #update movement position on board
        board.reverse()
        playerTurn == False
    elif (playerTurn == False):
        for unit in board:
            if(unit >= 16):
                move = 0
                attacks = battleDict[unit][3]
                ranging = 1
                attacking = True
                while True:
                    if(attacks >= 1):
                        target = board[board.index(unit) - (ranging + move)]
                        if (target == '('):
                            #resolve attack on player
                            attacks = attacks - 1
                        elif (target >= 1 and target <= 15):
                            #resolve attack
                            attacks = attacks - 1
                        elif (target == 0):
                            ranging = ranging + 1
                    if(move <= battleDict[unit][2] - 1 and attacking == False and board[board.index(unit) - (move + 1) == 0]):
                        move = move + 1
                        attacking = True
                    if(ranging == battleDict[unit][4] + 1 or attacks == 0):
                        attacking = False
                        ranging = 1
                    if(attacks == 0 and move == battleDict[unit][2]):
                        break
                #update movement position on board
        playerTurn == True
    combat == False
         
#initialize pygame
pygame.init()
     
#define a main function
def main():
    #load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen
    screen = pygame.display.set_mode((1920,1080))

    #fill the screen
    screen.fill([0, 0, 0])
    pygame.display.flip()
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        
        
        blit_board(board, screen)
        
        
        #player turn
        if(playerTurn == True and combat == False):
            #player actions
            if(#start combat button is pushed):
                    combat = True
                    
        #enemy turn
        if(playerTurn == False and combat == False):
                #AI decision making. Once reached decision execute orders and set combat to true
        
        #combat
        if(combat == True)
            #call combat
        
        #victory
        if(enemyHP <= 0):
            #win
        #failure
        if(playerHP <= 0):
            #lose
        
        
        #event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

#run the main function only if this module is executed as the main script
#(if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
    pygame.quit()
