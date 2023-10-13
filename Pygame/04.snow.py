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
        #Set snowflake sprite image
        self.image = pygame.Surface([s_width,s_length])
        self.image.fill(WHITE)
        #set speed
        self.speed = random.randrange(1,10)
        #MAke snowflake a rectangle
        self.rect = self.image.get_rect()
        #Set x y values
        self.rect.x = random.randrange(0,700)
        self.rect.y = random.randrange(0,400)
    # end of contruction function
    def update(self):
        #To make snow spawn back at top of screen when it hits bottom
        if self.rect.y > 500 :
            self.rect.y = -50
            self.speed = random.randrange(1,10)
        else:
            #To make snow move down
            self.rect.y = self.rect.y + self.speed
        if self.rect.x < 0:
            #Makes snow spawn back when it goes off left side or screen
            self.rect.x = random.randrange(0,700)
        else:
            #Makes snow move slightly sideways
            self.rect.x += random.randrange(-1,2)
    #end update
#end class Snow

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#Global Variables
#Set group for snow
snow_group = pygame.sprite.Group()
#Determine amount of snaowflakes
number_of_flakes = 3000
#Adds snowflakes to group
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
    #Updates position of snow
    snow_group.update()
    # --- Drawing code should go here
    # above this, or they will be erased with this command.
    #Creates screen color
    screen.fill(BLUE)

    #Draw here
    #Draws snowflakes
    snow_group.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
 #end while

pygame.quit()