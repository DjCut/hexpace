import pygame
import random

pygame.init()

# VARIABLES
GREY = (152,152,152)
WIDTH = 1024
HEIGHT = 576
global GreenBlockCreated
GreenBlockCreated = False

#Ouverture de la fenêtre Pygame
window = pygame.display.set_mode((WIDTH, HEIGHT))

#Images Load
window.fill(GREY)#background

bigHexRed = pygame.image.load("/home/ludwig/hexpace/bigHexRed.png").convert_alpha()
bigHexBlue = pygame.image.load("/home/ludwig/hexpace/bigHexBlue.png").convert_alpha()
bigHexGreen = pygame.image.load("/home/ludwig/hexpace/bigHexGreen.png").convert_alpha()
bigHexViolet = pygame.image.load("/home/ludwig/hexpace/bigHexViolet.png").convert_alpha()
bigHexWhite = pygame.image.load("/home/ludwig/hexpace/bigHexWhite.gif").convert_alpha()

#OBJECT CLASS
class redBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bigHexRed, (116, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 10, HEIGHT * 0.1)  

class blueBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # sprite image
        self.image = pygame.transform.scale(bigHexBlue, (116, 100))
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        # position the sprite on the screen
        self.rect.center = (WIDTH / 10, HEIGHT * 0.3) 
    
class violetBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # sprite image
        self.image = pygame.transform.scale(bigHexViolet, (116, 100))
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        # position the sprite on the screen
        self.rect.center = (WIDTH / 10, HEIGHT * 0.5) 

class greenBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bigHexGreen, (116, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 10, HEIGHT * 0.7) 

    def update(self):
        GreenBlock.rect = (pygame.mouse.get_pos())

# Sprite Group
all_sprites = pygame.sprite.Group()

RedBlock = redBlock()
all_sprites.add(RedBlock)
blueBlock = blueBlock()
all_sprites.add(blueBlock)
violetBlock = violetBlock()
all_sprites.add(violetBlock)


all_sprites.draw(window)

#Rafraîchissement de l'écran
pygame.display.flip()

#MAIN LOOP
running = True
while running:
    for event in pygame.event.get():    #Attente des événements
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print('click gauche pressed')
                mouseX, mouseY = pygame.mouse.get_pos()
                print (mouseX, mouseY)
                if mouseX > WIDTH / 10 and mouseX < WIDTH / 10 + 116 and mouseY > HEIGHT * 0.7 and mouseY < HEIGHT * 0.7 + 100:
                    print ('Detected')
                    GreenBlock = greenBlock()
                    GreenBlock.rect = GreenBlock.image.get_rect()
                    all_sprites.add(GreenBlock)                    
                    GreenBlockCreated = True
                    GreenBlock.rect(mouseX-58,mouseY-50)
        if event.type == pygame.MOUSEBUTTONUP and GreenBlockCreated == True:
            GreenBlock.kill()
            GreenBlockCreated = False
                     
    # Update
    all_sprites.update()
    # Draw / render
    window.fill(GREY)
    all_sprites.draw(window)
    window.blit(bigHexGreen, (WIDTH / 10, HEIGHT * 0.7))
    # Refresh window
    pygame.display.flip()

pygame.quit()