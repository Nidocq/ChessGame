import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800 ,400))
pygame.display.set_caption('Chess With Friends')


edge = 45
tile = 39.3

gameExit = False
boolRect = False

def makeShadow():
    #rect = pygame.draw.rect(gameDisplay, (255, 0, 0), [44.5, 44.5, edge, edge])
    s = pygame.Surface((39.9, 39.9))
    s.set_alpha(120)
    gameDisplay.blit(s, (44.5, 44.5))


def PawnW(x, y):
    W_Pawn = pygame.image.load('Pictures/W_Pawn.png')
    gameDisplay.blit(W_Pawn,(edge+tile*x, edge+tile*y))

def PawnB(x, y): # Read the input of this function and display it on the board
    B_Pawn = pygame.image.load('Pictures/B_Pawn.png')
    gameDisplay.blit(B_Pawn,(edge+tile*x, edge+tile*y))

def RookW(x, y):
    W_Rook = pygame.image.load('Pictures/W_Rook.png')
    gameDisplay.blit(W_Rook,(edge+tile*x, edge+tile*y))

def RookB(x, y):
    B_Rook = pygame.image.load('Pictures/B_Rook.png')
    gameDisplay.blit(B_Rook,(edge+tile*x, edge+tile*y))

def KnightW(x, y):
    W_Knight = pygame.image.load('Pictures/W_Knight.png')
    gameDisplay.blit(W_Knight,(edge+tile*x, edge+tile*y))

def KnightB(x, y):
    B_Knight = pygame.image.load('Pictures/B_Knight.png')
    gameDisplay.blit(B_Knight,(edge+tile*x, edge+tile*y))

def BishopW(x, y):
    W_Bishop = pygame.image.load('Pictures/W_Bishop.png')
    gameDisplay.blit(W_Bishop,(edge+tile*x, edge+tile*y))

def BishopB(x, y):
    B_Bishop = pygame.image.load('Pictures/B_Bishop.png')
    gameDisplay.blit(B_Bishop,(edge+tile*x, edge+tile*y))

def QueenW(x, y):
    W_Queen = pygame.image.load('Pictures/W_Queen.png')
    gameDisplay.blit(W_Queen,(edge+tile*x, edge+tile*y))

def QueenB(x, y):
    B_Queen = pygame.image.load('Pictures/B_Queen.png')
    gameDisplay.blit(B_Queen,(edge+tile*x, edge+tile*y))

def KingW(x, y):
    W_King = pygame.image.load('Pictures/W_King.png')
    gameDisplay.blit(W_King,(edge+tile*x, edge+tile*y))

def KingB(x, y):
    B_King = pygame.image.load('Pictures/B_King.png')
    gameDisplay.blit(B_King,(edge+tile*x, edge+tile*y))


boardImage = pygame.image.load('Pictures/Board.png')


# gameDisplay.blit(W_Pawn,(edge, edge+tile*6))
# gameDisplay.blit(W_Pawn,(edge+tile, edge+tile*6))
# gameDisplay.blit(W_Pawn,(edge+tile*2, edge+tile*6))
# gameDisplay.blit(W_Pawn,(edge+tile*3, edge+tile*6))
# gameDisplay.blit(W_Pawn,(edge+tile*4, edge+tile*6))
# gameDisplay.blit(W_Pawn,(edge+tile*5, edge+tile*6))
# gameDisplay.blit(W_Pawn,(edge+tile*6, edge+tile*6))
# gameDisplay.blit(W_Pawn,(edge+tile*7, edge+tile*6))
#
# gameDisplay.blit(B_Pawn,(edge, edge+tile))
# gameDisplay.blit(B_Pawn,(edge+tile, edge+tile))
# gameDisplay.blit(B_Pawn,(edge+tile*2, edge+tile))
# gameDisplay.blit(B_Pawn,(edge+tile*3, edge+tile))
# gameDisplay.blit(B_Pawn,(edge+tile*4, edge+tile))
# gameDisplay.blit(B_Pawn,(edge+tile*5, edge+tile))
# gameDisplay.blit(B_Pawn,(edge+tile*6, edge+tile))
# gameDisplay.blit(B_Pawn,(edge+tile*7, edge+tile))
#
# gameDisplay.blit(W_Rook,(edge, edge+tile*7))
# gameDisplay.blit(W_Rook,(edge+tile*7, edge+tile*7))
# gameDisplay.blit(B_Rook,(edge, edge))
# gameDisplay.blit(B_Rook,(edge+tile*7, edge))
# gameDisplay.blit(W_Knight,(edge+tile*1, edge+tile*7))
# gameDisplay.blit(W_Knight,(edge+tile*6, edge+tile*7))
# gameDisplay.blit(B_Knight,(edge+tile, edge))
# gameDisplay.blit(B_Knight,(edge+tile*6, edge))
# gameDisplay.blit(W_Bishop,(edge+tile*5, edge+tile*7))
# gameDisplay.blit(W_Bishop,(edge+tile*2, edge+tile*7))
# gameDisplay.blit(B_Bishop,(edge+tile*5, edge))
# gameDisplay.blit(B_Bishop,(edge+tile*2, edge))
# gameDisplay.blit(W_Queen,(edge+tile*3, edge+tile*7))
# gameDisplay.blit(B_Queen,(edge+tile*4, edge))
# gameDisplay.blit(W_King,(edge+tile*4, edge+tile*7))
# gameDisplay.blit(B_King,(edge+tile*3, edge))


while not gameExit:

    gameDisplay.fill((255,255,255))
    Board = gameDisplay.blit(boardImage, (0,0))
    PawnB(0,1)
    PawnB(1,1)
    PawnB(2,1)
    PawnB(3,1)
    PawnB(4,1)
    PawnB(5,1)
    PawnB(6,1)
    PawnB(7,1)
    PawnW(0,6)
    PawnW(1,6)
    PawnW(2,6)
    PawnW(3,6)
    PawnW(4,6)
    PawnW(5,6)
    PawnW(6,6)
    PawnW(7,6)
    RookB(0,0)
    RookB(7,0)
    RookW(0,7)
    RookW(7,7)
    KnightB(1,0)
    KnightB(6,0)
    KnightW(1,7)
    KnightW(6,7)
    BishopB(2,0)
    BishopB(5,0)
    BishopW(2,7)
    BishopW(5,7)
    QueenB(3,0)
    QueenW(3,7)
    KingB(4,0)
    KingW(4,7)
    #Define chess pieces for the pictures

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True

        if event.type == pygame.MOUSEBUTTONUP:
            boolRect = True



    if boolRect == True:
        makeShadow()
            # largeText = pygame.font.SysFont("comicsansms",115)
            # TextSurf, TextRect = pygame.text_objects("Paused", largeText)
            # TextRect.center = ((display_width/2),(display_height/2))
            # gameDisplay.blit(TextSurf, TextRect)


    pygame.display.update()
pygame.quit()
quit()

if __name__ == '__main__':
    print("Exec main.py")
    execfile('Engine.py')
