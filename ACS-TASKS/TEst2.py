import pygame, sys

# First thing in any pygame program, initializes pygame variables
pygame.init()

# Set up variables for screen size in pixels
# Set this up as a tuple which is a pair of values
size = width, height = 640, 480

# Initialize a window with the screen size
screen = pygame.display.set_mode(size)

# Create a clock to control the program's frame rate
clock = pygame.time.Clock()

# Create variable to store location and shape size for drawing
shape_position = (width/2, height/2)
shape_position2 = (150, 35)
shape_position3 = (10, 100)
shape_size = (50, 50)

# Make a pygame.rectangle variable
shape_rect = pygame.Rect(shape_position, shape_size)
shape_rect2 = pygame.Rect(shape_position2, shape_size)
shape_rect3 = pygame.Rect(shape_position3, shape_size)

# RGB colours for shapes
shape_colour = (142, 58, 60)
line_colour = (51, 116, 48)
circle_colour = (143, 122, 59)

# Player Variables
circle_pos = (50, 50)
circle_radius = 25

# Coin Variables
coin_colour = (255, 255, 0)
coin_pos = (600, 400)
coin_radius = 10

# Coin collision box
# coin_collision = pygame.Rect(coin_pos[0] - coin_radius)

# Define move value
move_right = False
move_left = False
move_up = False
move_down = False

# Game loop
while True:
    # Moves the clock forward 60 frames per second
    clock.tick(60)
    
    # For loop gets any keyboard, mouse, or other events from user input
    for event in pygame.event.get(): 
        # pygame.quit happens when someone tries to close the game window
        if event.type == pygame.QUIT:
            sys.exit()
        # Check to see if a key is pressed
        elif event.type == pygame.KEYDOWN:
            # Check to see if any of the arrow keys are pressed
            if event.key == pygame.K_RIGHT:
                move_right = True
            elif event.key == pygame.K_LEFT:
                move_left = True
            elif event.key == pygame.K_UP:
                move_up = True
            elif event.key == pygame.K_DOWN:
                move_down = True
                
        # Check what happens when a key is released
        elif event.type == pygame.KEYUP:
            # Check to see if any of the arrow keys are pressed
            if event.key == pygame.K_RIGHT:
                move_right = False
            elif event.key == pygame.K_LEFT:
                move_left = False
            elif event.key == pygame.K_UP:
                move_up = False
            elif event.key == pygame.K_DOWN:
                move_down = False
        
    # Player controls
    # // means to remove the remainder of a division operation
    if move_right:
        circle_pos = (circle_pos[0] + 60 // 10, circle_pos[1])
    elif move_left:
        circle_pos = (circle_pos[0] - 60 // 10, circle_pos[1])
    elif move_up:
        circle_pos = (circle_pos[0], circle_pos[1] - 60 // 10)
    elif move_down:
        circle_pos = (circle_pos[0], circle_pos[1] + 60 // 10)
                
    # Fill the screen with a solid colour
    screen.fill((255, 252, 252))
    
    # Fill the rectangle with a shape colour. This is the fastest way to draw a rectangle
    screen.fill(shape_colour, rect = shape_rect)
    screen.fill(shape_colour, rect = shape_rect2)
    screen.fill(shape_colour, rect = shape_rect3)
    
    # If you need more complex shapes or lines use pygame.draw
    
    # Draw a circle on a given surface, along with its colour, position, and radius
    pygame.draw.circle(screen, circle_colour, circle_pos, 25)
    
    # Draw a line on the given surface, along with its colour, start position, end position, and line thickness
    # pygame.draw.line(screen, line_colour, circle_pos, shape_rect.center, 4)

    # At the end of each game loop, call this to update the screen
    pygame.display.flip()