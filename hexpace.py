import pygame
import random

pygame.init()

# VARIABLES
GREY = (152,152,152)
WIDTH = 1024
HEIGHT = 576

#Ouverture de la fenêtre Pygame
window = pygame.display.set_mode((WIDTH, HEIGHT))

#Images Load
window.fill(GREY)#background

bigHexRed = pygame.image.load("/home/ludwig/python/hexpace/bigHexRed.png").convert_alpha()
bigHexBlue = pygame.image.load("/home/ludwig/python/hexpace/bigHexBlue.png").convert_alpha()
bigHexGreen = pygame.image.load("/home/ludwig/python/hexpace/bigHexGreen.png").convert_alpha()
bigHexViolet = pygame.image.load("/home/ludwig/python/hexpace/bigHexViolet.png").convert_alpha()
bigHexWhite = pygame.image.load("/home/ludwig/python/hexpace/bigHexWhite.gif").convert_alpha()

#OBJECT CLASS
class redBlock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # sprite image
        self.image = pygame.transform.scale(bigHexRed, (116, 100))
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        # position the sprite on the screen
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
        # sprite image
        self.image = pygame.transform.scale(bigHexGreen, (116, 100))
        # find the rectangle that encloses the image
        self.rect = self.image.get_rect()
        # position the sprite on the screen
        self.rect.center = (WIDTH / 10, HEIGHT * 0.7) 

# Sprite Group
all_sprites = pygame.sprite.Group()
redBlock = redBlock()
all_sprites.add(redBlock)
blueBlock = blueBlock()
all_sprites.add(blueBlock)
violetBlock = violetBlock()
all_sprites.add(violetBlock)
greenBlock = greenBlock()
all_sprites.add(greenBlock)

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
                if redBlock.rect.collidepoint(pygame.mouse.get_pos()):
                    print ('Detected')
                    newRedBlock = redBlock()
                    all_sprites.add(newRedBlock)

    # Update
    all_sprites.update()

# Draw / render
    #all_sprites.draw(window)
    # *after* drawing everything, flip the display
pygame.display.flip()

pygame.quit()