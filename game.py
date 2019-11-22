# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:19:12 2019

@author: TastyBeanDip
"""


#add system for naming troops by default or players choosing
#implement abilities based on equipment and creatures
#add vehicles/steeds/environment/fortifications
#add multiple types of equipment
#some creatures might only be able to use certain types of equipment
#trample
#counterspell (u iz mukkin about)
#kopy kobold
#goblin cannon
#goblin airstrike?
#bugbears +1 racial range
#trample flying reach


import random
import copy
import pygame
from pygame.locals import *

'''variables'''
#the mouse
mouse = [(0,0), 0, 0, 0, 0, 0, 0] #(pos, b1,b2,b3,b4,b5,b6)

#sprites
field = pygame.image.load("field.png")
combatButton = pygame.image.load("fight.png")
selector = pygame.image.load("select.png")
hand = pygame.image.load("hand.png")
background = pygame.image.load("background.png")
spells = pygame.image.load("spells.png")

#localize these
playerHp = 10
enemyHp = 10
playerTurn = True
combat = False
playerAp = 1
playerTotalAp = 1
enemyAp = 1
enemyTotalAp = 1
playerUpkeep = 0
enemyUpkeep = 0
active = 0
move = 0
selectors = 0
combatClicked = False
player = True
combatClicked = False
boardClicked = False
handClicked = False
xpos = 0
ypos = 0
select = 0

#Creates a list to represent the player's deck
playerDeck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#Creates a list to represent the player's hand
playerHand = []

#Creates a list to represent the enemy's deck
enemyDeck = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

#Creates a list to represent the player's hand
enemyHand = []

#Creates an array to represent the playinb board
board = [-1, 0, 0, 0, 0, 0, -2,
         -1, 0, 0, 0, 0, 0, -2,
         -1, 0, 0, 0, 0, 0, -2]

selectBoard = [0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0]

#the stats of the creatures in the game (some might not be allowed certain equipment implement when we need)
creatures = {
        #[damage, health, movement, attacks, range, cost, upkeep], [taunt, heal, berserk, splash, embark capacity]
        "orc": [[2, 4, 1, 1, 1, 1, 1], [0, 0, 0 ,0, 0]],
        "goblin": [[3, 2, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0]],
        "warbear": [[3, 6, 1, 1, 1, 2, 1], [0, 0, 0, 0, 1]]
        }

#the stats of equipment in the game (might make seperate one for armor, weapons, runes, artifacts, etc)
equipment = {
        #[damage, health, movement, attacks, range, cost, upkeep], [taunt, heal, berserk, splash, embark capacity]
        "dogslicer": [[1, 2, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0]],
        "knives": [[0, 2, 2, 1, 0, 0, 0], [0, 0, 0, 0, 0]],
        "bow": [[2, 0, 0, 0, 2, 0, 0], [0, 0, 0, 2, 0]],
        "staff":[[1, 2, 0, 0, 1, 0, 0], [0, 2, 0, 0, 0]],
        "": [[0, 6, 1, 0, 0, 0, 0], [2, 0, 0, 0, 0]]
        }

#the units and equipment in the player's deck
deckList = {
        "name1": "orc",
        "equip1": "dogslicer",
        "name2": "orc",
        "equip2": "dogslicer",
        "name3": "orc",
        "equip3": "",
        "name4": "orc",
        "equip4": "",
        "name5": "goblin",
        "equip5": "knives",
        "name6": "goblin",
        "equip6": "knives",
        "name7": "goblin",
        "equip7": "bow",
        "name8": "goblin",
        "equip8": "bow",
        "name9": "goblin",
        "equip9": "",
        "name10": "goblin",
        "equip10": "",
        "name11": "goblin",
        "equip11": "staff",
        "name12": "goblin",
        "equip12": "staff",
        "name13": "orc",
        "equip13": "staff",
        "name14": "orc",
        "equip14": "staff",
        "name15": "orc",
        "equip15": "bow"
        }

#the units and equipment in the enemy's deck
encList = {
        "name1": "orc",
        "equip1": "dogslicer",
        "name2": "orc",
        "equip2": "dogslicer",
        "name3": "orc",
        "equip3": "",
        "name4": "orc",
        "equip4": "",
        "name5": "goblin",
        "equip5": "knives",
        "name6": "goblin",
        "equip6": "knives",
        "name7": "goblin",
        "equip7": "bow",
        "name8": "goblin",
        "equip8": "bow",
        "name9": "goblin",
        "equip9": "",
        "name10": "goblin",
        "equip10": "",
        "name11": "goblin",
        "equip11": "staff",
        "name12": "goblin",
        "equip12": "staff",
        "name13": "orc",
        "equip13": "staff",
        "name14": "orc",
        "equip14": "staff",
        "name15": "orc",
        "equip15": "bow"
        }

#the art of units in both decks
artDict = {
        1: [pygame.image.load(f"{deckList['name1']}BodyWalk.png"), pygame.image.load(f"{deckList['name1']}ArmsIdle{deckList['equip1']}.png")],
        2: [pygame.image.load(f"{deckList['name2']}BodyWalk.png"), pygame.image.load(f"{deckList['name2']}ArmsIdle{deckList['equip2']}.png")],
        3: [pygame.image.load(f"{deckList['name3']}BodyWalk.png"), pygame.image.load(f"{deckList['name3']}ArmsIdle{deckList['equip3']}.png")],
        4: [pygame.image.load(f"{deckList['name4']}BodyWalk.png"), pygame.image.load(f"{deckList['name4']}ArmsIdle{deckList['equip4']}.png")],
        5: [pygame.image.load(f"{deckList['name5']}BodyWalk.png"), pygame.image.load(f"{deckList['name5']}ArmsIdle{deckList['equip5']}.png")],
        6: [pygame.image.load(f"{deckList['name6']}BodyWalk.png"), pygame.image.load(f"{deckList['name6']}ArmsIdle{deckList['equip6']}.png")],
        7: [pygame.image.load(f"{deckList['name7']}BodyWalk.png"), pygame.image.load(f"{deckList['name7']}ArmsIdle{deckList['equip7']}.png")],
        8: [pygame.image.load(f"{deckList['name8']}BodyWalk.png"), pygame.image.load(f"{deckList['name8']}ArmsIdle{deckList['equip8']}.png")],
        9: [pygame.image.load(f"{deckList['name9']}BodyWalk.png"), pygame.image.load(f"{deckList['name9']}ArmsIdle{deckList['equip9']}.png")],
        10: [pygame.image.load(f"{deckList['name10']}BodyWalk.png"), pygame.image.load(f"{deckList['name10']}ArmsIdle{deckList['equip10']}.png")],
        11: [pygame.image.load(f"{deckList['name11']}BodyWalk.png"), pygame.image.load(f"{deckList['name11']}ArmsIdle{deckList['equip11']}.png")],
        12: [pygame.image.load(f"{deckList['name12']}BodyWalk.png"), pygame.image.load(f"{deckList['name12']}ArmsIdle{deckList['equip12']}.png")],
        13: [pygame.image.load(f"{deckList['name13']}BodyWalk.png"), pygame.image.load(f"{deckList['name13']}ArmsIdle{deckList['equip13']}.png")],
        14: [pygame.image.load(f"{deckList['name14']}BodyWalk.png"), pygame.image.load(f"{deckList['name14']}ArmsIdle{deckList['equip14']}.png")],
        15: [pygame.image.load(f"{deckList['name15']}BodyWalk.png"), pygame.image.load(f"{deckList['name15']}ArmsIdle{deckList['equip15']}.png")],
        16: [pygame.image.load(f"{encList['name1']}BodyWalk.png"), pygame.image.load(f"{encList['name1']}ArmsIdle{encList['equip1']}.png")],
        17: [pygame.image.load(f"{encList['name2']}BodyWalk.png"), pygame.image.load(f"{encList['name2']}ArmsIdle{encList['equip2']}.png")],
        18: [pygame.image.load(f"{encList['name3']}BodyWalk.png"), pygame.image.load(f"{encList['name3']}ArmsIdle{encList['equip3']}.png")],
        19: [pygame.image.load(f"{encList['name4']}BodyWalk.png"), pygame.image.load(f"{encList['name4']}ArmsIdle{encList['equip4']}.png")],
        20: [pygame.image.load(f"{encList['name5']}BodyWalk.png"), pygame.image.load(f"{encList['name5']}ArmsIdle{encList['equip5']}.png")],
        21: [pygame.image.load(f"{encList['name6']}BodyWalk.png"), pygame.image.load(f"{encList['name6']}ArmsIdle{encList['equip6']}.png")],
        22: [pygame.image.load(f"{encList['name7']}BodyWalk.png"), pygame.image.load(f"{encList['name7']}ArmsIdle{encList['equip7']}.png")],
        23: [pygame.image.load(f"{encList['name8']}BodyWalk.png"), pygame.image.load(f"{encList['name8']}ArmsIdle{encList['equip8']}.png")],
        24: [pygame.image.load(f"{encList['name9']}BodyWalk.png"), pygame.image.load(f"{encList['name9']}ArmsIdle{encList['equip9']}.png")],
        25: [pygame.image.load(f"{encList['name10']}BodyWalk.png"), pygame.image.load(f"{encList['name10']}ArmsIdle{encList['equip10']}.png")],
        26: [pygame.image.load(f"{encList['name11']}BodyWalk.png"), pygame.image.load(f"{encList['name11']}ArmsIdle{encList['equip11']}.png")],
        27: [pygame.image.load(f"{encList['name12']}BodyWalk.png"), pygame.image.load(f"{encList['name12']}ArmsIdle{encList['equip12']}.png")],
        28: [pygame.image.load(f"{encList['name13']}BodyWalk.png"), pygame.image.load(f"{encList['name13']}ArmsIdle{encList['equip13']}.png")],
        29: [pygame.image.load(f"{encList['name14']}BodyWalk.png"), pygame.image.load(f"{encList['name14']}ArmsIdle{encList['equip14']}.png")],
        30: [pygame.image.load(f"{encList['name15']}BodyWalk.png"), pygame.image.load(f"{encList['name15']}ArmsIdle{encList['equip15']}.png")]
        }

#the stats of the units in the player's deck
deckStats = {
        #[damage, health, movement, attacks, range, cost, upkeep], [taunt, heal, berserk, splash], [taunted, carrying]
        1: [[creatures[deckList["name1"]][0][0] + equipment[deckList["equip1"]][0][0], creatures[deckList["name1"]][0][1] + equipment[deckList["equip1"]][0][1], creatures[deckList["name1"]][0][2] + equipment[deckList["equip1"]][0][2], creatures[deckList["name1"]][0][3] + equipment[deckList["equip1"]][0][3], creatures[deckList["name1"]][0][4] + equipment[deckList["equip1"]][0][4], creatures[deckList["name1"]][0][5] + equipment[deckList["equip1"]][0][5], creatures[deckList["name1"]][0][6] + equipment[deckList["equip1"]][0][6]],
            [creatures[deckList["name1"]][1][0] + equipment[deckList["equip1"]][1][0], creatures[deckList["name1"]][1][1] + equipment[deckList["equip1"]][1][1], creatures[deckList["name1"]][1][2] + equipment[deckList["equip1"]][1][2], creatures[deckList["name1"]][1][3] + equipment[deckList["equip1"]][1][3], creatures[deckList["name1"]][1][4] + equipment[deckList["equip1"]][1][4]],
            [0, 0]],
        2: [[creatures[deckList["name2"]][0][0] + equipment[deckList["equip2"]][0][0], creatures[deckList["name2"]][0][1] + equipment[deckList["equip2"]][0][1], creatures[deckList["name2"]][0][2] + equipment[deckList["equip2"]][0][2], creatures[deckList["name2"]][0][3] + equipment[deckList["equip2"]][0][3], creatures[deckList["name2"]][0][4] + equipment[deckList["equip2"]][0][4], creatures[deckList["name2"]][0][5] + equipment[deckList["equip2"]][0][5], creatures[deckList["name2"]][0][6] + equipment[deckList["equip2"]][0][6]],
            [creatures[deckList["name2"]][1][0] + equipment[deckList["equip2"]][1][0], creatures[deckList["name2"]][1][1] + equipment[deckList["equip2"]][1][1], creatures[deckList["name2"]][1][2] + equipment[deckList["equip2"]][1][2], creatures[deckList["name2"]][1][3] + equipment[deckList["equip2"]][1][3], creatures[deckList["name2"]][1][4] + equipment[deckList["equip2"]][1][4]],
            [0, 0]],
        3: [[creatures[deckList["name3"]][0][0] + equipment[deckList["equip3"]][0][0], creatures[deckList["name3"]][0][1] + equipment[deckList["equip3"]][0][1], creatures[deckList["name3"]][0][2] + equipment[deckList["equip3"]][0][2], creatures[deckList["name3"]][0][3] + equipment[deckList["equip3"]][0][3], creatures[deckList["name3"]][0][4] + equipment[deckList["equip3"]][0][4], creatures[deckList["name3"]][0][5] + equipment[deckList["equip3"]][0][5], creatures[deckList["name3"]][0][6] + equipment[deckList["equip3"]][0][6]],
            [creatures[deckList["name3"]][1][0] + equipment[deckList["equip3"]][1][0], creatures[deckList["name3"]][1][1] + equipment[deckList["equip3"]][1][1], creatures[deckList["name3"]][1][2] + equipment[deckList["equip3"]][1][2], creatures[deckList["name3"]][1][3] + equipment[deckList["equip3"]][1][3], creatures[deckList["name3"]][1][4] + equipment[deckList["equip3"]][1][4]],
            [0, 0]],
        4: [[creatures[deckList["name4"]][0][0] + equipment[deckList["equip4"]][0][0], creatures[deckList["name4"]][0][1] + equipment[deckList["equip4"]][0][1], creatures[deckList["name4"]][0][2] + equipment[deckList["equip4"]][0][2], creatures[deckList["name4"]][0][3] + equipment[deckList["equip4"]][0][3], creatures[deckList["name4"]][0][4] + equipment[deckList["equip4"]][0][4], creatures[deckList["name4"]][0][5] + equipment[deckList["equip4"]][0][5], creatures[deckList["name4"]][0][6] + equipment[deckList["equip4"]][0][6]],
            [creatures[deckList["name4"]][1][0] + equipment[deckList["equip4"]][1][0], creatures[deckList["name4"]][1][1] + equipment[deckList["equip4"]][1][1], creatures[deckList["name4"]][1][2] + equipment[deckList["equip4"]][1][2], creatures[deckList["name4"]][1][3] + equipment[deckList["equip4"]][1][3], creatures[deckList["name4"]][1][4] + equipment[deckList["equip4"]][1][4]],
            [0, 0]],
        5: [[creatures[deckList["name5"]][0][0] + equipment[deckList["equip5"]][0][0], creatures[deckList["name5"]][0][1] + equipment[deckList["equip5"]][0][1], creatures[deckList["name5"]][0][2] + equipment[deckList["equip5"]][0][2], creatures[deckList["name5"]][0][3] + equipment[deckList["equip5"]][0][3], creatures[deckList["name5"]][0][4] + equipment[deckList["equip5"]][0][4], creatures[deckList["name5"]][0][5] + equipment[deckList["equip5"]][0][5], creatures[deckList["name5"]][0][6] + equipment[deckList["equip5"]][0][6]],
            [creatures[deckList["name5"]][1][0] + equipment[deckList["equip5"]][1][0], creatures[deckList["name5"]][1][1] + equipment[deckList["equip5"]][1][1], creatures[deckList["name5"]][1][2] + equipment[deckList["equip5"]][1][2], creatures[deckList["name5"]][1][3] + equipment[deckList["equip5"]][1][3], creatures[deckList["name5"]][1][4] + equipment[deckList["equip5"]][1][4]],
            [0, 0]],
        6: [[creatures[deckList["name6"]][0][0] + equipment[deckList["equip6"]][0][0], creatures[deckList["name6"]][0][1] + equipment[deckList["equip6"]][0][1], creatures[deckList["name6"]][0][2] + equipment[deckList["equip6"]][0][2], creatures[deckList["name6"]][0][3] + equipment[deckList["equip6"]][0][3], creatures[deckList["name6"]][0][4] + equipment[deckList["equip6"]][0][4], creatures[deckList["name6"]][0][5] + equipment[deckList["equip6"]][0][5], creatures[deckList["name6"]][0][6] + equipment[deckList["equip6"]][0][6]],
            [creatures[deckList["name6"]][1][0] + equipment[deckList["equip6"]][1][0], creatures[deckList["name6"]][1][1] + equipment[deckList["equip6"]][1][1], creatures[deckList["name6"]][1][2] + equipment[deckList["equip6"]][1][2], creatures[deckList["name6"]][1][3] + equipment[deckList["equip6"]][1][3], creatures[deckList["name6"]][1][4] + equipment[deckList["equip6"]][1][4]],
            [0, 0]],
        7: [[creatures[deckList["name7"]][0][0] + equipment[deckList["equip7"]][0][0], creatures[deckList["name7"]][0][1] + equipment[deckList["equip7"]][0][1], creatures[deckList["name7"]][0][2] + equipment[deckList["equip7"]][0][2], creatures[deckList["name7"]][0][3] + equipment[deckList["equip7"]][0][3], creatures[deckList["name7"]][0][4] + equipment[deckList["equip7"]][0][4], creatures[deckList["name7"]][0][5] + equipment[deckList["equip7"]][0][5], creatures[deckList["name7"]][0][6] + equipment[deckList["equip7"]][0][6]],
            [creatures[deckList["name7"]][1][0] + equipment[deckList["equip7"]][1][0], creatures[deckList["name7"]][1][1] + equipment[deckList["equip7"]][1][1], creatures[deckList["name7"]][1][2] + equipment[deckList["equip7"]][1][2], creatures[deckList["name7"]][1][3] + equipment[deckList["equip7"]][1][3], creatures[deckList["name7"]][1][4] + equipment[deckList["equip7"]][1][4]],
            [0, 0]],
        8: [[creatures[deckList["name8"]][0][0] + equipment[deckList["equip8"]][0][0], creatures[deckList["name8"]][0][1] + equipment[deckList["equip8"]][0][1], creatures[deckList["name8"]][0][2] + equipment[deckList["equip8"]][0][2], creatures[deckList["name8"]][0][3] + equipment[deckList["equip8"]][0][3], creatures[deckList["name8"]][0][4] + equipment[deckList["equip8"]][0][4], creatures[deckList["name8"]][0][5] + equipment[deckList["equip8"]][0][5], creatures[deckList["name8"]][0][6] + equipment[deckList["equip8"]][0][6]],
            [creatures[deckList["name8"]][1][0] + equipment[deckList["equip8"]][1][0], creatures[deckList["name8"]][1][1] + equipment[deckList["equip8"]][1][1], creatures[deckList["name8"]][1][2] + equipment[deckList["equip8"]][1][2], creatures[deckList["name8"]][1][3] + equipment[deckList["equip8"]][1][3], creatures[deckList["name8"]][1][4] + equipment[deckList["equip8"]][1][4]],
            [0, 0]],
        9: [[creatures[deckList["name9"]][0][0] + equipment[deckList["equip9"]][0][0], creatures[deckList["name9"]][0][1] + equipment[deckList["equip9"]][0][1], creatures[deckList["name9"]][0][2] + equipment[deckList["equip9"]][0][2], creatures[deckList["name9"]][0][3] + equipment[deckList["equip9"]][0][3], creatures[deckList["name9"]][0][4] + equipment[deckList["equip9"]][0][4], creatures[deckList["name9"]][0][5] + equipment[deckList["equip9"]][0][5], creatures[deckList["name9"]][0][6] + equipment[deckList["equip9"]][0][6]],
            [creatures[deckList["name9"]][1][0] + equipment[deckList["equip9"]][1][0], creatures[deckList["name9"]][1][1] + equipment[deckList["equip9"]][1][1], creatures[deckList["name9"]][1][2] + equipment[deckList["equip9"]][1][2], creatures[deckList["name9"]][1][3] + equipment[deckList["equip9"]][1][3], creatures[deckList["name9"]][1][4] + equipment[deckList["equip9"]][1][4]],
            [0, 0]],
        10: [[creatures[deckList["name10"]][0][0] + equipment[deckList["equip10"]][0][0], creatures[deckList["name10"]][0][1] + equipment[deckList["equip10"]][0][1], creatures[deckList["name10"]][0][2] + equipment[deckList["equip10"]][0][2], creatures[deckList["name10"]][0][3] + equipment[deckList["equip10"]][0][3], creatures[deckList["name10"]][0][4] + equipment[deckList["equip10"]][0][4], creatures[deckList["name10"]][0][5] + equipment[deckList["equip10"]][0][5], creatures[deckList["name10"]][0][6] + equipment[deckList["equip10"]][0][6]],
             [creatures[deckList["name10"]][1][0] + equipment[deckList["equip10"]][1][0], creatures[deckList["name10"]][1][1] + equipment[deckList["equip10"]][1][1], creatures[deckList["name10"]][1][2] + equipment[deckList["equip10"]][1][2], creatures[deckList["name10"]][1][3] + equipment[deckList["equip10"]][1][3], creatures[deckList["name10"]][1][4] + equipment[deckList["equip10"]][1][4]],
             [0, 0]],
        11: [[creatures[deckList["name11"]][0][0] + equipment[deckList["equip11"]][0][0], creatures[deckList["name11"]][0][1] + equipment[deckList["equip11"]][0][1], creatures[deckList["name11"]][0][2] + equipment[deckList["equip11"]][0][2], creatures[deckList["name11"]][0][3] + equipment[deckList["equip11"]][0][3], creatures[deckList["name11"]][0][4] + equipment[deckList["equip11"]][0][4], creatures[deckList["name11"]][0][5] + equipment[deckList["equip11"]][0][5], creatures[deckList["name11"]][0][6] + equipment[deckList["equip11"]][0][6]],
             [creatures[deckList["name11"]][1][0] + equipment[deckList["equip11"]][1][0], creatures[deckList["name11"]][1][1] + equipment[deckList["equip11"]][1][1], creatures[deckList["name11"]][1][2] + equipment[deckList["equip11"]][1][2], creatures[deckList["name11"]][1][3] + equipment[deckList["equip11"]][1][3], creatures[deckList["name11"]][1][4] + equipment[deckList["equip11"]][1][4]],
             [0, 0]],
        12: [[creatures[deckList["name12"]][0][0] + equipment[deckList["equip12"]][0][0], creatures[deckList["name12"]][0][1] + equipment[deckList["equip12"]][0][1], creatures[deckList["name12"]][0][2] + equipment[deckList["equip12"]][0][2], creatures[deckList["name12"]][0][3] + equipment[deckList["equip12"]][0][3], creatures[deckList["name12"]][0][4] + equipment[deckList["equip12"]][0][4], creatures[deckList["name12"]][0][5] + equipment[deckList["equip12"]][0][5], creatures[deckList["name12"]][0][6] + equipment[deckList["equip12"]][0][6]],
             [creatures[deckList["name12"]][1][0] + equipment[deckList["equip12"]][1][0], creatures[deckList["name12"]][1][1] + equipment[deckList["equip12"]][1][1], creatures[deckList["name12"]][1][2] + equipment[deckList["equip12"]][1][2], creatures[deckList["name12"]][1][3] + equipment[deckList["equip12"]][1][3], creatures[deckList["name12"]][1][4] + equipment[deckList["equip12"]][1][4]],
             [0, 0]],
        13: [[creatures[deckList["name13"]][0][0] + equipment[deckList["equip13"]][0][0], creatures[deckList["name13"]][0][1] + equipment[deckList["equip13"]][0][1], creatures[deckList["name13"]][0][2] + equipment[deckList["equip13"]][0][2], creatures[deckList["name13"]][0][3] + equipment[deckList["equip13"]][0][3], creatures[deckList["name13"]][0][4] + equipment[deckList["equip13"]][0][4], creatures[deckList["name13"]][0][5] + equipment[deckList["equip13"]][0][5], creatures[deckList["name13"]][0][6] + equipment[deckList["equip13"]][0][6]],
             [creatures[deckList["name13"]][1][0] + equipment[deckList["equip13"]][1][0], creatures[deckList["name13"]][1][1] + equipment[deckList["equip13"]][1][1], creatures[deckList["name13"]][1][2] + equipment[deckList["equip13"]][1][2], creatures[deckList["name13"]][1][3] + equipment[deckList["equip13"]][1][3], creatures[deckList["name13"]][1][4] + equipment[deckList["equip13"]][1][4]],
             [0, 0]],
        14: [[creatures[deckList["name14"]][0][0] + equipment[deckList["equip14"]][0][0], creatures[deckList["name14"]][0][1] + equipment[deckList["equip14"]][0][1], creatures[deckList["name14"]][0][2] + equipment[deckList["equip14"]][0][2], creatures[deckList["name14"]][0][3] + equipment[deckList["equip14"]][0][3], creatures[deckList["name14"]][0][4] + equipment[deckList["equip14"]][0][4], creatures[deckList["name14"]][0][5] + equipment[deckList["equip14"]][0][5], creatures[deckList["name14"]][0][6] + equipment[deckList["equip14"]][0][6]],
             [creatures[deckList["name14"]][1][0] + equipment[deckList["equip14"]][1][0], creatures[deckList["name14"]][1][1] + equipment[deckList["equip14"]][1][1], creatures[deckList["name14"]][1][2] + equipment[deckList["equip14"]][1][2], creatures[deckList["name14"]][1][3] + equipment[deckList["equip14"]][1][3], creatures[deckList["name14"]][1][4] + equipment[deckList["equip14"]][1][4]],
             [0, 0]],
        15: [[creatures[deckList["name15"]][0][0] + equipment[deckList["equip15"]][0][0], creatures[deckList["name15"]][0][1] + equipment[deckList["equip15"]][0][1], creatures[deckList["name15"]][0][2] + equipment[deckList["equip15"]][0][2], creatures[deckList["name15"]][0][3] + equipment[deckList["equip15"]][0][3], creatures[deckList["name15"]][0][4] + equipment[deckList["equip15"]][0][4], creatures[deckList["name15"]][0][5] + equipment[deckList["equip15"]][0][5], creatures[deckList["name15"]][0][6] + equipment[deckList["equip15"]][0][6]],
             [creatures[deckList["name15"]][1][0] + equipment[deckList["equip15"]][1][0], creatures[deckList["name15"]][1][1] + equipment[deckList["equip15"]][1][1], creatures[deckList["name15"]][1][2] + equipment[deckList["equip15"]][1][2], creatures[deckList["name15"]][1][3] + equipment[deckList["equip15"]][1][3], creatures[deckList["name15"]][1][4] + equipment[deckList["equip15"]][1][4]],
             [0, 0]]
        }

#the stats of the units in the enemy's deck
encStats = {
        #[damage, health, movement, attacks, range, cost, upkeep], [taunt, heal, berserk, splash], [taunted, embarked]
        16: [[creatures[encList["name1"]][0][0] + equipment[encList["equip1"]][0][0], creatures[encList["name1"]][0][1] + equipment[encList["equip1"]][0][1], creatures[encList["name1"]][0][2] + equipment[encList["equip1"]][0][2], creatures[encList["name1"]][0][3] + equipment[encList["equip1"]][0][3], creatures[encList["name1"]][0][4] + equipment[encList["equip1"]][0][4], creatures[encList["name1"]][0][5] + equipment[encList["equip1"]][0][5], creatures[encList["name1"]][0][6] + equipment[encList["equip1"]][0][6]],
             [creatures[encList["name1"]][1][0] + equipment[encList["equip1"]][1][0], creatures[encList["name1"]][1][1] + equipment[encList["equip1"]][1][1], creatures[encList["name1"]][1][2] + equipment[encList["equip1"]][1][2], creatures[encList["name1"]][1][3] + equipment[encList["equip1"]][1][3], creatures[encList["name1"]][1][4] + equipment[encList["equip1"]][1][4]],
             [0, 0]],
        17: [[creatures[encList["name2"]][0][0] + equipment[encList["equip2"]][0][0], creatures[encList["name2"]][0][1] + equipment[encList["equip2"]][0][1], creatures[encList["name2"]][0][2] + equipment[encList["equip2"]][0][2], creatures[encList["name2"]][0][3] + equipment[encList["equip2"]][0][3], creatures[encList["name2"]][0][4] + equipment[encList["equip2"]][0][4], creatures[encList["name2"]][0][5] + equipment[encList["equip2"]][0][5], creatures[encList["name2"]][0][6] + equipment[encList["equip2"]][0][6]],
             [creatures[encList["name2"]][1][0] + equipment[encList["equip2"]][1][0], creatures[encList["name2"]][1][1] + equipment[encList["equip2"]][1][1], creatures[encList["name2"]][1][2] + equipment[encList["equip2"]][1][2], creatures[encList["name2"]][1][3] + equipment[encList["equip2"]][1][3], creatures[encList["name2"]][1][4] + equipment[encList["equip2"]][1][4]],
             [0, 0]],
        18: [[creatures[encList["name3"]][0][0] + equipment[encList["equip3"]][0][0], creatures[encList["name3"]][0][1] + equipment[encList["equip3"]][0][1], creatures[encList["name3"]][0][2] + equipment[encList["equip3"]][0][2], creatures[encList["name3"]][0][3] + equipment[encList["equip3"]][0][3], creatures[encList["name3"]][0][4] + equipment[encList["equip3"]][0][4], creatures[encList["name3"]][0][5] + equipment[encList["equip3"]][0][5], creatures[encList["name3"]][0][6] + equipment[encList["equip3"]][0][6]],
             [creatures[encList["name3"]][1][0] + equipment[encList["equip3"]][1][0], creatures[encList["name3"]][1][1] + equipment[encList["equip3"]][1][1], creatures[encList["name3"]][1][2] + equipment[encList["equip3"]][1][2], creatures[encList["name3"]][1][3] + equipment[encList["equip3"]][1][3], creatures[encList["name3"]][1][4] + equipment[encList["equip3"]][1][4]],
             [0, 0]],
        19: [[creatures[encList["name4"]][0][0] + equipment[encList["equip4"]][0][0], creatures[encList["name4"]][0][1] + equipment[encList["equip4"]][0][1], creatures[encList["name4"]][0][2] + equipment[encList["equip4"]][0][2], creatures[encList["name4"]][0][3] + equipment[encList["equip4"]][0][3], creatures[encList["name4"]][0][4] + equipment[encList["equip4"]][0][4], creatures[encList["name4"]][0][5] + equipment[encList["equip4"]][0][5], creatures[encList["name4"]][0][6] + equipment[encList["equip4"]][0][6]],
             [creatures[encList["name4"]][1][0] + equipment[encList["equip4"]][1][0], creatures[encList["name4"]][1][1] + equipment[encList["equip4"]][1][1], creatures[encList["name4"]][1][2] + equipment[encList["equip4"]][1][2], creatures[encList["name4"]][1][3] + equipment[encList["equip4"]][1][3], creatures[encList["name4"]][1][4] + equipment[encList["equip4"]][1][4]],
             [0, 0]],
        20: [[creatures[encList["name5"]][0][0] + equipment[encList["equip5"]][0][0], creatures[encList["name5"]][0][1] + equipment[encList["equip5"]][0][1], creatures[encList["name5"]][0][2] + equipment[encList["equip5"]][0][2], creatures[encList["name5"]][0][3] + equipment[encList["equip5"]][0][3], creatures[encList["name5"]][0][4] + equipment[encList["equip5"]][0][4], creatures[encList["name5"]][0][5] + equipment[encList["equip5"]][0][5], creatures[encList["name5"]][0][6] + equipment[encList["equip5"]][0][6]],
             [creatures[encList["name5"]][1][0] + equipment[encList["equip5"]][1][0], creatures[encList["name5"]][1][1] + equipment[encList["equip5"]][1][1], creatures[encList["name5"]][1][2] + equipment[encList["equip5"]][1][2], creatures[encList["name5"]][1][3] + equipment[encList["equip5"]][1][3], creatures[encList["name5"]][1][4] + equipment[encList["equip5"]][1][4]],
             [0, 0]],
        21: [[creatures[encList["name6"]][0][0] + equipment[encList["equip6"]][0][0], creatures[encList["name6"]][0][1] + equipment[encList["equip6"]][0][1], creatures[encList["name6"]][0][2] + equipment[encList["equip6"]][0][2], creatures[encList["name6"]][0][3] + equipment[encList["equip6"]][0][3], creatures[encList["name6"]][0][4] + equipment[encList["equip6"]][0][4], creatures[encList["name6"]][0][5] + equipment[encList["equip6"]][0][5], creatures[encList["name6"]][0][6] + equipment[encList["equip6"]][0][6]],
             [creatures[encList["name6"]][1][0] + equipment[encList["equip6"]][1][0], creatures[encList["name6"]][1][1] + equipment[encList["equip6"]][1][1], creatures[encList["name6"]][1][2] + equipment[encList["equip6"]][1][2], creatures[encList["name6"]][1][3] + equipment[encList["equip6"]][1][3], creatures[encList["name6"]][1][4] + equipment[encList["equip6"]][1][4]],
             [0, 0]],
        22: [[creatures[encList["name7"]][0][0] + equipment[encList["equip7"]][0][0], creatures[encList["name7"]][0][1] + equipment[encList["equip7"]][0][1], creatures[encList["name7"]][0][2] + equipment[encList["equip7"]][0][2], creatures[encList["name7"]][0][3] + equipment[encList["equip7"]][0][3], creatures[encList["name7"]][0][4] + equipment[encList["equip7"]][0][4], creatures[encList["name7"]][0][5] + equipment[encList["equip7"]][0][5], creatures[encList["name7"]][0][6] + equipment[encList["equip7"]][0][6]],
             [creatures[encList["name7"]][1][0] + equipment[encList["equip7"]][1][0], creatures[encList["name7"]][1][1] + equipment[encList["equip7"]][1][1], creatures[encList["name7"]][1][2] + equipment[encList["equip7"]][1][2], creatures[encList["name7"]][1][3] + equipment[encList["equip7"]][1][3], creatures[encList["name7"]][1][4] + equipment[encList["equip7"]][1][4]],
             [0, 0]],
        23: [[creatures[encList["name8"]][0][0] + equipment[encList["equip8"]][0][0], creatures[encList["name8"]][0][1] + equipment[encList["equip8"]][0][1], creatures[encList["name8"]][0][2] + equipment[encList["equip8"]][0][2], creatures[encList["name8"]][0][3] + equipment[encList["equip8"]][0][3], creatures[encList["name8"]][0][4] + equipment[encList["equip8"]][0][4], creatures[encList["name8"]][0][5] + equipment[encList["equip8"]][0][5], creatures[encList["name8"]][0][6] + equipment[encList["equip8"]][0][6]],
             [creatures[encList["name8"]][1][0] + equipment[encList["equip8"]][1][0], creatures[encList["name8"]][1][1] + equipment[encList["equip8"]][1][1], creatures[encList["name8"]][1][2] + equipment[encList["equip8"]][1][2], creatures[encList["name8"]][1][3] + equipment[encList["equip8"]][1][3], creatures[encList["name8"]][1][4] + equipment[encList["equip8"]][1][4]],
             [0, 0]],
        24: [[creatures[encList["name9"]][0][0] + equipment[encList["equip9"]][0][0], creatures[encList["name9"]][0][1] + equipment[encList["equip9"]][0][1], creatures[encList["name9"]][0][2] + equipment[encList["equip9"]][0][2], creatures[encList["name9"]][0][3] + equipment[encList["equip9"]][0][3], creatures[encList["name9"]][0][4] + equipment[encList["equip9"]][0][4], creatures[encList["name9"]][0][5] + equipment[encList["equip9"]][0][5], creatures[encList["name9"]][0][6] + equipment[encList["equip9"]][0][6]],
             [creatures[encList["name9"]][1][0] + equipment[encList["equip9"]][1][0], creatures[encList["name9"]][1][1] + equipment[encList["equip9"]][1][1], creatures[encList["name9"]][1][2] + equipment[encList["equip9"]][1][2], creatures[encList["name9"]][1][3] + equipment[encList["equip9"]][1][3], creatures[encList["name9"]][1][4] + equipment[encList["equip9"]][1][4]],
             [0, 0]],
        25: [[creatures[encList["name10"]][0][0] + equipment[encList["equip10"]][0][0], creatures[encList["name10"]][0][1] + equipment[encList["equip10"]][0][1], creatures[encList["name10"]][0][2] + equipment[encList["equip10"]][0][2], creatures[encList["name10"]][0][3] + equipment[encList["equip10"]][0][3], creatures[encList["name10"]][0][4] + equipment[encList["equip10"]][0][4], creatures[encList["name10"]][0][5] + equipment[encList["equip10"]][0][5], creatures[encList["name10"]][0][6] + equipment[encList["equip10"]][0][6]],
             [creatures[encList["name10"]][1][0] + equipment[encList["equip10"]][1][0], creatures[encList["name10"]][1][1] + equipment[encList["equip10"]][1][1], creatures[encList["name10"]][1][2] + equipment[encList["equip10"]][1][2], creatures[encList["name10"]][1][3] + equipment[encList["equip10"]][1][3], creatures[encList["name10"]][1][4] + equipment[encList["equip10"]][1][4]],
             [0, 0]],
        26: [[creatures[encList["name11"]][0][0] + equipment[encList["equip11"]][0][0], creatures[encList["name11"]][0][1] + equipment[encList["equip11"]][0][1], creatures[encList["name11"]][0][2] + equipment[encList["equip11"]][0][2], creatures[encList["name11"]][0][3] + equipment[encList["equip11"]][0][3], creatures[encList["name11"]][0][4] + equipment[encList["equip11"]][0][4], creatures[encList["name11"]][0][5] + equipment[encList["equip11"]][0][5], creatures[encList["name11"]][0][6] + equipment[encList["equip11"]][0][6]],
             [creatures[encList["name11"]][1][0] + equipment[encList["equip11"]][1][0], creatures[encList["name11"]][1][1] + equipment[encList["equip11"]][1][1], creatures[encList["name11"]][1][2] + equipment[encList["equip11"]][1][2], creatures[encList["name11"]][1][3] + equipment[encList["equip11"]][1][3], creatures[encList["name11"]][1][4] + equipment[encList["equip11"]][1][4]],
             [0, 0]],
        27: [[creatures[encList["name12"]][0][0] + equipment[encList["equip12"]][0][0], creatures[encList["name12"]][0][1] + equipment[encList["equip12"]][0][1], creatures[encList["name12"]][0][2] + equipment[encList["equip12"]][0][2], creatures[encList["name12"]][0][3] + equipment[encList["equip12"]][0][3], creatures[encList["name12"]][0][4] + equipment[encList["equip12"]][0][4], creatures[encList["name12"]][0][5] + equipment[encList["equip12"]][0][5], creatures[encList["name12"]][0][6] + equipment[encList["equip12"]][0][6]],
             [creatures[encList["name12"]][1][0] + equipment[encList["equip12"]][1][0], creatures[encList["name12"]][1][1] + equipment[encList["equip12"]][1][1], creatures[encList["name12"]][1][2] + equipment[encList["equip12"]][1][2], creatures[encList["name12"]][1][3] + equipment[encList["equip12"]][1][3], creatures[encList["name12"]][1][4] + equipment[encList["equip12"]][1][4]],
             [0, 0]],
        28: [[creatures[encList["name13"]][0][0] + equipment[encList["equip13"]][0][0], creatures[encList["name13"]][0][1] + equipment[encList["equip13"]][0][1], creatures[encList["name13"]][0][2] + equipment[encList["equip13"]][0][2], creatures[encList["name13"]][0][3] + equipment[encList["equip13"]][0][3], creatures[encList["name13"]][0][4] + equipment[encList["equip13"]][0][4], creatures[encList["name13"]][0][5] + equipment[encList["equip13"]][0][5], creatures[encList["name13"]][0][6] + equipment[encList["equip13"]][0][6]],
             [creatures[encList["name13"]][1][0] + equipment[encList["equip13"]][1][0], creatures[encList["name13"]][1][1] + equipment[encList["equip13"]][1][1], creatures[encList["name13"]][1][2] + equipment[encList["equip13"]][1][2], creatures[encList["name13"]][1][3] + equipment[encList["equip13"]][1][3], creatures[encList["name13"]][1][4] + equipment[encList["equip13"]][1][4]],
             [0, 0]],
        29: [[creatures[encList["name14"]][0][0] + equipment[encList["equip14"]][0][0], creatures[encList["name14"]][0][1] + equipment[encList["equip14"]][0][1], creatures[encList["name14"]][0][2] + equipment[encList["equip14"]][0][2], creatures[encList["name14"]][0][3] + equipment[encList["equip14"]][0][3], creatures[encList["name14"]][0][4] + equipment[encList["equip14"]][0][4], creatures[encList["name14"]][0][5] + equipment[encList["equip14"]][0][5], creatures[encList["name14"]][0][6] + equipment[encList["equip14"]][0][6]],
             [creatures[encList["name14"]][1][0] + equipment[encList["equip14"]][1][0], creatures[encList["name14"]][1][1] + equipment[encList["equip14"]][1][1], creatures[encList["name14"]][1][2] + equipment[encList["equip14"]][1][2], creatures[encList["name14"]][1][3] + equipment[encList["equip14"]][1][3], creatures[encList["name14"]][1][4] + equipment[encList["equip14"]][1][4]],
             [0, 0]],
        30: [[creatures[encList["name15"]][0][0] + equipment[encList["equip15"]][0][0], creatures[encList["name15"]][0][1] + equipment[encList["equip15"]][0][1], creatures[encList["name15"]][0][2] + equipment[encList["equip15"]][0][2], creatures[encList["name15"]][0][3] + equipment[encList["equip15"]][0][3], creatures[encList["name15"]][0][4] + equipment[encList["equip15"]][0][4], creatures[encList["name15"]][0][5] + equipment[encList["equip15"]][0][5], creatures[encList["name15"]][0][6] + equipment[encList["equip15"]][0][6]],
             [creatures[encList["name15"]][1][0] + equipment[encList["equip15"]][1][0], creatures[encList["name15"]][1][1] + equipment[encList["equip15"]][1][1], creatures[encList["name15"]][1][2] + equipment[encList["equip15"]][1][2], creatures[encList["name15"]][1][3] + equipment[encList["equip15"]][1][3], creatures[encList["name15"]][1][4] + equipment[encList["equip15"]][1][4]],
             [0, 0]]
        }

#the instance of all units used in a battle
battleDict = copy.deepcopy(deckStats)
battleDict.update(copy.deepcopy(encStats))

#main function
def main():
    # initialize the pygame module
    pygame.init()
        
    #load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Gobrin")
    
    #define a variable to control the main loop
    running = True
    
    global combatClicked
    global boardClicked
    global handClicked
    global playerTurn
    global combat
    
    displayUnit = 0
    update(displayUnit = displayUnit)

    #main loop
    while running:
        
        xpos, ypos = mouse[0]
        
        #battleinput
        if combatClicked == True and mouse[1] == 0:
            combatClicked = False
            combat = True
            runCombat()
            update(displayUnit = displayUnit)
        elif boardClicked == True and mouse[1] == 0:
            boardClicked = False
            boardInput(index=index)
            update(displayUnit = displayUnit)
        elif handClicked == True and mouse[1] == 0:
            handClicked = False
            handInput(index=index)
            update(displayUnit = displayUnit)
        elif xpos >= 1670 and xpos <= 1750 and ypos >= 520 and ypos <= 560 and mouse[1] == 1:
            combatClicked = True
        #remember the < vs <= is crucial to get correct index
        elif xpos >= 435 and xpos < 1485 and ypos >= 10 and ypos < 670:
            index = ((ypos - 10) // 220) * 7 + ((xpos - 435) // 150)
            displayUnit = board[index]
            update(displayUnit = displayUnit)
            if mouse[1] == 1:
                boardClicked = True
        #remember the < vs <= is crucial to get correct index
        elif xpos >= 885 and xpos < 1785 and ypos >= 850 and ypos <= 1070:
            index = (xpos - 885) // 150
            if playerTurn == True and index >= 0 and index <= len(playerHand) - 1:
                displayUnit = playerHand[index]
                update(displayUnit = displayUnit)
            if playerTurn == False and index >= 0 and index <= len(enemyHand) - 1:
                displayUnit = enemyHand[index]
                update(displayUnit = displayUnit)
            if mouse[1] == 1:
                handClicked = True
        
        #event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            #you can add 'if event.button = 1' to limit input to your list and not have errors
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse[event.button] = 1
                mouse[0] = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse[event.button] = 0
                mouse[0] = event.pos
            elif event.type == pygame.MOUSEMOTION:
                mouse[0] = event.pos

'''Display Functions'''
#blits stuff to screen
def blit(image, screen, x, y):
    screen.blit(image, [x, y])

#updates visuals
def update(displayUnit):
    #create a surface on screen that has the size of 1920 x 1080
    screen = pygame.display.set_mode((1920, 1080))
    
    #initialize the font module
    pygame.font.init()
    
    #font
    font = pygame.font.Font(None, 60)
    if (playerTurn == True):
        deckCounter = font.render(f"Deck: {len(playerDeck)}", True, (0, 0, 0))
        apCounter = font.render(f"Command Points: {playerTotalAp}", True, (0, 0, 0))
        apBreakdown = font.render(f"Available: {playerAp} In Use: {playerUpkeep}", True, (0, 0, 0))
    if (playerTurn == False):
        deckCounter = font.render(f"Deck: {len(enemyDeck)}", True, (0, 0, 0))
        apCounter = font.render(f"Command Points: {enemyTotalAp}", True, (0, 0, 0))
        apBreakdown = font.render(f"Available: {enemyAp} In Use: {enemyUpkeep}", True, (0, 0, 0))
    playerHpCounter = font.render(f"Hitpoints: {playerHp}", True, (0, 0, 0))
    enemyHpCounter = font.render(f"Enemy Hitpoints: {enemyHp}", True, (0, 0, 0))
    blit(background, screen, 0, 0)
    blit(field, screen, 425, 0)
    blit(hand, screen, 875, 840)
    blit(deckCounter, screen, 0, 50)
    blit(playerHpCounter, screen, 0, 150)
    blit(enemyHpCounter, screen, 0, 200)
    blit(apCounter, screen, 0, 300)
    blit(apBreakdown, screen, 0, 350)
    blit(combatButton, screen, 1670, 520)
    blit(spells, screen, 125, 840)
    if displayUnit >= 1:
        #if displayUnit >= 16:
        #name = font.render(f"{encList[f'name{displayUnit - 15}']} with {encList[f'equip{displayUnit - 15}']}", True, (0, 0, 0))
        #else:
        #name = font.render(f"{deckList[f'name{displayUnit}']} with {deckList[f'equip{displayUnit']}", True, (0, 0, 0))
        dmg = font.render(f"Damage: {battleDict[displayUnit][0][0]}", True, (0, 0, 0))
        hp = font.render(f"Hitpoints: {battleDict[displayUnit][0][1]}", True, (0, 0, 0))
        movement = font.render(f"Speed: {battleDict[displayUnit][0][2]}", True, (0, 0, 0))
        shot = font.render(f"Range: {battleDict[displayUnit][0][4]}", True, (0, 0, 0))
        #blit(name, screen, 1505, 50)
        blit(hp, screen, 1505, 100)
        blit(movement, screen, 1505, 150)
        blit(dmg, screen, 1505, 200)
        blit(shot, screen, 1505, 250)
        abilities = 0
        if battleDict[displayUnit][0][3] >= 2:
            attacks = font.render(f"Multiattack {battleDict[displayUnit][0][3]}x", True, (0, 0, 0))
            blit(attacks, screen, 1505, abilities * 50 + 300)
            abilities = abilities + 1
        if battleDict[displayUnit][1][3] >= 1:
            splash = font.render(f"Splash {battleDict[displayUnit][1][3]}", True, (0, 0, 0))
            blit(splash, screen, 1505, abilities * 50 + 300)
            abilities = abilities + 1
        if battleDict[displayUnit][1][0] >= 1:
            taunt = font.render(f"Taunt {battleDict[displayUnit][1][0]} Turns", True, (0, 0, 0))
            blit(taunt, screen, 1505, abilities * 50 + 300)
            abilities = abilities + 1
        if battleDict[displayUnit][1][1] >= 1:
            heal = font.render(f"Heal {battleDict[displayUnit][1][1]}", True, (0, 0, 0))
            blit(heal, screen, 1505, abilities * 50 + 300)
            abilities = abilities + 1
        if battleDict[displayUnit][1][2] >= 1:
            berserk = font.render(f"Berserk +{battleDict[displayUnit][1][2]}/Turn", True, (0, 0, 0))
            blit(berserk, screen, 1505, abilities * 50 + 300)
            abilities = abilities + 1
        if battleDict[displayUnit][2][0] >= 1:
            taunted = font.render(f"TAUNTED {battleDict[displayUnit][2][0]} TURNS", True, (255, 0, 0))
            blit(taunted, screen, 1505, abilities * 50 + 300)
            abilities = abilities + 1
    for space in selectBoard:
        if(space <= -3):
            blit(selector, screen, 150 * (selectBoard.index(space) % 7) + 445, 220 * (selectBoard.index(space) // 7) + 20)
    if (playerTurn == True):
        for card in playerHand:
            dmg = font.render(f"{battleDict[card][0][0]}", True, (255, 0, 0))
            hp = font.render(f"{battleDict[card][0][1]}", True, (0, 255, 0))
            blit(artDict[card][0], screen, 150 * playerHand.index(card) + 895, 906)
            blit(artDict[card][1], screen, 150 * playerHand.index(card) + 895, 906)
            blit(dmg, screen, 150 * playerHand.index(card) + 895 + 10, 906 - 30)
            blit(hp, screen, 150 * playerHand.index(card) + 895 + 80, 906 - 30)
    if (playerTurn == False):
        for card in enemyHand:
            dmg = font.render(f"{battleDict[card][0][0]}", True, (255, 0, 0))
            hp = font.render(f"{battleDict[card][0][1]}", True, (0, 255, 0))
            blit(artDict[card][0], screen, 150 * enemyHand.index(card) + 895, 906)
            blit(artDict[card][1], screen, 150 * enemyHand.index(card) + 895, 906)
            blit(dmg, screen, 150 * enemyHand.index(card) + 895 + 10, 906 - 30)
            blit(hp, screen, 150 * enemyHand.index(card) + 895 + 80, 906 - 30)
    for card in board:
        if(combat == True and playerTurn == True):
            board.reverse()
        if(card >= 1):
            dmg = font.render(f"{battleDict[card][0][0]}", True, (255, 0, 0))
            hp = font.render(f"{battleDict[card][0][1]}", True, (0, 255, 0))
            body = artDict[card][0]
            equip = artDict[card][1]
            if(card >= 16):
                body = pygame.transform.flip(body, True, False)
                equip = pygame.transform.flip(equip, True, False)
            if(card == active):
                blit(body, screen, 150 * ((board.index(card) - move) % 7) + 445, 220 * (board.index(card) // 7) + 61)
                blit(equip, screen, 150 * ((board.index(card) - move) % 7) + 445, 220 * (board.index(card) // 7) + 61)
                blit(dmg, screen, 150 * ((board.index(card) - move) % 7) + 445 + 10, 220 * (board.index(card) // 7) + 61 - 30)
                blit(hp, screen, 150 * ((board.index(card) - move) % 7) + 445 + 80, 220 * (board.index(card) // 7) + 61 - 30)
            else:
                blit(body, screen, 150 * (board.index(card) % 7) + 445, 220 * (board.index(card) // 7) + 61)
                blit(equip, screen, 150 * (board.index(card) % 7) + 445, 220 * (board.index(card) // 7) + 61)
                blit(dmg, screen, 150 * (board.index(card) % 7) + 445 + 10, 220 * (board.index(card) // 7) + 61 - 30)
                blit(hp, screen, 150 * (board.index(card) % 7) + 445 + 80, 220 * (board.index(card) // 7) + 61 - 30)
        if(combat == True and playerTurn == True):
            board.reverse()
    pygame.display.flip()

'''battleInput'''
#processes input on the board
def boardInput(index):
    global playerTurn
    global select
    global playerAp
    global playerUpkeep
    global enemyAp
    global enemyUpkeep
    global displayUnit
    global selectors
    #if selector clicked
    if(selectBoard[index] <= -3):
        #if placing unit from hand
        if(board.count(select) == 0):
            #cleanup
            if playerTurn == True:
                playerAp = playerAp - battleDict[select][0][5]
                playerUpkeep = playerUpkeep + battleDict[select][0][6]
                playerHand.remove(select)
            else:
                enemyAp = enemyAp - battleDict[select][0][5]
                enemyUpkeep = enemyUpkeep + battleDict[select][0][6]
                enemyHand.remove(select)
            #place unit
            board[index] = select
        elif board[index] >= 1 and battleDict[board[index]][1][4] >= 1:
            if(board.index(select) % 7 == 0):
                board[board.index(select)] = -1
            elif(board.index(select) % 7 == 6):
                board[board.index(select)] = -2
            else:
                board[board.index(select)] = 0
            battleDict[board[index]][2][1] = select
        elif board[index] >= 1 and battleDict[select][1][4] >= 1:
            if(index % 7 == 0):
                board[index] = -1
            elif(index % 7 == 6):
                board[index] = -2
            else:
                board[index] = 0
            battleDict[select][2][1] = board[index]
        #if moving unit on board
        else:
            #switch units/move unit
            board[board.index(select)] = board[index]
            board[index] = select
        removeSelectors()
        select = 0
    #if unit clicked
    elif(board[index] >= 1):
        displayUnit = board[index]
        if playerTurn == True:
            #if clicked unit is friendly and not taunted and middle row is safe
            if(board[index] >= 1 and board[index] <= 15 and battleDict[board[index]][2][0] <= 0 and board[(index % 7) + 7] <= 15):
                removeSelectors()
                select = board[index]
                row = 0
                #deploy selectors
                while True:
                    if(row == 3):
                        break
                    if board[(index % 7) + (7 * row)] <= 0 or (board[(index % 7) + (7 * row)] <= 15 and battleDict[board[(index % 7) + (7 * row)]][2][0] <= 0 and board[(index % 7) + (7 * row)] != select):
                        selectBoard[(index % 7) + (7 * row)] = - (3 + selectors)
                        selectors = selectors + 1
                    row = row + 1
        else:
            #if clicked unit is enemy and not taunted
            if(board[index] >= 16 and battleDict[board[index]][2][0] <= 0):
                #if middle row is safe
                if(board[(index % 7) + 7] >= 16 or board[(index % 7) + 7] <= 0):
                    removeSelectors()
                    select = board[index]
                    #deploy selectors
                    row = 0
                    while True:
                        if(row == 3):
                            break
                        if board[(index % 7) + (7 * row)] <= 0 or (board[(index % 7) + (7 * row)] >= 16 and battleDict[board[(index % 7) + (7 * row)]][2][0] <= 0 and board[(index % 7) + (7 * row)] != select):
                            selectBoard[(index % 7) + (7 * row)] = - (3 + selectors)
                            selectors = selectors + 1
                        row = row + 1
    #if empty space clicked
    else:
        removeSelectors()

#processes input on the hand
def handInput(index):
    global select
    global selectors
    global playerTurn
    removeSelectors()
    #if its your turn and you have a card in that slot
    if playerTurn == True and index <= len(playerHand) - 1:
        #if you can afford
        if playerAp - battleDict[playerHand[index]][0][5] >= 0:
            select = playerHand[index]
            row = 0
            #deploy selectors
            while True:
                if(row == 3):
                    break
                if(board[7 * row] == -1):
                    selectBoard[7 * row] = -1 * (3 + selectors)
                    selectors = selectors + 1
                row = row + 1
    #if its their turn and they have a card in that slot
    elif playerTurn == False and index <= len(enemyHand) - 1:
        #if they can afford
        if enemyAp - battleDict[enemyHand[index]][0][5] >= 0:
            select = enemyHand[index]
            row = 0
            #deploy selectors
            while True:
                if(row == 3):
                    break
                if(board[6 + (7 * row)] == -2):
                    selectBoard[6 + (7 * row)] = -1 * (3 + selectors)
                    selectors = selectors + 1
                row = row + 1

'''ability functions'''
#draws a card
def drawCard(player):
    if(player == True):
        if(len(playerDeck) >= 1 and len(playerHand) <= 5):
            card = random.randint(0, len(playerDeck)-1)
            playerHand.append(playerDeck[card])
            playerDeck.pop(card)
    elif(player == False):
        if(len(enemyDeck) >= 1 and len(enemyHand) <= 5):
            card = random.randint(0, len(enemyDeck)-1)
            enemyHand.append(enemyDeck[card])
            enemyDeck.pop(card)

#handles splash damage calculations
def splash(unit, target):
    global playerTurn
    if battleDict[unit][1][3] >= 1:
        if playerTurn == True:
            if board.index(target) + 1 <= 20 and board.index(target) + 1 >= 0 and board[board.index(target) + 1] >= 16:
                battleDict[board[board.index(target) + 1]][0][1] = battleDict[board[board.index(target) + 1]][0][1] - battleDict[unit][1][3]
                processFatality(damagedUnit = board[board.index(target) + 1], player = False)
            if board.index(target) - 1 <= 20 and board.index(target) - 1 >= 0 and board[board.index(target) - 1] >= 16:
                battleDict[board[board.index(target) - 1]][0][1] = battleDict[board[board.index(target) - 1]][0][1] - battleDict[unit][1][3]
                processFatality(damagedUnit = board[board.index(target) - 1], player = False)
            if board.index(target) + 7 <= 20 and board.index(target) + 7 >= 0 and board[board.index(target) + 7] >= 16:
                battleDict[board[board.index(target) + 7]][0][1] = battleDict[board[board.index(target) + 7]][0][1] - battleDict[unit][1][3]
                processFatality(damagedUnit = board[board.index(target) + 7], player = False)
            if board.index(target) - 7 <= 20 and board.index(target) - 7 >= 0 and board[board.index(target) - 7] >= 16:
                battleDict[board[board.index(target) - 7]][0][1] = battleDict[board[board.index(target) - 7]][0][1] - battleDict[unit][1][3]
                processFatality(damagedUnit = board[board.index(target) - 7], player = False)
        if playerTurn == False:
            if board.index(target) + 1 <= 20 and board.index(target) + 1 >= 0 and board[board.index(target) + 1] >= 1 and board[board.index(target) + 1] <= 15:
                battleDict[board[board.index(target) + 1]][0][1] = battleDict[board[board.index(target) + 1]][0][1] - battleDict[unit][1][3]
                processFatality(damagedUnit = board[board.index(target) + 1], player = True)
            if board.index(target) - 1 <= 20 and board.index(target) - 1 >= 0 and board[board.index(target) - 1] >= 1 and board[board.index(target) - 1] <= 15:
                battleDict[board[board.index(target) - 1]][0][1] = battleDict[board[board.index(target) - 1]][0][1] - battleDict[unit][1][3]
                processFatality(damagedUnit = board[board.index(target) - 1], player = True)
            if board.index(target) + 7 <= 20 and board.index(target) + 7 >= 0 and board[board.index(target) + 7] >= 1 and board[board.index(target) + 7] <= 15:
                battleDict[board[board.index(target) + 7]][0][1] = battleDict[board[board.index(target) + 7]][0][1] - battleDict[unit][1][3]
                processFatality(damagedUnit = board[board.index(target) + 7], player = True)
            if board.index(target) - 7 <= 20 and board.index(target) - 7 >= 0 and board[board.index(target) - 7] >= 1 and board[board.index(target) - 7] <= 15:
                battleDict[board[board.index(target) - 7]][0][1] = battleDict[board[board.index(target) - 7]][0][1] - battleDict[unit][1][3]
                processFatality(damagedUnit = board[board.index(target) - 7], player = True)

'''general calculation functions'''
#checks for a processes fatalities
def processFatality(damagedUnit, player):
    global playerTurn
    global combat
    global playerUpkeep
    global enemyUpkeep
    if combat == True and playerTurn == True:
        board.reverse()
    if(battleDict[damagedUnit][0][1] <= 0):
        if player == True:
            playerUpkeep = playerUpkeep - battleDict[damagedUnit][0][6]
        else:
            enemyUpkeep = enemyUpkeep - battleDict[damagedUnit][0][6]
        if(board.index(damagedUnit) % 7 == 0):
            board[board.index(damagedUnit)] = -1
        elif(board.index(damagedUnit) % 7 == 6):
            board[board.index(damagedUnit)] = -2
        else:
            board[board.index(damagedUnit)] = 0
    if combat == True and playerTurn == True:
        board.reverse()

#removes selector locations from board
def removeSelectors():
    global selectors
    for space in selectBoard:
        if(space <= -3):
                selectBoard[selectBoard.index(space)] = 0
    selectors = 0

#runs combat
def runCombat():
    removeSelectors()
    global playerTurn
    global enemyHp
    global playerHp
    global combat
    global playerUpkeep
    global enemyUpkeep
    global playerAp
    global enemyAp
    global active
    global move
    global playerTotalAp
    global enemyTotalAp
    if (playerTurn == True):
        board.reverse()
        for unit in board:
            if(unit >= 1 and unit <= 15):
                active = unit
                move = 0
                newPosition = 0
                attacks = battleDict[unit][0][3]
                ranging = 1
                attacking = True
                while True:
                    if(attacks == 0 and move == battleDict[unit][0][2]):
                        break
                    elif(attacks == 0 and board[board.index(unit) - (move + 1)] != 0):
                        break
                    elif(ranging == battleDict[unit][0][4] + 1 and move == battleDict[unit][0][2]):
                        break
                    elif(ranging == battleDict[unit][0][4] + 1 and board[board.index(unit) - (move + 1)] != 0):
                        break
                    if (ranging == battleDict[unit][0][4] + 1 or attacks == 0) and (attacking == True):
                        attacking = False
                        ranging = 1
                    elif(attacks >= 1 and attacking == True):
                        target = board[board.index(unit) - (ranging + move)]
                        if (target == -2):
                            enemyHp = enemyHp - battleDict[unit][0][0]
                            #check victory
                            attacks = attacks - 1
                        elif (target >= 16):
                            battleDict[target][0][1] = battleDict[target][0][1] - battleDict[unit][0][0]
                            battleDict[target][2][0] = battleDict[unit][1][0]
                            if battleDict[unit][1][3] >= 1:
                                splash(unit = unit, target = target)
                            if(battleDict[target][0][1] <= 0):
                                enemyUpkeep = enemyUpkeep - battleDict[target][0][6]
                                #remove dead unit here and now
                                if(board.index(target) % 7 == 0):
                                    board[board.index(target)] = -2
                                else:
                                    board[board.index(target)] = 0
                            attacks = attacks - 1
                        else:
                            ranging = ranging + 1
                    elif(move <= battleDict[unit][0][2] - 1 and attacking == False):
                        if(board[board.index(unit) - (move + 1)] == 0):
                            move = move + 1
                            attacking = True
                battleDict[unit][0][0] = battleDict[unit][0][0] + battleDict[unit][1][2]
                battleDict[unit][2][0] = battleDict[unit][2][0] - 1
                if battleDict[unit][1][1] >= 1:
                    healthsMissing = []
                    healTargets = []
                    for target in board:
                        if target >= 1 and target <= 15:
                            healTargets.append(target)
                            healthsMissing.append(deckStats[target][0][1] - battleDict[target][0][1])
                    battleDict[healTargets[healthsMissing.index(max(healthsMissing))]][0][1] = min(battleDict[healTargets[healthsMissing.index(max(healthsMissing))]][0][1] + battleDict[unit][1][1], deckStats[healTargets[healthsMissing.index(max(healthsMissing))]][0][1])
                newPosition = board.index(unit) - move
                if(board.index(unit) % 7 == 6):
                    board[board.index(unit)] = -1
                else:
                    board[board.index(unit)] = 0
                board[newPosition] = unit
        board.reverse()
        if(playerTotalAp <= 4):
            playerTotalAp = playerTotalAp + 1
        playerTurn = False
        drawCard(player == True)
    elif (playerTurn == False):
        for unit in board:
            if(unit >= 16):
                active = unit
                move = 0
                newPosition = 0
                attacks = battleDict[unit][0][3]
                ranging = 1
                attacking = True
                while True:
                    if(attacks == 0 and move == battleDict[unit][0][2]):
                        break
                    elif(attacks == 0 and board[board.index(unit) - (move + 1)] != 0):
                        break
                    elif(ranging == battleDict[unit][0][4] + 1 and move == battleDict[unit][0][2]):
                        break
                    elif(ranging == battleDict[unit][0][4] + 1 and board[board.index(unit) - (move + 1)] != 0):
                        break
                    elif(ranging == battleDict[unit][0][4] + 1 or attacks == 0) and (attacking == True):
                        attacking = False
                        ranging = 1
                    elif(attacks >= 1 and attacking == True):
                        target = board[board.index(unit) - (ranging + move)]
                        if (target == -1):
                            playerHp = playerHp - battleDict[unit][0][0]
                            #check victory
                            attacks = attacks - 1
                        elif (target >= 1 and target <= 15):
                            battleDict[target][0][1] = battleDict[target][0][1] - battleDict[unit][0][0]
                            battleDict[target][2][0] = battleDict[unit][1][0]
                            if battleDict[unit][1][3] >= 1:
                                splash(unit = unit, target = target)
                            if(battleDict[target][0][1] <= 0):
                                playerUpkeep = playerUpkeep - battleDict[target][0][6]
                                #remove dead unit here and now
                                if(board.index(target) % 7 == 0):
                                    board[board.index(target)] = -1
                                else:
                                    board[board.index(target)] = 0
                            attacks = attacks - 1
                        else:
                            ranging = ranging + 1
                    elif(move <= battleDict[unit][0][2] - 1 and attacking == False):
                        if(board[board.index(unit) - (move + 1)] == 0):
                            move = move + 1
                            attacking = True
                battleDict[unit][0][0] = battleDict[unit][0][0] + battleDict[unit][1][2]
                battleDict[unit][2][0] = battleDict[unit][2][0] - 1
                if battleDict[unit][1][1] >= 1:
                    healthsMissing = []
                    healTargets = []
                    for target in board:
                        if target >= 16:
                            healTargets.append(target)
                            healthsMissing.append(encStats[target][0][1] - battleDict[target][0][1])
                    battleDict[healTargets[healthsMissing.index(max(healthsMissing))]][0][1] = min(battleDict[healTargets[healthsMissing.index(max(healthsMissing))]][0][1] + battleDict[unit][1][1], encStats[healTargets[healthsMissing.index(max(healthsMissing))]][0][1])
                newPosition = board.index(unit) - move
                if(board.index(unit) % 7 == 6):
                    board[board.index(unit)] = -2
                else:
                    board[board.index(unit)] = 0
                board[newPosition] = unit
        if(enemyTotalAp <= 4):
            enemyTotalAp = enemyTotalAp + 1
        playerTurn = True
        drawCard(player == False)
    playerAp = playerTotalAp - playerUpkeep
    enemyAp = enemyTotalAp - enemyUpkeep
    active = 0
    combat = False

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
