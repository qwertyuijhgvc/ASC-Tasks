# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Dr Storey's test pygame program")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Global variables
x_val = 50
y_val = 50
x_offset = 5
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
    x_val = x_val + x_offset
    if x_val > size[0]:
        x_val = -50
        x_offset = x_offset + 2
    # end if


    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    # Draw stuff here
    pygame.draw.rect(screen, RED, [x_val, y_val, 20, 25])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

# end while

pygame.quit()