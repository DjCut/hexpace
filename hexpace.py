import pygame

pygame.init()

################# VARIABLES #################
# colors
GREY = (152,152,152)
BLUE = (0,87,128)
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
bigHexRed = pygame.image.load("/home/ludwig/hexpace/bigHexRed.png").convert_alpha()
bigHexBlue = pygame.image.load("/home/ludwig/hexpace/bigHexBlue.png").convert_alpha()
bigHexGreen = pygame.image.load("/home/ludwig/hexpace/bigHexGreen.png").convert_alpha()
bigHexViolet = pygame.image.load("/home/ludwig/hexpace/bigHexViolet.png").convert_alpha()
bigHexWhite = pygame.image.load("/home/ludwig/hexpace/bigHexWhite.png").convert_alpha()

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
            dictBlockVariable[bigHexRed].rect.center = (mouseX,mouseY)

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
            dictBlockVariable[bigHexBlue].rect.center = (mouseX,mouseY) 

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
            dictBlockVariable[bigHexViolet].rect.center = (mouseX,mouseY)

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
            dictBlockVariable[bigHexGreen].rect.center = (mouseX,mouseY)

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
                dictBlockVariable[bigHexWhite].rect.center = (mouseX,mouseY)

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print('click gauche pressed')
                for blockClass in dictBlockClass:
                    if blockClass.get_rect().collidepoint(pygame.mouse.get_pos()):
                        print('blockClass',blockClass)
                        print('dictBlockClass[blockClass]',dictBlockClass[blockClass])
                        print('dictBlockVariable[blockClass]',dictBlockVariable[blockClass])
                        pygame.mouse.set_pos(100 + (blockWidth/2), 100 + (blockHeight/2))
                        dictBlockVariable[blockClass] = dictBlockClass[blockClass]
                        all_sprites.add(dictBlockVariable[blockClass])    
                        BlockCreating = True
                for i in range(7):
                    for j in range(5):
                        if PlateauBlock[i][j] != None:
                            if PlateauBlock[i][j].rect.collidepoint(pygame.mouse.get_pos()):
                                print(PlateauBlock[i][j].condition)
        if event.type == pygame.MOUSEBUTTONUP and BlockCreating == True:
            k=0
            up=False
            for i in range(7):               
                if up == True:
                    k+=50
                    up = False
                else:
                    k-=50  
                    up = True  
                for j in range(5):
                    if PlateauBlock[i][j] == None:
                        if Plateau[i][j].collidepoint(pygame.mouse.get_pos()): 
                            newBlock.rect.center = Plateau[i][j].center
                            print(Plateau[i][j])
                            PlateauBlock[i][j] = newBlock
                            BlockCreating = False
                        else:
                            newBlock.kill()
                            BlockCreating = False
                    else:
                        print('A block is already here')   
                        newBlock.kill()
                        BlockCreating = False     

    ################### Update ###################
    all_sprites.update()
    #################### DRAW ####################
    window.fill(GREY)
    window.blit(bigHexGreen, (greenBlockPositionX, greenBlockPositionY))
    window.blit(bigHexRed, (redBlockPositionX, redBlockPositionY))
    window.blit(bigHexBlue, (blueBlockPositionX, blueBlockPositionY))
    window.blit(bigHexViolet, (violetBlockPositionX, violetBlockPositionY))
    window.blit(bigHexWhite, (whiteBlockPositionX, whiteBlockPositionY))

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