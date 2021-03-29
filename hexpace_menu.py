import pygame
import os

pygame.init()

################# VARIABLES #################
# colors
GREY = (155,155,155)
BLUE = (0,90,130)
# display
WIDTH = 1024
HEIGHT = 576
# block size
blockWidth = 116
blockHeight = 100
# block position
greenBlockPositionX = WIDTH - WIDTH + 20
greenBlockPositionY = HEIGHT * 0.01
redBlockPositionX = WIDTH - WIDTH + 20
redBlockPositionY = HEIGHT * 0.21
blueBlockPositionX = WIDTH - WIDTH + 20
blueBlockPositionY = HEIGHT * 0.41
violetBlockPositionX = WIDTH - WIDTH + 20
violetBlockPositionY = HEIGHT * 0.61
whiteBlockPositionX = WIDTH - WIDTH + 20
whiteBlockPositionY = HEIGHT * 0.81
# credits
money = 30

BlockCreating = False
mouseHoverARectangle = False 

############### Pygame Window ###############
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(GREY)#color background

#################Images Load ################
bigHexRed = pygame.image.load("/Users/ludwigdanvin/others/hexpace/img/bigHexRed.png").convert_alpha()
bigHexRedRect = bigHexRed.get_rect()
bigHexRedRect.x = redBlockPositionX
bigHexRedRect.y = redBlockPositionY

bigHexBlue = pygame.image.load("/Users/ludwigdanvin/others/hexpace/img/bigHexBlue.png").convert_alpha()
bigHexBlueRect = bigHexBlue.get_rect()
bigHexBlueRect.x = blueBlockPositionX
bigHexBlueRect.y = blueBlockPositionY

bigHexGreen = pygame.image.load("/Users/ludwigdanvin/others/hexpace/img/bigHexGreen.png").convert_alpha()
bigHexGreenRect = bigHexGreen.get_rect()
bigHexGreenRect.x = greenBlockPositionX
bigHexGreenRect.y = greenBlockPositionY

bigHexViolet = pygame.image.load("/Users/ludwigdanvin/others/hexpace/img/bigHexViolet.png").convert_alpha()
bigHexVioletRect = bigHexViolet.get_rect()
bigHexVioletRect.x = violetBlockPositionX
bigHexVioletRect.y = violetBlockPositionY

bigHexWhite = pygame.image.load("/Users/ludwigdanvin/others/hexpace/img/bigHexWhite.png").convert_alpha()
bigHexWhiteRect = bigHexWhite.get_rect()
bigHexWhiteRect.x = whiteBlockPositionX
bigHexWhiteRect.y = whiteBlockPositionY

################### CLASS ###################
class redBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bigHexRed, (blockWidth, blockHeight))
        self.rect = self.image.get_rect()
        self.rect.center = (blockWidth/2, blockHeight/2)
        self.name = 'weapon'
        self.condition = 5
        self.power = 1
        self.speed = 1 
        self.firingRate = 1
        self.weight = 10

    def update(self):
        if BlockCreating == True:
            mouseX, mouseY = pygame.mouse.get_pos()
            newBlock.rect.center = (mouseX,mouseY)

class blueBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bigHexBlue, (blockWidth, blockHeight))
        self.rect = self.image.get_rect()
        self.rect.center = (blockWidth/2, blockHeight/2)
        self.name = 'motor'
        self.condition = 5
        self.power = 1  
        self.weight = 10

    def update(self):
        if BlockCreating == True:
            mouseX, mouseY = pygame.mouse.get_pos()
            newBlock.rect.center = (mouseX,mouseY) 

class violetBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bigHexViolet, (blockWidth, blockHeight))
        self.rect = self.image.get_rect()
        self.rect.center = (blockWidth/2, blockHeight/2)
        self.name = 'shield'
        self.condition = 5
        self.reloadSpeed = 1 
        self.weight = 10

    def update(self):
        if BlockCreating == True:
            mouseX, mouseY = pygame.mouse.get_pos()
            newBlock.rect.center = (mouseX,mouseY)

class greenBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bigHexGreen, (blockWidth, blockHeight))
        self.rect = self.image.get_rect()
        self.rect.center = (blockWidth/2, blockHeight/2)
        self.name = 'tank'
        self.condition = 5
        self.storageCapacity = 1
        self.refillSpeed = 1
        self.weight = 10
    
    def update(self):
        if BlockCreating == True:
            mouseX, mouseY = pygame.mouse.get_pos()
            newBlock.rect.center = (mouseX,mouseY)

class whiteBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bigHexWhite, (blockWidth, blockHeight))
        self.rect = self.image.get_rect()
        self.rect.center = (blockWidth/2, blockHeight/2)
        self.weight = 10

    def update(self):
        if BlockCreating == True:
            mouseX, mouseY = pygame.mouse.get_pos()
            newBlock.rect.center = (mouseX,mouseY)

################### ARRAY ###################
Plateau = [[None]*5 for i in range(7)]      
PlateauBlock = [[None]*5 for i in range(7)]
dictBlockClass =    {
                    bigHexRed: redBlock(), 
                    bigHexBlue: blueBlock(), 
                    bigHexGreen: greenBlock(), 
                    bigHexViolet: violetBlock(),
                    bigHexWhite: whiteBlock()
                    }
dictBlockVariable = {
                    bigHexRed: 'newRedBlock', 
                    bigHexBlue: 'newBlueBlock', 
                    bigHexGreen: 'newGreenBlock', 
                    bigHexViolet: 'newVioletBlock',
                    bigHexWhite: 'newWhiteBlock'
                    }                    

################# Sprite Group #################
all_sprites = pygame.sprite.Group()
all_sprites.draw(window)

############### Fonctions ###############
#def blockInfo():
    

############### Refresh window ###############
pygame.display.update()

#################################################
################### MAIN LOOP ###################
running = True
while running:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False
        # MOUSE BUTTON DOWN
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if bigHexRedRect.collidepoint(pygame.mouse.get_pos()):
                    print('Red')
                    pygame.mouse.set_pos(bigHexRedRect.center)
                    newBlock = redBlock()
                    all_sprites.add(newBlock)    
                    BlockCreating = True
                if bigHexBlueRect.collidepoint(pygame.mouse.get_pos()):
                    print('Blue')  
                    pygame.mouse.set_pos(bigHexBlueRect.center) 
                    newBlock = blueBlock()
                    all_sprites.add(newBlock)    
                    BlockCreating = True
                if bigHexVioletRect.collidepoint(pygame.mouse.get_pos()):
                    print('Violet')
                    pygame.mouse.set_pos(bigHexVioletRect.center)
                    newBlock = violetBlock()
                    all_sprites.add(newBlock)    
                    BlockCreating = True
                if bigHexGreenRect.collidepoint(pygame.mouse.get_pos()):
                    print('green')
                    pygame.mouse.set_pos(bigHexGreenRect.center)
                    newBlock = greenBlock()
                    all_sprites.add(newBlock)    
                    BlockCreating = True
                if bigHexWhiteRect.collidepoint(pygame.mouse.get_pos()):
                    print('white') 
                    pygame.mouse.set_pos(bigHexWhiteRect.center)
                    newBlock = whiteBlock()
                    all_sprites.add(newBlock)    
                    BlockCreating = True
            
            # Display Block information
            for i in range(7):
                for j in range(5):
                    if PlateauBlock[i][j] != None:
                        if PlateauBlock[i][j].rect.collidepoint(pygame.mouse.get_pos()):
                            print(PlateauBlock[i][j].condition)
        # MOUSE BUTTON UP
        if event.type == pygame.MOUSEBUTTONUP and BlockCreating == True:
            k=0
            up=False
            for i in range(7): 
                if BlockCreating == True:  
                    if up == True:
                        k+=50
                        up = False
                    else:
                        k-=50  
                        up = True  
                    for j in range(5):
                        print(newBlock)
                        if BlockCreating == True:
                            print(i,j)
                            if Plateau[i][j].collidepoint(pygame.mouse.get_pos()):
                                if PlateauBlock[i][j] == None: 
                                    newBlock.rect.center = Plateau[i][j].center
                                    print(Plateau[i][j])
                                    PlateauBlock[i][j] = newBlock
                                    newBlock = None
                                    BlockCreating = False                            
                                else:
                                    newBlock.kill()
                                    newBlock = None
                                    BlockCreating = False
            if BlockCreating == True:
                newBlock.kill()
                newBlock = None
                BlockCreating = False        

    ################### Update ###################
    all_sprites.update()
    #################### DRAW ####################
    window.fill(GREY)
    window.blit(bigHexGreen, bigHexGreenRect)
    window.blit(bigHexRed, bigHexRedRect)
    window.blit(bigHexBlue, bigHexBlueRect)
    window.blit(bigHexViolet, bigHexVioletRect)
    window.blit(bigHexWhite, bigHexWhiteRect)

    all_sprites.draw(window)
    # Tableau
    k=0
    up=False
    for i in range(7):
        if up == True:
            k+=blockHeight/2
            up = False
        else:
            k-=blockHeight/2  
            up = True  
        for j in range(5):
            if PlateauBlock[i][j] != None:
                all_sprites.add(PlateauBlock[i][j])
            else:
                Plateau[i][j] = pygame.draw.rect(window,BLUE,((i*87)+200,(j*100)+100+k,blockWidth/2,blockHeight/2))
                
    
    ############### Refresh window ###############
    pygame.display.update()

pygame.quit()