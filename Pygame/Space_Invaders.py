import pygame
import random
import pygame
import math

pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 153,   0,   0)
BLUE    =   (0,   0, 255)
YELLOW = (255, 255, 0)
BROWN = (102, 51, 0)
LIGHT_BROWN = (153, 76, 0)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("I always hated the color blue")
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Classes
class Player(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length):
        super().__init__()
        self.image = pygame.Surface([s_width,s_length])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 450
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 2
        if keys[pygame.K_d]:
            self.rect.x += 2
#end Class
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4,10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.y -= 3
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4,10])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x = 5

#Global Variables
all_sprites_list = pygame.sprite.Group()
player = Player(5, 5)
all_sprites_list.add(player)
keys = pygame.key.get_pressed()
#Define writing on screen 
text_font = pygame.font.SysFont("Arial", 50)
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    # --- Game logic should go here
    previous_time = pygame.time.get_ticks()
    all_sprites_list.update()
    if event.type == pygame.MOUSEBUTTONDOWN:
            current_time = pygame.time.get_ticks()
            # Fire a bullet if the user clicks the mouse button
            if current_time - previous_time > 500:
                bullet = Bullet()
            # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
            # Add the bullet to the lists
                all_sprites_list.add(bullet)
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    #Draw here
    all_sprites_list.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 #end while

pygame.quit()