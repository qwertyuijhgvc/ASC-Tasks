import pygame
from pygame.locals import *
#initialize pygame
pygame.init()
#set colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0,   0, 255)
PINK = (255,51,255)
ORANGE = (255,128,0)
RED = (255,0,0)
#set clock and screen
clock = pygame.time.Clock()
size = (700, 500)
screen = pygame.display.set_mode(size)
# Creating Classes
# Creating PACMAN class
class pac_man(pygame.sprite.Sprite):
    #constructor function
    def __init__(self, s_width, s_length):
        super().__init__()
        self.image = pygame.Surface([s_width, s_length])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 450
        self.prevx = 0
        self.prevy= 0
        self.direction = "E"
        self.lives = 3
    #end constructor
    #update procedure to mkae pacman move
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.direction = "W"
        elif keys[pygame.K_d]:
            self.direction = "E"
        elif keys[pygame.K_w]:
            self.direction = "N"
        elif keys[pygame.K_s]:
            self.direction = "S"
        if self.direction == "W":
            self.prevx = self.rect.x
            self.rect.x -= 3
        elif self.direction == "N":
            self.prevy = self.rect.y
            self.rect.y -= 3
        elif self.direction == "E":
            self.prevx = self.rect.x
            self.rect.x += 3
        elif self.direction == "S":
            self.prevy = self.rect.y
            self.rect.y += 3
        if self.rect.x > 750:
            self.rect.x = -50
        elif self.rect.x < -50:
            self.rect.x = 750
        if self.rect.y > 550:
            self.rect.y = -50
        elif self.rect.y < -50:
            self.rect.y = 550
    #end procedure
    #procedure to make him go back to previous location when he hits a wall so he can't go through
    def go_back(self):
        self.rect.x = self.prevx
        self.rect.y = self.prevy
    #end procedure
    def get_x(self):
        return self.rect.x
    #end function
    def get_y(self):
        return self.rect.y
    #end function
    #To make pacman take damage
    def take_damage(self):
        self.lives -= 1
    #end procedure
#end class

#class for individual blocks in the wall
class Block(pygame.sprite.Sprite):
    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_cord
        self.rect.y = y_cord
    #end constructor
#end class

#class for the ghost enemies
class Ghost(pygame.sprite.Sprite):
    def __init__(self,):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    #end constructor
#end class
#Classes for each ghost
class Pinky(Ghost):
    def __init__(self,):
        super().__init__() 
        self.image.fill(PINK)
        self.rect.x = 100
        self.rect.y = 100
        
class Blinky(Ghost):
    def __init__(self):
        super().__init__()  
        self.image.fill(BLUE)
        self.rect.x = 600
        self.rect.y = 100
        
class Inky(Ghost):
    def __init__(self,):
        super().__init__()  
        self.image.fill(RED)
        self.rect.x = 100
        self.rect.y = 400
        
        
class Clyde(Ghost):
    def __init__(self,):
        super().__init__()
        self.image.fill(ORANGE)
        self.rect.x = 600
        self.rect.y = 400


# Variables
done = False
all_sprites_list = pygame.sprite.Group() # New group for all sprites
wall_sprites = pygame.sprite.Group()  #Group for walls
player = pac_man(40, 40) #The player
#add player into sprite gorup
all_sprites_list.add(player)
#Create walls
for _ in range(35):
    wall_segment = Block(20 * _, 200)
    wall_sprites.add(wall_segment)
all_sprites_list.add(wall_sprites)
#Create ghosts
clyde = Clyde()
pinky = Pinky()
inky = Inky()
blinky = Blinky()
all_sprites_list.add(clyde)
all_sprites_list.add(pinky)
all_sprites_list.add(inky)
all_sprites_list.add(blinky)
#Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Check for collisions with walls
    collisions = pygame.sprite.spritecollide(player, wall_sprites, False)
    # Makes sure player can't go through walls
    if collisions:
       player.go_back()
    # Drawing objects on screen
    screen.fill(BLACK)
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    #Draws pacman character on top of player hitbox/hurtbox
    pygame.draw.circle(screen, YELLOW, (player.get_x() +20, player.get_y()+20),20)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
