import pygame

pygame.init()
width = 390
height = 390

rectWidth = 100
rectHeight = 100
gameDisplay = pygame.display.set_mode((width ,height))
pygame.display.set_caption('Chess With Friends')

gameExit = False
boolRect = False

pygame.draw.rect(gameDisplay, (0, 255, 255), [xPos, yPos, rectWidth, rectHeight])


while not gameExit:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True




    pygame.display.update()
pygame.quit()
quit()
