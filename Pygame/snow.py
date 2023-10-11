import pygame
import random
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 153,   0,   0)
BLUE   =   0,   205, 255
YELLOW = (255, 255, 0)
BROWN = (102, 51, 0)
LIGHT_BROWN = (153, 76, 0)

# Loop until the user clicks the close button.
done = False

#Screen details
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Let it snow")
#Classes 
class Snow(pygame.sprite.Sprite):
    
    #Constructor Function
    def __init__(self, s_width, s_length):
        super().__init__()
        self.image = pygame.Surface([s_width,s_length])
        self.image.fill(WHITE)
        self.speed = random.randrange(1,10)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,700)
        self.rect.y = random.randrange(0,400)
    # end of contruction function
    def update(self):
        if self.rect.y > 500 :
            self.rect.y = -50
            self.speed = random.randrange(1,10)
        else:
            self.rect.y = self.rect.y + self.speed
#end class Snow


 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#Global Variables
snow_group = pygame.sprite.Group()
number_of_flakes = 3000
for i in range (number_of_flakes):
    flake = Snow(2,2)
    snow_group.add(flake)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
    snow_group.update()
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLUE)

    #Draw here
    snow_group.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60)
 #end while

pygame.quit()