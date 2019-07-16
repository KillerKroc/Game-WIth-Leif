import pygame
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

playerHP = 10
AP = 0
enemyHP = 10
playerTurn = True
combat = False
#Creates an array to represent the playinb board
board = ['(', 0, 0, 0, 0, 0, ')',
         '(', 0, 0, 0, 0, 0, ')',
         '(', 0, 0, 0, 0, 0, ')']
#blits board to screen
def blit_board(board, screen):
         screen.blit(field, [0, 0])
         pygame.display.flip()
#initialize pygame
pygame.init()     
# define a main function
def main():
    #load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
     
    # create a surface on screen that has the size of 240 x 180
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
        if (playerTurn == True):
            #play
            if (combat == False):
                #player actions
                if(#start combat button is pushed):
                    combat = True
            #combat
            if (combat == True):
                #combat process
                if (#combat is complete):
                    combat = False
                    playerTurn = False
                    
        #enemy turn
        if (playerTurn == False):
            #enemy play
            if (combat == False):
                #AI decision making. Once reached decision execute orders and set combat to true
            #enemy combat
            if (combat == True):
                #enemy combat process
                if (#combat is complete):
                    combat = False
                    playerTurn = True
        #victory
        if (enemyHP <= 0):
            #win
        #failure
        if (playerHP <= 0):
            #lose
        
        
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
    pygame.quit()
