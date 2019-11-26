import pygame

phase = "mainMenu"
prevPhase = "mainMenu"
screenWidth = 1280
screenHeight = 720
button1 = pygame.image.load("button1.png")

mouse = [(0, 0), 0]

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

#main function
def main():
    global phase
    global prevPhase
    global screenWidth
    global screenHeight
    
    startClicked = False
    backClicked = False
    settingsClicked = False
    armyClicked = False
    
    # initialize the pygame module
    pygame.init()
    
    #initialize the font module
    pygame.font.init()
    
    #font
    font = pygame.font.Font(None, 50)
    
    #load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("1 Dollar Gobrin")
    
    #create a surface on screen
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    
    #define a variable to control the main loop
    running = True
    
    #main loop
    while running:
        
        if phase == "mainMenu":
            screen.fill((150, 150, 150))
            pygame.draw.rect(screen, (0, 0, 0), (0, screenHeight * 8 / 10, screenWidth / 5, screenHeight / 10))
            start = font.render("Start", True, (255, 255, 255))
            screen.blit(start, (0, screenHeight * 4 / 5))
            pygame.display.flip()
            if mouse[0][0] > 0 and mouse[0][0] < screenWidth / 5 and mouse[0][1] > screenHeight * 4 / 5 and mouse[0][1] < screenHeight * 9 / 10 and mouse[1] == 1:
                startClicked = True
            elif startClicked == True and mouse[1] == 0:
                phase = "worldMap"
                startClicked = False
        
        elif phase == "worldMap":
            screen.fill((50, 100, 50))
            screen.blit(button1, (0, screenHeight * 8 / 10))
            pygame.draw.rect(screen, (255, 255, 0), (0, screenHeight * 6.5 / 10, screenWidth / 5, screenHeight / 10))
            pygame.draw.rect(screen, (0, 255, 255), (0, screenHeight * 5 / 10, screenWidth / 5, screenHeight / 10))
            pygame.draw.rect(screen, (0, 0, 0), (screenWidth - (screenHeight / 5), 0, screenHeight / 10, screenHeight / 10))
            pygame.draw.rect(screen, (255, 0, 0), (screenWidth - (screenHeight / 10), 0, screenHeight / 10, screenHeight / 10))
            pygame.display.flip()
            if mouse[0][0] > screenWidth - (screenHeight / 10) and mouse[0][0] < screenWidth and mouse[0][1] > 0 and mouse[0][1] < screenHeight / 10 and mouse[1] == 1:
                backClicked = True
            elif mouse[0][0] > screenWidth - (screenHeight / 5) and mouse[0][0] < screenWidth - (screenHeight / 10) and mouse[0][1] > 0 and mouse[0][1] <= screenHeight / 10 and mouse[1] == 1:
                settingsClicked = True
            elif mouse[0][0] > 0 and mouse[0][0] < screenWidth / 5 and mouse[0][1] > screenHeight * 5 / 10 and mouse[0][1] <= screenHeight * 6 / 10 and mouse[1] == 1:
                armyClicked = True
            elif backClicked == True and mouse[1] == 0:
                phase = "mainMenu"
                backClicked = False
            elif settingsClicked == True and mouse[1] == 0:
                phase = "settings"
                prevPhase = "worldMap"
                settingsClicked = False
            elif armyClicked == True and mouse[1] == 0:
                phase = "army"
                armyClicked = False
                
        #elif phase == "provinceMap":
            
        elif phase == "settings":
            pygame.draw.rect(screen, (150, 150, 150), (screenWidth / 5, screenHeight / 5, screenWidth * 3 / 5, screenHeight * 3 / 5))
            pygame.draw.rect(screen, (255, 0, 0), (screenWidth * 4 / 5 - (screenHeight / 10), screenHeight / 5, screenHeight / 10, screenHeight /10))
            pygame.display.flip()
            if mouse[0][0] > screenWidth * 4 / 5 - (screenHeight / 10) and mouse[0][0] < screenWidth * 4 / 5 and mouse[0][1] > screenHeight / 5 and mouse[0][1] < screenHeight * 3 / 10 and mouse[1] == 1:
                backClicked = True
            elif backClicked == True and mouse[1] == 0:
                phase = prevPhase
                backClicked = False
        elif phase == "army":
            screen.fill((207, 185, 151))
            pygame.draw.rect(screen, (255, 255, 255), (screenHeight / 10, screenHeight / 10, screenHeight * 1.5 / 5, screenHeight * 2.5 / 10))
            pygame.draw.rect(screen, (255, 255, 255), (screenHeight / 10, screenHeight * 4 / 10, screenHeight * 1.5 / 10, screenHeight / 5))
            pygame.draw.rect(screen, (255, 255, 255), (screenHeight / 10, screenHeight * 7 / 10, screenHeight * 1.5 / 10, screenHeight / 5))
            pygame.display.flip()
            
            
        #elif phase == "unit":
            
        #elif phase == "hero":
        
        #elif phase == "spells"
            
        #elif phase == "voidForge":
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse[event.button] = 1
                mouse[0] = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse[event.button] = 0
                mouse[0] = event.pos
            elif event.type == pygame.MOUSEMOTION:
                mouse[0] = event.pos

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()