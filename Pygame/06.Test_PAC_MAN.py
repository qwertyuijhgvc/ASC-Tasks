import pygame
from pygame.locals import *
#initialize pygame
pygame.init()
#set colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

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
    pygame.draw.circle(screen, YELLOW, (player.get_x(), player.get_y()),20)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
