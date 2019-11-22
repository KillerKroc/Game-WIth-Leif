import pygame

phase = "mainMenu"

startClicked = False
backClicked = False

mouse = [(0, 0), 0]

#main function
def main():
    global phase
    global startClicked
    global backClicked
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
    
    #create a surface on screen that has the size of 1920 x 1080
    screen = pygame.display.set_mode((800, 450))
    
    #define a variable to control the main loop
    running = True
    
    #main loop
    while running:
        if phase == "mainMenu":
            screen.fill((150, 150, 150))
            pygame.draw.rect(screen, (0, 0, 0), (300, 200, 200, 50))
            start = font.render("Start", True, (255, 255, 255))
            screen.blit(start, (300, 200))
            pygame.display.flip()
            if startClicked == True and mouse[1] == 0:
                phase = "worldMap"
                startClicked = False
            elif mouse[0][0] >= 300 and mouse[0][0] <= 500 and mouse[0][1] >= 200 and mouse[0][1] <= 250 and mouse[1] == 1:
                startClicked = True
        elif phase == "worldMap":
            screen.fill((50, 100, 50))
            pygame.draw.rect(screen, (255, 0, 255), (30, 380, 70, 70))
            pygame.draw.rect(screen, (255, 255, 0), (130, 380, 70, 70))
            pygame.draw.rect(screen, (0, 255, 255), (230, 380, 70, 70))
            pygame.draw.rect(screen, (0, 0, 0), (700, 0, 50, 50))
            pygame.draw.rect(screen, (255, 0, 0), (750, 0, 50, 50))
            pygame.display.flip()
            if backClicked == True and mouse[1] == 0:
                phase = "mainMenu"
                backClicked = False
            elif mouse[0][0] >= 750 and mouse[0][0] <= 800 and mouse[0][1] >= 0 and mouse[0][1] <= 50 and mouse[1] == 1:
                backClicked = True
        #elif phase == "provinceMap":
            
        #elif phase == "settings":
            
        #elif phase == "army":
            
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