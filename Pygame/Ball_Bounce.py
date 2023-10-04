import pygame
pygame.init()
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncy Ball")
# Loop until the user clicks the close button.
done = False
 
 
 #colours
RED      = ( 153,   0,   0)
blue    =   0,   205, 255
 
x_val = 20
y_val = 20
x_offset = 3
y_offset = 3
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
   # --- Game logic should go here
        x_val += x_offset
        y_val += y_offset
        if (y_val >= 480):
            y_offset = -1 * y_offset
        #end if
        if (x_val >= 680 ):
            x_offset = -1 * x_offset
        #end if
        if (y_val <= 20):
            y_offset = -1 * y_offset
        #end if
        if (x_val <= 20):
            x_offset = -1 * x_offset
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(blue)        
    #Draw here
    pygame.draw.circle(screen, RED, [x_val, y_val], 20)        
            
    pygame.display.flip()
            
    clock.tick(60)
#end while