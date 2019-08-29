import pygame

pygame.init()

################# VARIABLES #################
# colors
GREY = (152,152,152)
BLUE = (0,87,128)

WIDTH = 1024
HEIGHT = 576
blockWidth = 116
blockHeight = 100
greenBlockPositionX = WIDTH - WIDTH + 20
greenBlockPositionY = HEIGHT * 0.7

GreenBlockCreated = False
mouseHoverARectangle = False 

############### Pygame Window ###############
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(GREY)#background

#################Images Load ################
bigHexRed = pygame.image.load("/home/ludwig/hexpace/bigHexRed.png").convert_alpha()
bigHexBlue = pygame.image.load("/home/ludwig/hexpace/bigHexBlue.png").convert_alpha()
bigHexGreen = pygame.image.load("/home/ludwig/hexpace/bigHexGreen.png").convert_alpha()
bigHexViolet = pygame.image.load("/home/ludwig/hexpace/bigHexViolet.png").convert_alpha()
bigHexWhite = pygame.image.load("/home/ludwig/hexpace/bigHexWhite.gif").convert_alpha()

################### ARRAY ###################
Plateau = [[None]*5 for i in range(7)]      
PlateauBlock = [[None]*5 for i in range(7)]

################### CLASS ###################
class redBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bigHexRed, (blockWidth, blockHeight))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 10, HEIGHT * 0.1)  

class blueBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bigHexBlue, (blockWidth, blockHeight))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 10, HEIGHT * 0.3) 
    
class violetBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # sprite image
        self.image = pygame.transform.scale(bigHexViolet, (blockWidth, blockHeight))
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        # position the sprite on the screen
        self.rect.center = (WIDTH / 10, HEIGHT * 0.5) 

class greenBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bigHexGreen, (blockWidth, blockHeight))
        self.rect = self.image.get_rect()
        self.rect.center = (blockWidth/2, blockHeight/2)
        self.condition = 5
        self.storageCapacity = 1
        self.refillSpeed = 1

    def update(self):
        if GreenBlockCreated == True:
            mouseX, mouseY = pygame.mouse.get_pos()
            GreenBlock.rect.center = (mouseX,mouseY)

################# Sprite Group #################
all_sprites = pygame.sprite.Group()

RedBlock = redBlock()
all_sprites.add(RedBlock)
blueBlock = blueBlock()
all_sprites.add(blueBlock)
violetBlock = violetBlock()
all_sprites.add(violetBlock)


all_sprites.draw(window)

############### Fonctions ###############
def blockInfo():
    

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
                mouseX, mouseY = pygame.mouse.get_pos()
                print (mouseX, mouseY)
                if mouseX > greenBlockPositionX and mouseX < greenBlockPositionX + blockWidth and mouseY > greenBlockPositionY and mouseY < greenBlockPositionY + blockHeight:
                    print ('Detected')
                    pygame.mouse.set_pos(greenBlockPositionX + (blockWidth/2), greenBlockPositionY + (blockHeight/2))
                    GreenBlock = greenBlock()
                    all_sprites.add(GreenBlock)    
                    GreenBlockCreated = True
                for i in range(7):
                    for j in range(5):
                        if PlateauBlock[i][j] != None:
                            if PlateauBlock[i][j].rect.collidepoint(pygame.mouse.get_pos()):
                                print(PlateauBlock[i][j].condition)
        if event.type == pygame.MOUSEBUTTONUP and GreenBlockCreated == True:
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
                            GreenBlock.rect.center = Plateau[i][j].center
                            print(Plateau[i][j])
                            PlateauBlock[i][j] = GreenBlock
                            GreenBlockCreated = False
                        else:
                            GreenBlock.kill()
                            GreenBlockCreated = False
                    else:
                        print('A block is already here')   
                        GreenBlock.kill()
                        GreenBlockCreated = False     

    ################### Update ###################
    all_sprites.update()
    #################### DRAW ####################
    window.fill(GREY)
    window.blit(bigHexGreen, (greenBlockPositionX, greenBlockPositionY))
    all_sprites.draw(window)
    # Tableau
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
            if PlateauBlock[i][j] != None:
                all_sprites.add(PlateauBlock[i][j])
            else:
                Plateau[i][j] = pygame.draw.rect(window,BLUE,((i*87)+200,(j*100)+100+k,blockWidth/2,blockHeight/2))
                
    
    ############### Refresh window ###############
    pygame.display.update()

pygame.quit()