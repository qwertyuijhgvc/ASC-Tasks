import pygame

pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
blue    =   0,   205, 255
YELLOW = (255, 255, 0)
blue =list(blue)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Professor Craven's Cool Game")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#Global Variables

x_val = 15
y_val = 100
offset = 1
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
    x_val += 3
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(blue)
    if (blue[1] > 0):
        blue[1] -= 1
        blue[2] -= 1
    #Draw here
    pygame.draw.circle(screen, YELLOW, [x_val, y_val], 20)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 #end while

pygame.quit()
