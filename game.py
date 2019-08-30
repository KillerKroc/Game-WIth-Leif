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



import random
import copy
import pygame
from pygame.locals import *

#load sprites
field = pygame.image.load("field.png")
combatButton = pygame.image.load("fight.png")
selector = pygame.image.load("select.png")
hand = pygame.image.load("hand.png")
background = pygame.image.load("background.png")
#define variables
playerHp = 10
enemyHp = 10
playerTurn = True
combat = False
playerAp = 1
enemyAp = 1
playerUpkeep = 0
enemyUpkeep = 0
active = 0
move = 0
selectors = 0
combatClicked = False
player = True
displayUnit = 0

#the mouse
mouse = [(0,0), 0, 0, 0, 0, 0, 0] #(pos, b1,b2,b3,b4,b5,b6)

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

#the stats of the creatures in the game (some might not be allowed certain equipment implement when we need)
creatures = {
        #damage, health, movement, attacks, range, cost, upkeep, taunt, heal, berserk, splash
        "orc": [2, 4, 1, 1, 1,
                1, 1,
                0, 0, 0 ,0],
        "goblin": [3, 2, 1, 1, 1,
                   1, 1,
                   0, 0, 0, 0]
        }

#the stats of equipment in the game (might make seperate one for armor, weapons, runes, artifacts, etc)
equipment = {
        #damage, health, movement, attacks, range, cost, upkeep, taunt, heal, berserk, splash
        "dogslicer": [1, 2, 1, 0, 0,
                      0, 0,
                      0, 0, 1, 0],
        "knives": [0, 2, 2, 1, 0,
                   0, 0,
                   0, 0, 0, 0],
        "bow": [2, 0, 0, 0, 2,
                0, 0,
                0, 0, 0, 2],
        "staff":[1, 2, 0, 0, 1,
                 0, 0,
                 0, 2, 0, 0],
        "": [0, 6, 1, 0, 0,
             0, 0,
             2, 0, 0, 0]
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
        #damage, health, movement, attacks, range, cost, upkeep, taunt, heal, berserk, splash, taunted
        1: [creatures[deckList["name1"]][0] + equipment[deckList["equip1"]][0], creatures[deckList["name1"]][1] + equipment[deckList["equip1"]][1], creatures[deckList["name1"]][2] + equipment[deckList["equip1"]][2], creatures[deckList["name1"]][3] + equipment[deckList["equip1"]][3], creatures[deckList["name1"]][4] + equipment[deckList["equip1"]][4],
            creatures[deckList["name1"]][5] + equipment[deckList["equip1"]][5], creatures[deckList["name1"]][6] + equipment[deckList["equip1"]][6],
            creatures[deckList["name1"]][7] + equipment[deckList["equip1"]][7], creatures[deckList["name1"]][8] + equipment[deckList["equip1"]][8], creatures[deckList["name1"]][9] + equipment[deckList["equip1"]][9], creatures[deckList["name1"]][10] + equipment[deckList["equip1"]][10],
            0],
        2: [creatures[deckList["name2"]][0] + equipment[deckList["equip2"]][0], creatures[deckList["name2"]][1] + equipment[deckList["equip2"]][1], creatures[deckList["name2"]][2] + equipment[deckList["equip2"]][2], creatures[deckList["name2"]][3] + equipment[deckList["equip2"]][3], creatures[deckList["name2"]][4] + equipment[deckList["equip2"]][4],
            creatures[deckList["name2"]][5] + equipment[deckList["equip2"]][5], creatures[deckList["name2"]][6] + equipment[deckList["equip2"]][6], 
            creatures[deckList["name2"]][7] + equipment[deckList["equip2"]][7], creatures[deckList["name2"]][8] + equipment[deckList["equip2"]][8], creatures[deckList["name2"]][9] + equipment[deckList["equip2"]][9], creatures[deckList["name2"]][10] + equipment[deckList["equip2"]][10],
            0],
        3: [creatures[deckList["name3"]][0] + equipment[deckList["equip3"]][0], creatures[deckList["name3"]][1] + equipment[deckList["equip3"]][1], creatures[deckList["name3"]][2] + equipment[deckList["equip3"]][2], creatures[deckList["name3"]][3] + equipment[deckList["equip3"]][3], creatures[deckList["name3"]][4] + equipment[deckList["equip3"]][4],
            creatures[deckList["name3"]][5] + equipment[deckList["equip3"]][5], creatures[deckList["name3"]][6] + equipment[deckList["equip3"]][6], 
            creatures[deckList["name3"]][7] + equipment[deckList["equip3"]][7], creatures[deckList["name3"]][8] + equipment[deckList["equip3"]][8], creatures[deckList["name3"]][9] + equipment[deckList["equip3"]][9], creatures[deckList["name3"]][10] + equipment[deckList["equip3"]][10],
            0],
        4: [creatures[deckList["name4"]][0] + equipment[deckList["equip4"]][0], creatures[deckList["name4"]][1] + equipment[deckList["equip4"]][1], creatures[deckList["name4"]][2] + equipment[deckList["equip4"]][2], creatures[deckList["name4"]][3] + equipment[deckList["equip4"]][3], creatures[deckList["name4"]][4] + equipment[deckList["equip4"]][4],
            creatures[deckList["name4"]][5] + equipment[deckList["equip4"]][5], creatures[deckList["name4"]][6] + equipment[deckList["equip4"]][6], 
            creatures[deckList["name4"]][7] + equipment[deckList["equip4"]][7], creatures[deckList["name4"]][8] + equipment[deckList["equip4"]][8], creatures[deckList["name4"]][9] + equipment[deckList["equip4"]][9], creatures[deckList["name4"]][10] + equipment[deckList["equip4"]][10],
            0],
        5: [creatures[deckList["name5"]][0] + equipment[deckList["equip5"]][0], creatures[deckList["name5"]][1] + equipment[deckList["equip5"]][1], creatures[deckList["name5"]][2] + equipment[deckList["equip5"]][2], creatures[deckList["name5"]][3] + equipment[deckList["equip5"]][3], creatures[deckList["name5"]][4] + equipment[deckList["equip5"]][4],
            creatures[deckList["name5"]][5] + equipment[deckList["equip5"]][5], creatures[deckList["name5"]][6] + equipment[deckList["equip5"]][6], 
            creatures[deckList["name5"]][7] + equipment[deckList["equip5"]][7], creatures[deckList["name5"]][8] + equipment[deckList["equip5"]][8], creatures[deckList["name5"]][9] + equipment[deckList["equip5"]][9], creatures[deckList["name5"]][10] + equipment[deckList["equip5"]][10],
            0],
        6: [creatures[deckList["name6"]][0] + equipment[deckList["equip6"]][0], creatures[deckList["name6"]][1] + equipment[deckList["equip6"]][1], creatures[deckList["name6"]][2] + equipment[deckList["equip6"]][2], creatures[deckList["name6"]][3] + equipment[deckList["equip6"]][3], creatures[deckList["name6"]][4] + equipment[deckList["equip6"]][4], 
            creatures[deckList["name6"]][5] + equipment[deckList["equip6"]][5], creatures[deckList["name6"]][6] + equipment[deckList["equip6"]][6], 
            creatures[deckList["name6"]][7] + equipment[deckList["equip6"]][7], creatures[deckList["name6"]][8] + equipment[deckList["equip6"]][8], creatures[deckList["name6"]][9] + equipment[deckList["equip6"]][9], creatures[deckList["name6"]][10] + equipment[deckList["equip6"]][10],
            0],
        7: [creatures[deckList["name7"]][0] + equipment[deckList["equip7"]][0], creatures[deckList["name7"]][1] + equipment[deckList["equip7"]][1], creatures[deckList["name7"]][2] + equipment[deckList["equip7"]][2], creatures[deckList["name7"]][3] + equipment[deckList["equip7"]][3], creatures[deckList["name7"]][4] + equipment[deckList["equip7"]][4], 
            creatures[deckList["name7"]][5] + equipment[deckList["equip7"]][5], creatures[deckList["name7"]][6] + equipment[deckList["equip7"]][6], 
            creatures[deckList["name7"]][7] + equipment[deckList["equip7"]][7], creatures[deckList["name7"]][8] + equipment[deckList["equip7"]][8], creatures[deckList["name7"]][9] + equipment[deckList["equip7"]][9], creatures[deckList["name7"]][10] + equipment[deckList["equip7"]][10],
            0],
        8: [creatures[deckList["name8"]][0] + equipment[deckList["equip8"]][0], creatures[deckList["name8"]][1] + equipment[deckList["equip8"]][1], creatures[deckList["name8"]][2] + equipment[deckList["equip8"]][2], creatures[deckList["name8"]][3] + equipment[deckList["equip8"]][3], creatures[deckList["name8"]][4] + equipment[deckList["equip8"]][4],
            creatures[deckList["name8"]][5] + equipment[deckList["equip8"]][5], creatures[deckList["name8"]][6] + equipment[deckList["equip8"]][6], 
            creatures[deckList["name8"]][7] + equipment[deckList["equip8"]][7], creatures[deckList["name8"]][8] + equipment[deckList["equip8"]][8], creatures[deckList["name8"]][9] + equipment[deckList["equip8"]][9], creatures[deckList["name8"]][10] + equipment[deckList["equip8"]][10],
            0],
        9: [creatures[deckList["name9"]][0] + equipment[deckList["equip9"]][0], creatures[deckList["name9"]][1] + equipment[deckList["equip9"]][1], creatures[deckList["name9"]][2] + equipment[deckList["equip9"]][2], creatures[deckList["name9"]][3] + equipment[deckList["equip9"]][3], creatures[deckList["name9"]][4] + equipment[deckList["equip9"]][4],
            creatures[deckList["name9"]][5] + equipment[deckList["equip9"]][5], creatures[deckList["name9"]][6] + equipment[deckList["equip9"]][6], 
            creatures[deckList["name9"]][7] + equipment[deckList["equip9"]][7], creatures[deckList["name9"]][8] + equipment[deckList["equip9"]][8], creatures[deckList["name9"]][9] + equipment[deckList["equip9"]][9], creatures[deckList["name9"]][10] + equipment[deckList["equip9"]][10],
            0],
        10: [creatures[deckList["name10"]][0] + equipment[deckList["equip10"]][0], creatures[deckList["name10"]][1] + equipment[deckList["equip10"]][1], creatures[deckList["name10"]][2] + equipment[deckList["equip10"]][2], creatures[deckList["name10"]][3] + equipment[deckList["equip10"]][3], creatures[deckList["name10"]][4] + equipment[deckList["equip10"]][4], 
             creatures[deckList["name10"]][5] + equipment[deckList["equip10"]][5], creatures[deckList["name10"]][6] + equipment[deckList["equip10"]][6], 
             creatures[deckList["name10"]][7] + equipment[deckList["equip10"]][7], creatures[deckList["name10"]][8] + equipment[deckList["equip10"]][8], creatures[deckList["name10"]][9] + equipment[deckList["equip10"]][9], creatures[deckList["name10"]][10] + equipment[deckList["equip10"]][10],
             0],
        11: [creatures[deckList["name11"]][0] + equipment[deckList["equip11"]][0], creatures[deckList["name11"]][1] + equipment[deckList["equip11"]][1], creatures[deckList["name11"]][2] + equipment[deckList["equip11"]][2], creatures[deckList["name11"]][3] + equipment[deckList["equip11"]][3], creatures[deckList["name11"]][4] + equipment[deckList["equip11"]][4],
             creatures[deckList["name11"]][5] + equipment[deckList["equip11"]][5], creatures[deckList["name11"]][6] + equipment[deckList["equip11"]][6], 
             creatures[deckList["name11"]][7] + equipment[deckList["equip11"]][7], creatures[deckList["name11"]][8] + equipment[deckList["equip11"]][8], creatures[deckList["name11"]][9] + equipment[deckList["equip11"]][9], creatures[deckList["name11"]][10] + equipment[deckList["equip11"]][10],
             0],
        12: [creatures[deckList["name12"]][0] + equipment[deckList["equip12"]][0], creatures[deckList["name12"]][1] + equipment[deckList["equip12"]][1], creatures[deckList["name12"]][2] + equipment[deckList["equip12"]][2], creatures[deckList["name12"]][3] + equipment[deckList["equip12"]][3], creatures[deckList["name12"]][4] + equipment[deckList["equip12"]][4],
             creatures[deckList["name12"]][5] + equipment[deckList["equip12"]][5], creatures[deckList["name12"]][6] + equipment[deckList["equip12"]][6], 
             creatures[deckList["name12"]][7] + equipment[deckList["equip12"]][7], creatures[deckList["name12"]][8] + equipment[deckList["equip12"]][8], creatures[deckList["name12"]][9] + equipment[deckList["equip12"]][9], creatures[deckList["name12"]][10] + equipment[deckList["equip12"]][10],
             0],
        13: [creatures[deckList["name13"]][0] + equipment[deckList["equip13"]][0], creatures[deckList["name13"]][1] + equipment[deckList["equip13"]][1], creatures[deckList["name13"]][2] + equipment[deckList["equip13"]][2], creatures[deckList["name13"]][3] + equipment[deckList["equip13"]][3], creatures[deckList["name13"]][4] + equipment[deckList["equip13"]][4],
             creatures[deckList["name13"]][5] + equipment[deckList["equip13"]][5], creatures[deckList["name13"]][6] + equipment[deckList["equip13"]][6], 
             creatures[deckList["name13"]][7] + equipment[deckList["equip13"]][7], creatures[deckList["name13"]][8] + equipment[deckList["equip13"]][8], creatures[deckList["name13"]][9] + equipment[deckList["equip13"]][9], creatures[deckList["name13"]][10] + equipment[deckList["equip13"]][10],
             0],
        14: [creatures[deckList["name14"]][0] + equipment[deckList["equip14"]][0], creatures[deckList["name14"]][1] + equipment[deckList["equip14"]][1], creatures[deckList["name14"]][2] + equipment[deckList["equip14"]][2], creatures[deckList["name14"]][3] + equipment[deckList["equip14"]][3], creatures[deckList["name14"]][4] + equipment[deckList["equip14"]][4],
             creatures[deckList["name14"]][5] + equipment[deckList["equip14"]][5], creatures[deckList["name14"]][6] + equipment[deckList["equip14"]][6], 
             creatures[deckList["name14"]][7] + equipment[deckList["equip14"]][7], creatures[deckList["name14"]][8] + equipment[deckList["equip14"]][8], creatures[deckList["name14"]][9] + equipment[deckList["equip14"]][9], creatures[deckList["name14"]][10] + equipment[deckList["equip14"]][10],
             0],
        15: [creatures[deckList["name15"]][0] + equipment[deckList["equip15"]][0], creatures[deckList["name15"]][1] + equipment[deckList["equip15"]][1], creatures[deckList["name15"]][2] + equipment[deckList["equip15"]][2], creatures[deckList["name15"]][3] + equipment[deckList["equip15"]][3], creatures[deckList["name15"]][4] + equipment[deckList["equip15"]][4],
             creatures[deckList["name15"]][5] + equipment[deckList["equip15"]][5], creatures[deckList["name15"]][6] + equipment[deckList["equip15"]][6], 
             creatures[deckList["name15"]][7] + equipment[deckList["equip15"]][7], creatures[deckList["name15"]][8] + equipment[deckList["equip15"]][8], creatures[deckList["name15"]][9] + equipment[deckList["equip15"]][9], creatures[deckList["name15"]][10] + equipment[deckList["equip15"]][10],
             0]
        }

#the stats of the units in the enemy's deck
encStats = {
        #damage, health, movement, attacks, range, cost, upkeep, taunt, heal, berserk, splash, taunted
        16: [creatures[encList["name1"]][0] + equipment[encList["equip1"]][0], creatures[encList["name1"]][1] + equipment[encList["equip1"]][1], creatures[encList["name1"]][2] + equipment[encList["equip1"]][2], creatures[encList["name1"]][3] + equipment[encList["equip1"]][3], creatures[encList["name1"]][4] + equipment[encList["equip1"]][4],
            creatures[encList["name1"]][5] + equipment[encList["equip1"]][5], creatures[encList["name1"]][6] + equipment[encList["equip1"]][6],
            creatures[encList["name1"]][7] + equipment[encList["equip1"]][7], creatures[encList["name1"]][8] + equipment[encList["equip1"]][8], creatures[encList["name1"]][9] + equipment[encList["equip1"]][9], creatures[encList["name1"]][10] + equipment[encList["equip1"]][10],
            0],
        17: [creatures[encList["name2"]][0] + equipment[encList["equip2"]][0], creatures[encList["name2"]][1] + equipment[encList["equip2"]][1], creatures[encList["name2"]][2] + equipment[encList["equip2"]][2], creatures[encList["name2"]][3] + equipment[encList["equip2"]][3], creatures[encList["name2"]][4] + equipment[encList["equip2"]][4],
            creatures[encList["name2"]][5] + equipment[encList["equip2"]][5], creatures[encList["name2"]][6] + equipment[encList["equip2"]][6], 
            creatures[encList["name2"]][7] + equipment[encList["equip2"]][7], creatures[encList["name2"]][8] + equipment[encList["equip2"]][8], creatures[encList["name2"]][9] + equipment[encList["equip2"]][9], creatures[encList["name2"]][10] + equipment[encList["equip2"]][10],
            0],
        18: [creatures[encList["name3"]][0] + equipment[encList["equip3"]][0], creatures[encList["name3"]][1] + equipment[encList["equip3"]][1], creatures[encList["name3"]][2] + equipment[encList["equip3"]][2], creatures[encList["name3"]][3] + equipment[encList["equip3"]][3], creatures[encList["name3"]][4] + equipment[encList["equip3"]][4],
            creatures[encList["name3"]][5] + equipment[encList["equip3"]][5], creatures[encList["name3"]][6] + equipment[encList["equip3"]][6], 
            creatures[encList["name3"]][7] + equipment[encList["equip3"]][7], creatures[encList["name3"]][8] + equipment[encList["equip3"]][8], creatures[encList["name3"]][9] + equipment[encList["equip3"]][9], creatures[encList["name3"]][10] + equipment[encList["equip3"]][10],
            0],
        19: [creatures[encList["name4"]][0] + equipment[encList["equip4"]][0], creatures[encList["name4"]][1] + equipment[encList["equip4"]][1], creatures[encList["name4"]][2] + equipment[encList["equip4"]][2], creatures[encList["name4"]][3] + equipment[encList["equip4"]][3], creatures[encList["name4"]][4] + equipment[encList["equip4"]][4],
            creatures[encList["name4"]][5] + equipment[encList["equip4"]][5], creatures[encList["name4"]][6] + equipment[encList["equip4"]][6], 
            creatures[encList["name4"]][7] + equipment[encList["equip4"]][7], creatures[encList["name4"]][8] + equipment[encList["equip4"]][8], creatures[encList["name4"]][9] + equipment[encList["equip4"]][9], creatures[encList["name4"]][10] + equipment[encList["equip4"]][10],
            0],
        20: [creatures[encList["name5"]][0] + equipment[encList["equip5"]][0], creatures[encList["name5"]][1] + equipment[encList["equip5"]][1], creatures[encList["name5"]][2] + equipment[encList["equip5"]][2], creatures[encList["name5"]][3] + equipment[encList["equip5"]][3], creatures[encList["name5"]][4] + equipment[encList["equip5"]][4],
            creatures[encList["name5"]][5] + equipment[encList["equip5"]][5], creatures[encList["name5"]][6] + equipment[encList["equip5"]][6], 
            creatures[encList["name5"]][7] + equipment[encList["equip5"]][7], creatures[encList["name5"]][8] + equipment[encList["equip5"]][8], creatures[encList["name5"]][9] + equipment[encList["equip5"]][9], creatures[encList["name5"]][10] + equipment[encList["equip5"]][10],
            0],
        21: [creatures[encList["name6"]][0] + equipment[encList["equip6"]][0], creatures[encList["name6"]][1] + equipment[encList["equip6"]][1], creatures[encList["name6"]][2] + equipment[encList["equip6"]][2], creatures[encList["name6"]][3] + equipment[encList["equip6"]][3], creatures[encList["name6"]][4] + equipment[encList["equip6"]][4], 
            creatures[encList["name6"]][5] + equipment[encList["equip6"]][5], creatures[encList["name6"]][6] + equipment[encList["equip6"]][6], 
            creatures[encList["name6"]][7] + equipment[encList["equip6"]][7], creatures[encList["name6"]][8] + equipment[encList["equip6"]][8], creatures[encList["name6"]][9] + equipment[encList["equip6"]][9], creatures[encList["name6"]][10] + equipment[encList["equip6"]][10],
            0],
        22: [creatures[encList["name7"]][0] + equipment[encList["equip7"]][0], creatures[encList["name7"]][1] + equipment[encList["equip7"]][1], creatures[encList["name7"]][2] + equipment[encList["equip7"]][2], creatures[encList["name7"]][3] + equipment[encList["equip7"]][3], creatures[encList["name7"]][4] + equipment[encList["equip7"]][4], 
            creatures[encList["name7"]][5] + equipment[encList["equip7"]][5], creatures[encList["name7"]][6] + equipment[encList["equip7"]][6], 
            creatures[encList["name7"]][7] + equipment[encList["equip7"]][7], creatures[encList["name7"]][8] + equipment[encList["equip7"]][8], creatures[encList["name7"]][9] + equipment[encList["equip7"]][9], creatures[encList["name7"]][10] + equipment[encList["equip7"]][10],
            0],
        23: [creatures[encList["name8"]][0] + equipment[encList["equip8"]][0], creatures[encList["name8"]][1] + equipment[encList["equip8"]][1], creatures[encList["name8"]][2] + equipment[encList["equip8"]][2], creatures[encList["name8"]][3] + equipment[encList["equip8"]][3], creatures[encList["name8"]][4] + equipment[encList["equip8"]][4],
            creatures[encList["name8"]][5] + equipment[encList["equip8"]][5], creatures[encList["name8"]][6] + equipment[encList["equip8"]][6], 
            creatures[encList["name8"]][7] + equipment[encList["equip8"]][7], creatures[encList["name8"]][8] + equipment[encList["equip8"]][8], creatures[encList["name8"]][9] + equipment[encList["equip8"]][9], creatures[encList["name8"]][10] + equipment[encList["equip8"]][10],
            0],
        24: [creatures[encList["name9"]][0] + equipment[encList["equip9"]][0], creatures[encList["name9"]][1] + equipment[encList["equip9"]][1], creatures[encList["name9"]][2] + equipment[encList["equip9"]][2], creatures[encList["name9"]][3] + equipment[encList["equip9"]][3], creatures[encList["name9"]][4] + equipment[encList["equip9"]][4],
            creatures[encList["name9"]][5] + equipment[encList["equip9"]][5], creatures[encList["name9"]][6] + equipment[encList["equip9"]][6], 
            creatures[encList["name9"]][7] + equipment[encList["equip9"]][7], creatures[encList["name9"]][8] + equipment[encList["equip9"]][8], creatures[encList["name9"]][9] + equipment[encList["equip9"]][9], creatures[encList["name9"]][10] + equipment[encList["equip9"]][10],
            0],
        25: [creatures[encList["name10"]][0] + equipment[encList["equip10"]][0], creatures[encList["name10"]][1] + equipment[encList["equip10"]][1], creatures[encList["name10"]][2] + equipment[encList["equip10"]][2], creatures[encList["name10"]][3] + equipment[encList["equip10"]][3], creatures[encList["name10"]][4] + equipment[encList["equip10"]][4], 
             creatures[encList["name10"]][5] + equipment[encList["equip10"]][5], creatures[encList["name10"]][6] + equipment[encList["equip10"]][6], 
             creatures[encList["name10"]][7] + equipment[encList["equip10"]][7], creatures[encList["name10"]][8] + equipment[encList["equip10"]][8], creatures[encList["name10"]][9] + equipment[encList["equip10"]][9], creatures[encList["name10"]][10] + equipment[encList["equip10"]][10],
             0],
        26: [creatures[encList["name11"]][0] + equipment[encList["equip11"]][0], creatures[encList["name11"]][1] + equipment[encList["equip11"]][1], creatures[encList["name11"]][2] + equipment[encList["equip11"]][2], creatures[encList["name11"]][3] + equipment[encList["equip11"]][3], creatures[encList["name11"]][4] + equipment[encList["equip11"]][4],
             creatures[encList["name11"]][5] + equipment[encList["equip11"]][5], creatures[encList["name11"]][6] + equipment[encList["equip11"]][6], 
             creatures[encList["name11"]][7] + equipment[encList["equip11"]][7], creatures[encList["name11"]][8] + equipment[encList["equip11"]][8], creatures[encList["name11"]][9] + equipment[encList["equip11"]][9], creatures[encList["name11"]][10] + equipment[encList["equip11"]][10],
             0],
        27: [creatures[encList["name12"]][0] + equipment[encList["equip12"]][0], creatures[encList["name12"]][1] + equipment[encList["equip12"]][1], creatures[encList["name12"]][2] + equipment[encList["equip12"]][2], creatures[encList["name12"]][3] + equipment[encList["equip12"]][3], creatures[encList["name12"]][4] + equipment[encList["equip12"]][4],
             creatures[encList["name12"]][5] + equipment[encList["equip12"]][5], creatures[encList["name12"]][6] + equipment[encList["equip12"]][6], 
             creatures[encList["name12"]][7] + equipment[encList["equip12"]][7], creatures[encList["name12"]][8] + equipment[encList["equip12"]][8], creatures[encList["name12"]][9] + equipment[encList["equip12"]][9], creatures[encList["name12"]][10] + equipment[encList["equip12"]][10],
             0],
        28: [creatures[encList["name13"]][0] + equipment[encList["equip13"]][0], creatures[encList["name13"]][1] + equipment[encList["equip13"]][1], creatures[encList["name13"]][2] + equipment[encList["equip13"]][2], creatures[encList["name13"]][3] + equipment[encList["equip13"]][3], creatures[encList["name13"]][4] + equipment[encList["equip13"]][4],
             creatures[encList["name13"]][5] + equipment[encList["equip13"]][5], creatures[encList["name13"]][6] + equipment[encList["equip13"]][6], 
             creatures[encList["name13"]][7] + equipment[encList["equip13"]][7], creatures[encList["name13"]][8] + equipment[encList["equip13"]][8], creatures[encList["name13"]][9] + equipment[encList["equip13"]][9], creatures[encList["name13"]][10] + equipment[encList["equip13"]][10],
             0],
        29: [creatures[encList["name14"]][0] + equipment[encList["equip14"]][0], creatures[encList["name14"]][1] + equipment[encList["equip14"]][1], creatures[encList["name14"]][2] + equipment[encList["equip14"]][2], creatures[encList["name14"]][3] + equipment[encList["equip14"]][3], creatures[encList["name14"]][4] + equipment[encList["equip14"]][4],
             creatures[encList["name14"]][5] + equipment[encList["equip14"]][5], creatures[encList["name14"]][6] + equipment[encList["equip14"]][6], 
             creatures[encList["name14"]][7] + equipment[encList["equip14"]][7], creatures[encList["name14"]][8] + equipment[encList["equip14"]][8], creatures[encList["name14"]][9] + equipment[encList["equip14"]][9], creatures[encList["name14"]][10] + equipment[encList["equip14"]][10],
             0],
        30: [creatures[encList["name15"]][0] + equipment[encList["equip15"]][0], creatures[encList["name15"]][1] + equipment[encList["equip15"]][1], creatures[encList["name15"]][2] + equipment[encList["equip15"]][2], creatures[encList["name15"]][3] + equipment[encList["equip15"]][3], creatures[encList["name15"]][4] + equipment[encList["equip15"]][4],
             creatures[encList["name15"]][5] + equipment[encList["equip15"]][5], creatures[encList["name15"]][6] + equipment[encList["equip15"]][6], 
             creatures[encList["name15"]][7] + equipment[encList["equip15"]][7], creatures[encList["name15"]][8] + equipment[encList["equip15"]][8], creatures[encList["name15"]][9] + equipment[encList["equip15"]][9], creatures[encList["name15"]][10] + equipment[encList["equip15"]][10],
             0]
        }

#the instance of all units used in a battle
battleDict = copy.deepcopy(deckStats)
battleDict.update(copy.deepcopy(encStats))


#main function
def main():
    global combat
    global combatClicked
    global playerAp
    global enemyAp
    global playerUpkeep
    global enemyUpkeep
    global selectors
    global displayUnit
    
    # initialize the pygame module
    pygame.init()
    
    #initialize the font module
    pygame.font.init()
    
    #font
    font = pygame.font.Font(None, 60)
    
    #load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("1 Dollar Gobrin") 
    
    #create a surface on screen that has the size of 1920 x 1080
    screen = pygame.display.set_mode((1920,1080))
    
    #define a variable to control the main loop
    running = True
    
    #blits stuff to screen
    def blit(image, screen, x, y):
             screen.blit(image, [x, y])
             
    #updates visuals
    def update():
        global displayUnit
        if (playerTurn == True):
            deckCounter = font.render(f"Deck: {len(playerDeck)}", True, (0, 0, 0))
            apCounter = font.render(f"Command Points: {playerAp + playerUpkeep}", True, (0, 0, 0))
            apBreakdown = font.render(f"Available: {playerAp} In Use: {playerUpkeep}", True, (0, 0, 0))
        if (playerTurn == False):
            deckCounter = font.render(f"Deck: {len(enemyDeck)}", True, (0, 0, 0))
            apCounter = font.render(f"Command Points: {enemyAp + enemyUpkeep}", True, (0, 0, 0))
            apBreakdown = font.render(f"Available: {enemyAp} In Use: {enemyUpkeep}", True, (0, 0, 0))
        playerHpCounter = font.render(f"Hitpoints: {playerHp}", True, (0, 0, 0))
        enemyHpCounter = font.render(f"Enemy Hitpoints: {enemyHp}", True, (0, 0, 0))
        blit(background, screen, 0, 0)
        blit(field, screen, 425, 0)
        blit(hand, screen, 425, 840)
        blit(deckCounter, screen, 0, 50)
        blit(playerHpCounter, screen, 0, 150)
        blit(enemyHpCounter, screen, 0, 200)
        blit(apCounter, screen, 0, 300)
        blit(apBreakdown, screen, 0, 350)
        blit(combatButton, screen, 1670, 520)
        if displayUnit >= 1:
            #if displayUnit >= 16:
                #name = font.render(f"{encList[f'name{displayUnit - 15}']} with {encList[f'equip{displayUnit - 15}']}", True, (0, 0, 0))
            #else:
                #name = font.render(f"{deckList[f'name{displayUnit}']} with {deckList[f'equip{displayUnit']}", True, (0, 0, 0))
            dmg = font.render(f"Damage: {battleDict[displayUnit][0]}", True, (0, 0, 0))
            hp = font.render(f"Hitpoints: {battleDict[displayUnit][1]}", True, (0, 0, 0))
            movement = font.render(f"Speed: {battleDict[displayUnit][2]}", True, (0, 0, 0))
            shot = font.render(f"Range: {battleDict[displayUnit][4]}", True, (0, 0, 0))
            #blit(name, screen, 1505, 50)
            blit(hp, screen, 1505, 100)
            blit(movement, screen, 1505, 150)
            blit(dmg, screen, 1505, 200)
            blit(shot, screen, 1505, 250)
            abilities = 0
            if battleDict[displayUnit][3] >= 2:
                attacks = font.render(f"Multiattack {battleDict[displayUnit][3]}x", True, (0, 0, 0))
                blit(attacks, screen, 1505, abilities * 50 + 300)
                abilities = abilities + 1
            if battleDict[displayUnit][10] >= 1:
                attacks = font.render(f"Splash {battleDict[displayUnit][10]}", True, (0, 0, 0))
                blit(attacks, screen, 1505, abilities * 50 + 300)
                abilities = abilities + 1
            if battleDict[displayUnit][7] >= 1:
                taunt = font.render(f"Taunt {battleDict[displayUnit][7]} Turns", True, (0, 0, 0))
                blit(taunt, screen, 1505, abilities * 50 + 300)
                abilities = abilities + 1
            if battleDict[displayUnit][8] >= 1:
                taunt = font.render(f"Heal {battleDict[displayUnit][8]}", True, (0, 0, 0))
                blit(taunt, screen, 1505, abilities * 50 + 300)
                abilities = abilities + 1
            if battleDict[displayUnit][9] >= 1:
                berserk = font.render(f"Berserk +{battleDict[displayUnit][9]}/Turn", True, (0, 0, 0))
                blit(berserk, screen, 1505, abilities * 50 + 300)
                abilities = abilities + 1
            if battleDict[displayUnit][11] >= 1:
                taunted = font.render(f"TAUNTED {battleDict[displayUnit][11]} TURNS", True, (255, 0, 0))
                blit(taunted, screen, 1505, abilities * 50 + 300)
                abilities = abilities + 1
        if (playerTurn == True):
            for card in playerHand:
                dmg = font.render(f"{battleDict[card][0]}", True, (255, 0, 0))
                hp = font.render(f"{battleDict[card][1]}", True, (0, 255, 0))
                blit(artDict[card][0], screen, 150 * playerHand.index(card) + 445, 906)
                blit(artDict[card][1], screen, 150 * playerHand.index(card) + 445, 906)
                blit(dmg, screen, 150 * playerHand.index(card) + 445 + 10, 906 - 30)
                blit(hp, screen, 150 * playerHand.index(card) + 445 + 80, 906 - 30)
        if (playerTurn == False):
            for card in enemyHand:
                dmg = font.render(f"{battleDict[card][0]}", True, (255, 0, 0))
                hp = font.render(f"{battleDict[card][1]}", True, (0, 255, 0))
                blit(artDict[card][0], screen, 150 * enemyHand.index(card) + 445, 906)
                blit(artDict[card][1], screen, 150 * enemyHand.index(card) + 445, 906)
                blit(dmg, screen, 150 * enemyHand.index(card) + 445 + 10, 906 - 30)
                blit(hp, screen, 150 * enemyHand.index(card) + 445 + 80, 906 - 30)
        for card in board:
            if(combat == True and PlayerTurn == True):
                board.reverse()
            if(card >= 1):
                dmg = font.render(f"{battleDict[card][0]}", True, (255, 0, 0))
                hp = font.render(f"{battleDict[card][1]}", True, (0, 255, 0))
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
            if(card <= -3):
                blit(selector, screen, 150 * (board.index(card) % 7) + 445, 220 * (board.index(card) // 7) + 20)
            if(combat == True and PlayerTurn == True):
                board.reverse()
        pygame.display.flip()
    
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
        if (playerTurn == True):
            board.reverse()
            for unit in board:
                if(unit >= 1 and unit <= 15):
                    active = unit
                    move = 0
                    newPosition = 0
                    attacks = battleDict[unit][3]
                    ranging = 1
                    attacking = True
                    while True:
                        if(attacks == 0 and move == battleDict[unit][2]):
                            break
                        elif(attacks == 0 and board[board.index(unit) - (move + 1)] != 0):
                            break
                        elif(ranging == battleDict[unit][4] + 1 and move == battleDict[unit][2]):
                            break
                        elif(ranging == battleDict[unit][4] + 1 and board[board.index(unit) - (move + 1)] != 0):
                            break
                        if (ranging == battleDict[unit][4] + 1 or attacks == 0) and (attacking == True):
                            attacking = False
                            ranging = 1
                        elif(attacks >= 1 and attacking == True):
                            target = board[board.index(unit) - (ranging + move)]
                            if (target == -2):
                                enemyHp = enemyHp - battleDict[unit][0]
                                #check victory
                                attacks = attacks - 1
                            elif (target >= 16):
                                battleDict[target][1] = battleDict[target][1] - battleDict[unit][0]
                                battleDict[target][11] = battleDict[unit][7]
                                if battleDict[unit][10] >= 1:
                                    if board.index(target) + 1 <= 20 and board.index(target) + 1 >= 0:
                                        if board[board.index(target) + 1] >= 16:
                                            battleDict[board[board.index(target) + 1]][1] = battleDict[board[board.index(target) + 1]][1] - battleDict[unit][10]
                                            if battleDict[board[board.index(target) + 1]][1] <= 0:
                                                enemyUpkeep = enemyUpkeep - battleDict[board[board.index(target) + 1]][6]
                                                enemyAp = enemyAp + battleDict[board[board.index(target) + 1]][5]
                                                #remove dead unit here and now
                                                if(board.index(target + 1) % 7 == 0):
                                                    board[board.index(target + 1)] = -2
                                                else:
                                                    board[board.index(target + 1)] = 0
                                    if board.index(target) - 1 <= 20 and board.index(target) - 1 >= 0:
                                        if board[board.index(target) - 1] >= 16:
                                            battleDict[board[board.index(target) - 1]][1] = battleDict[board[board.index(target) - 1]][1] - battleDict[unit][10]
                                            if(battleDict[board[board.index(target) - 1]][1] <= 0):
                                                enemyUpkeep = enemyUpkeep - battleDict[board[board.index(target) - 1]][6]
                                                enemyAp = enemyAp + battleDict[board[board.index(target) - 1]][5]
                                                #remove dead unit here and now
                                                if(board.index(target - 1) % 7 == 0):
                                                    board[board.index(target - 1)] = -2
                                                else:
                                                    board[board.index(target - 1)] = 0
                                    if board.index(target) + 7 <= 20 and board.index(target) + 7 >= 0:
                                        if board[board.index(target) + 7] >= 16:
                                            battleDict[board[board.index(target) + 7]][1] = battleDict[board[board.index(target) + 7]][1] - battleDict[unit][10]
                                            if(battleDict[board[board.index(target) + 7]][1] <= 0):
                                                enemyUpkeep = enemyUpkeep - battleDict[board[board.index(target) + 7]][6]
                                                enemyAp = enemyAp + battleDict[board[board.index(target) + 7]][5]
                                                #remove dead unit here and now
                                                if(board.index(target + 7) % 7 == 0):
                                                    board[board.index(target + 7)] = -2
                                                else:
                                                    board[board.index(target + 7)] = 0
                                    if board.index(target) - 7 <= 20 and board.index(target) - 7 >= 0:
                                        if board[board.index(target) - 7] >= 16:
                                            battleDict[board[board.index(target) - 7]][1] = battleDict[board[board.index(target) - 7]][1] - battleDict[unit][10]
                                            if(battleDict[board[board.index(target) - 7]][1] <= 0):
                                                enemyUpkeep = enemyUpkeep - battleDict[board[board.index(target) - 7]][6]
                                                enemyAp = enemyAp + battleDict[board[board.index(target) - 7]][5]
                                                #remove dead unit here and now
                                                if(board.index(target - 7) % 7 == 0):
                                                    board[board.index(target - 7)] = -2
                                                else:
                                                    board[board.index(target - 7)] = 0
                                if(battleDict[target][1] <= 0):
                                    enemyUpkeep = enemyUpkeep - battleDict[target][6]
                                    enemyAp = enemyAp + battleDict[target][5]
                                    #remove dead unit here and now
                                    if(board.index(target) % 7 == 0):
                                        board[board.index(target)] = -2
                                    else:
                                        board[board.index(target)] = 0
                                attacks = attacks - 1
                            else:
                                ranging = ranging + 1
                        elif(move <= battleDict[unit][2] - 1 and attacking == False):
                            if(board[board.index(unit) - (move + 1)] == 0):
                                move = move + 1
                                attacking = True
                    battleDict[unit][0] = battleDict[unit][0] + battleDict[unit][9]
                    battleDict[unit][11] = battleDict[unit][11] - 1
                    if battleDict[unit][8] >= 1:
                        healthsMissing = []
                        healTargets = []
                        for target in board:
                            if target >= 1 and target <= 15:
                                healTargets.append(target)
                                healthsMissing.append(deckStats[target][1] - battleDict[target][1])
                        battleDict[healTargets[healthsMissing.index(max(healthsMissing))]][1] = min(battleDict[healTargets[healthsMissing.index(max(healthsMissing))]][1] + battleDict[unit][8], deckStats[healTargets[healthsMissing.index(max(healthsMissing))]][1])
                    newPosition = board.index(unit) - move
                    if(board.index(unit) % 7 == 6):
                        board[board.index(unit)] = -1
                    else:
                        board[board.index(unit)] = 0
                    board[newPosition] = unit
            board.reverse()
            if(playerAp + playerUpkeep <= 4):
                playerAp = playerAp + 1
            playerTurn = False
            drawCard(player == True)
        elif (playerTurn == False):
            for unit in board:
                if(unit >= 16):
                    active = unit
                    move = 0
                    newPosition = 0
                    attacks = battleDict[unit][3]
                    ranging = 1
                    attacking = True
                    while True:
                        if(attacks == 0 and move == battleDict[unit][2]):
                            break
                        elif(attacks == 0 and board[board.index(unit) - (move + 1)] != 0):
                            break
                        elif(ranging == battleDict[unit][4] + 1 and move == battleDict[unit][2]):
                            break
                        elif(ranging == battleDict[unit][4] + 1 and board[board.index(unit) - (move + 1)] != 0):
                            break
                        elif(ranging == battleDict[unit][4] + 1 or attacks == 0) and (attacking == True):
                            attacking = False
                            ranging = 1
                        elif(attacks >= 1 and attacking == True):
                            target = board[board.index(unit) - (ranging + move)]
                            if (target == -1):
                                playerHp = playerHp - battleDict[unit][0]
                                #check victory
                                attacks = attacks - 1
                            elif (target >= 1 and target <= 15):
                                battleDict[target][1] = battleDict[target][1] - battleDict[unit][0]
                                battleDict[target][11] = battleDict[unit][7]
                                if battleDict[unit][10] >= 1:
                                    if board.index(target) + 1 <= 20 and board.index(target) + 1 >= 0:
                                        if board[board.index(target) + 1] >= 1 and board[board.index(target) + 1] <= 15:
                                            battleDict[board[board.index(target) + 1]][1] = battleDict[board[board.index(target) + 1]][1] - battleDict[unit][10]
                                            if battleDict[board[board.index(target) + 1]][1] <= 0:
                                                playerUpkeep = playerUpkeep - battleDict[board[board.index(target) + 1]][6]
                                                playerAp = playerAp + battleDict[board[board.index(target) + 1]][5]
                                                #remove dead unit here and now
                                                if(board.index(target + 1) % 7 == 0):
                                                    board[board.index(target + 1)] = -1
                                                else:
                                                    board[board.index(target + 1)] = 0
                                    if board.index(target) - 1 <= 20 and board.index(target) - 1 >= 0:
                                        if board[board.index(target) - 1] >= 1 and board[board.index(target) - 1] <= 15:
                                            battleDict[board[board.index(target) - 1]][1] = battleDict[board[board.index(target) - 1]][1] - battleDict[unit][10]
                                            if(battleDict[board[board.index(target) - 1]][1] <= 0):
                                                playerUpkeep = playerUpkeep - battleDict[board[board.index(target) - 1]][6]
                                                playerAp = playerAp + battleDict[board[board.index(target) - 1]][5]
                                                #remove dead unit here and now
                                                if(board.index(target - 1) % 7 == 0):
                                                    board[board.index(target - 1)] = -1
                                                else:
                                                    board[board.index(target - 1)] = 0
                                    if board.index(target) + 7 <= 20 and board.index(target) + 7 >= 0:
                                        if board[board.index(target) + 7] >= 1 and board[board.index(target) + 7] <= 15:
                                            battleDict[board[board.index(target) + 7]][1] = battleDict[board[board.index(target) + 7]][1] - battleDict[unit][10]
                                            if(battleDict[board[board.index(target) + 7]][1] <= 0):
                                                playerUpkeep = playerUpkeep - battleDict[board[board.index(target) + 7]][6]
                                                playerAp = playerAp + battleDict[board[board.index(target) + 7]][5]
                                                #remove dead unit here and now
                                                if(board.index(target + 7) % 7 == 0):
                                                    board[board.index(target + 7)] = -1
                                                else:
                                                    board[board.index(target + 7)] = 0
                                    if board.index(target) - 7 <= 20 and board.index(target) - 7 >= 0:
                                        if board[board.index(target) - 7] >= 1 and board[board.index(target) - 7] <= 15:
                                            battleDict[board[board.index(target) - 7]][1] = battleDict[board[board.index(target) - 7]][1] - battleDict[unit][10]
                                            if(battleDict[board[board.index(target) - 7]][1] <= 0):
                                                playerUpkeep = playerUpkeep - battleDict[board[board.index(target) - 7]][6]
                                                playerAp = playerAp + battleDict[board[board.index(target) - 7]][5]
                                                #remove dead unit here and now
                                                if(board.index(target - 7) % 7 == 0):
                                                    board[board.index(target - 7)] = -1
                                                else:
                                                    board[board.index(target - 7)] = 0
                                if(battleDict[target][1] <= 0):
                                    playerUpkeep = playerUpkeep - battleDict[target][6]
                                    playerAp = playerAp + battleDict[target][5]
                                    #remove dead unit here and now
                                    if(board.index(target) % 7 == 0):
                                        board[board.index(target)] = -1
                                    else:
                                        board[board.index(target)] = 0
                                attacks = attacks - 1
                            else:
                                ranging = ranging + 1
                        elif(move <= battleDict[unit][2] - 1 and attacking == False):
                            if(board[board.index(unit) - (move + 1)] == 0):
                                move = move + 1
                                attacking = True
                    battleDict[unit][0] = battleDict[unit][0] + battleDict[unit][9]
                    battleDict[unit][11] = battleDict[unit][11] - 1
                    if battleDict[unit][8] >= 1:
                        healthsMissing = []
                        healTargets = []
                        for target in board:
                            if target >= 16:
                                healTargets.append(target)
                                healthsMissing.append(encStats[target][1] - battleDict[target][1])
                        battleDict[healTargets[healthsMissing.index(max(healthsMissing))]][1] = min(battleDict[healTargets[healthsMissing.index(max(healthsMissing))]][1] + battleDict[unit][8], encStats[healTargets[healthsMissing.index(max(healthsMissing))]][1])
                    newPosition = board.index(unit) - move
                    if(board.index(unit) % 7 == 6):
                        board[board.index(unit)] = -2
                    else:
                        board[board.index(unit)] = 0
                    board[newPosition] = unit
            if(enemyAp + enemyUpkeep <= 4):
                enemyAp = enemyAp + 1
            playerTurn = True
            drawCard(player == False)
        active = 0
        combat = False
    
    #removes selector locations from board
    def removeSelectors():
        global selectors
        for space in board:
            if(space <= -3):
                if(board.index(space) % 7 == 0):
                    board[board.index(space)] = -1
                elif(board.index(space) % 7 == 6):
                    board[board.index(space)] = -2
                else:
                    board[board.index(space)] = 0
        selectors = 0
    
    #draw cards
    drawCard(player == True)
    drawCard(player == False)
    drawCard(player == True)
    drawCard(player == False)
    drawCard(player == True)
    drawCard(player == False)
    drawCard(player == True)
    drawCard(player == False)
    
    # main loop
    while running:
        xpos, ypos = mouse[0]
        if(combatClicked == True and mouse[1] == 0):
            combatClicked = False
            combat = True
            runCombat()
        elif(xpos >= 1670 and xpos <= 1750):
            if(ypos >= 520 and ypos <= 560):
                if(mouse[1] == 1):
                    combatClicked = True
        #player turn
        elif(playerTurn == True):
            if((ypos - 10) // 220 >= 0 and (ypos - 10) // 220 <= 2):
                if((xpos - 435) // 150 >= 0 and (xpos - 435) // 150 <= 6):
                    index = ((ypos - 10) // 220) * 7 + ((xpos - 435) // 150)
                    if(board[index] <= -3):
                        if(mouse[1] == 1):
                            if(select >= 1):
                                if(board.count(select) == 0):
                                    playerAp = playerAp - battleDict[select][5]
                                    playerUpkeep = playerUpkeep + battleDict[select][6]
                                    playerHand.remove(select)
                                else:
                                    if(board.index(select) % 7 == 0):
                                        board[board.index(select)] = -1
                                    elif(board.index(select) % 7 == 6):
                                        board[board.index(select)] = -2
                                    else:
                                        board[board.index(select)] = 0
                                board[index] = select
                                removeSelectors()
                                select = 0
                    elif(board[index] >= 1):
                        displayUnit = board[index]
                        if(mouse[1] == 1):
                            if(board[index] >= 1 and board[index] <= 15 and battleDict[board[index]][11] <= 0):
                                if(board[(index % 7) + 7] <= 15):
                                        removeSelectors()
                                        select = board[index]
                                        row = 0
                                        while True:
                                            if(row == 3):
                                                break
                                            if(board[(index % 7) + (7 * row)] <= 0):
                                                board[(index % 7) + (7 * row)] = - (3 + selectors)
                                                selectors = selectors + 1
                                            row = row + 1
                    else:
                        if(mouse[1] == 1):
                            removeSelectors()
            elif((xpos - 435) // 150 >= 0 and (xpos - 435) // 150 <= len(playerHand) - 1):
                if(ypos >= 850 and ypos <= 1070):
                    index = (xpos - 435) // 150
                    displayUnit = playerHand[index]
                    if(playerAp - battleDict[playerHand[index]][5] >= 0):
                        if(mouse[1] == 1):
                            removeSelectors()
                            select = playerHand[index]
                            row = 0
                            while True:
                                if(row == 3):
                                    break
                                if(board[7 * row] == -1):
                                    board[7 * row] = -1 * (3 + selectors)
                                    selectors = selectors + 1
                                row = row + 1
        #enemy turn
        elif(playerTurn == False):
            #AI decision making. Once reached decision execute orders and set combat to true
            if((ypos - 10) // 220 >= 0 and (ypos - 10) // 220 <= 2):
                if((xpos - 435) // 150 >= 0 and (xpos - 435) // 150 <= 6):
                    index = ((ypos - 10) // 220) * 7 + ((xpos - 435) // 150)
                    if(board[index] <= -3):
                        if(mouse[1] == 1):
                            if(select >= 1):
                                if(board.count(select) == 0):
                                    enemyAp = enemyAp - battleDict[select][5]
                                    enemyUpkeep = enemyUpkeep + battleDict[select][6]
                                    enemyHand.remove(select)
                                else:
                                    if(board.index(select) % 7 == 0):
                                        board[board.index(select)] = -1
                                    elif(board.index(select) % 7 == 6):
                                        board[board.index(select)] = -2
                                    else:
                                        board[board.index(select)] = 0
                                board[index] = select
                                removeSelectors()
                                select = 0
                    elif(board[index] >= 1):
                        displayUnit = board[index]
                        if(mouse[1] == 1):
                            if(board[index] >= 16 and battleDict[board[index]][11] <= 0):
                                if(board[(index % 7) + 7] >= 16 or board[(index % 7) + 7] <= 0):
                                        removeSelectors()
                                        select = board[index]
                                        row = 0
                                        while True:
                                            if(row == 3):
                                                break
                                            if(board[(index % 7) + (7 * row)] <= 0):
                                                board[(index % 7) + (7 * row)] = - (3 + selectors)
                                                selectors = selectors + 1
                                            row = row + 1
                    else:
                        if(mouse[1] == 1):
                            removeSelectors()
            elif((xpos - 435) // 150 >= 0 and (xpos - 435) // 150 <= len(enemyHand) - 1):
                if(ypos >= 850 and ypos <= 1070):
                    index = (xpos - 435) // 150
                    displayUnit = enemyHand[index]
                    if(enemyAp - battleDict[enemyHand[index]][5] >= 0):
                        if(mouse[1] == 1):
                            removeSelectors()
                            select = enemyHand[index]
                            row = 0
                            while True:
                                if(row == 3):
                                    break
                                if(board[6 + (7 * row)] == -2):
                                    board[6 + (7 * row)] = -1 * (3 + selectors)
                                    selectors = selectors + 1
                                row = row + 1
            
        update()
        
        #if(mouse[1] == 1):
            #pygame.quit()
        #event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse[event.button] = 1
                mouse[0] = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse[event.button] = 0
                mouse[0] = event.pos
            elif event.type == pygame.MOUSEMOTION:
                mouse[0] = event.pos

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
