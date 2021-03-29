import pygame
import math

pygame.init()

################# VARIABLES #################
# display
WIDTH = 1024
HEIGHT = 576

BLACK = (0,0,0)
GREEN = (0,255,0)


############### Pygame Window ###############
pygame.display.set_caption('Xspace')
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(BLACK)
clock = pygame.time.Clock()


#################Content Load ################
player_img = pygame.image.load("/Users/ludwigdanvin/others/hexpace/img/vessel.png").convert_alpha()

################### CLASS ###################

class vessel(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self._image_master = player_img
        self.image = self._image_master
        self.rect = self.image.get_rect()
        self.orientation = 0
        self.vector_x = 0.0
        self.vector_y = 0.0
        self.inertia_x = 0.0
        self.inertia_y = 0.0

        self.name = name
        self.condition = 5
        self.power = 1
        self.speed = 1 
        self.firingRate = 1
        self.weight = 10
    
    def get_vector(self):
        self.vector_x = round(math.sin(math.radians(self.orientation)),2)
        self.vector_y = round(math.cos(math.radians(self.orientation)),2)

    def run_engine(self):
        self.inertia_x += self.vector_x
        self.inertia_y += self.vector_y
        self.inertia_x = round(self.inertia_x, 1)
        self.inertia_y = round(self.inertia_y, 1)
    
    def turnLeft(self):
        self.orientation += 5
        if self.orientation > 360:
            self.orientation = 5
        self.update_orientation()
        self.get_vector()

    def turnRight(self):
        self.orientation -= 5
        if self.orientation < 0:
            self.orientation = 355
        self.update_orientation()
        self.get_vector()

    def update_orientation(self):
        oldCenter = self.rect.center
        self.image = pygame.transform.rotozoom(self._image_master, self.orientation, 1)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter

    def update(self):
        # Move FORWARD
        self.rect.x += (self.inertia_x)
        self.rect.y += (self.inertia_y)
        if self.rect.x < 0: 
            self.rect.x = 0
            self.inertia_x = 1
        if self.rect.x > window.get_width(): 
            self.rect.x = window.get_width()
            self.inertia_x = -1
        if self.rect.y < 0: 
            self.rect.y = 0
            self.inertia_y = 1
        if self.rect.y > window.get_height(): 
            self.rect.y = window.get_height()
            self.inertia_y = -1



class TextBox(pygame.sprite.Sprite):
    def __init__(self):
        self.font = pygame.font.Font('Spaceport_2006.otf', 8)
    
    def display(self, orientation, vector_x, vector_y, inertia_x, inertia_y, rect_x, rect_y):
        self.message = self.font.render(f">Orientation: {player.orientation} >Vector_x: {player.vector_x} >Vector_y: {player.vector_y} >intertia_x: {player.inertia_x} >inertia_y: {player.inertia_y} >rect.x: {player.rect.x} >rect.y: {player.rect.y}", True, GREEN, BLACK)
        self.message_rect = self.message.get_rect()

################# Sprite Group #################
all_sprites = pygame.sprite.Group()
all_sprites.draw(window)

############### Fonctions ###############
#def blockInfo():
    

############### Refresh window ###############
pygame.display.update()

#################################################
################### MAIN LOOP ###################
text_box = TextBox()
player = vessel('player')

player.rect.x = 200
player.rect.y = 200

running = True
while running:

    clock.tick(30)

    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            running = False
        # FORWARD
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.get_vector()
                player.run_engine()
                print(player.vector_x)
                print(player.vector_y)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_d]:
            player.turnRight()
        if keys_pressed[pygame.K_a]:
            player.turnLeft()

    ################### Update ###################
    #all_sprites.update()
    player.update()

    #################### DRAW ####################
    window.fill(BLACK)
    window.blit(player.image, player.rect)

    text_box.display(player.orientation, player.vector_x, player.vector_y, player.inertia_x, player.inertia_y, player.rect.x, player.rect.y)
    window.blit(text_box.message, text_box.message_rect)

    #all_sprites.draw(window)
                
    ############### Refresh window ###############
    pygame.display.update()

pygame.quit()