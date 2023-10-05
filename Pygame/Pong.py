import pygame
pygame.init()
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
# Loop until the user clicks the close button.
done = False
# Defining Text
text_font = pygame.font.SysFont("Arial", 50)
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))
 #colours
BLACK = (0,0,0)
WHITE = (255, 255 ,255)
#Define Values
lose = False
x_val_ball = 350
y_val_ball = 250
x_offset = 3
y_offset = 3
p1_lives = 5
p1_x_val_rect = 600
p1_y_val_rect = 250
p2_lives = 5
p2_x_val_rect = 100
p2_y_val_rect = 250
# Define move value
move_W = False
move_S = False
move_up = False
move_down = False

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
   # --- Game logic should go here
    x_val_ball += x_offset
    y_val_ball += y_offset
    if (y_val_ball >= 480):
        y_offset = -1 * y_offset
    #end if
    if (x_val_ball >= 680 ):
        p1_lives -= 1
        x_val_ball = 350
        y_val_ball = 250
        p1_x_val_rect = 600
        p1_y_val_rect = 250
        p2_x_val_rect = 100
        p2_y_val_rect = 250
        x_offset = 3
        y_offset = 3
        pygame.time.wait(500)
    #end if
    if (y_val_ball <= 0):
        y_offset = -1 * y_offset
    #end if
    if (x_val_ball <= 0):
        p2_lives -= 1
        x_val_ball = 350
        y_val_ball = 250
        p1_x_val_rect = 600
        p1_y_val_rect = 250
        p2_x_val_rect = 100
        p2_y_val_rect = 250
        x_offset = 3
        y_offset = 3
        pygame.time.wait(500)
    #end if
    #Check to see if keys are pressed
    if event.type == pygame.KEYDOWN:
            # Check to see if any of the arrow keys are pressed
        if event.key == pygame.K_UP:
                move_up = True
        elif event.key == pygame.K_DOWN:
                move_down = True
        #end if
        if event.key == pygame.K_LEFT:
            move_W = True
        elif event.key == pygame.K_RIGHT:
            move_S = True
        #end if     
        # Check what happens when a key is released
    elif event.type == pygame.KEYUP:
            # Check to see if any of the arrow keys are pressed
        if event.key == pygame.K_UP:
            move_up = False
        elif event.key == pygame.K_DOWN:
            move_down = False
        #end if
        if event.key == pygame.K_LEFT:
            move_W = False
        elif event.key == pygame.K_RIGHT:
            move_S = False
        #end if
    #movement
    if move_up and p1_y_val_rect >= 0:
        p1_y_val_rect -= 3
    elif move_down and p1_y_val_rect <= 400:
        p1_y_val_rect += 3
    #end if
    if move_W and p2_y_val_rect >= 0:
        p2_y_val_rect -= 3
    elif move_S and p2_y_val_rect <= 400:
        p2_y_val_rect += 3
    #Set variable for the objects
    ball = pygame.Rect([x_val_ball, y_val_ball, 20,20] )
    player2 = pygame.Rect([p2_x_val_rect,p2_y_val_rect, 20, 100])
    player1 = pygame.Rect([p1_x_val_rect,p1_y_val_rect, 20, 100])
    #Collision
    collide1 = pygame.Rect.colliderect(player1,ball)
    collide2 = pygame.Rect.colliderect(player2,ball)
    if collide1:
        x_offset = -1 * x_offset
    #end if
    if collide2:
        x_offset = -1 * x_offset
    #end if
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)        
    #Draw here
    draw_text("P1 Lives: " + str(p1_lives), text_font, WHITE, 350, 10 )
    draw_text("P2 Lives: " + str(p2_lives), text_font, WHITE, 50, 10 )
    if lose:
        done = True
    if (p1_lives == 0):
        draw_text("Player 2 wins", text_font, WHITE, 250, 200 )
        lose= True
        pygame.time.wait(1000)
    if (p2_lives == 0):
        draw_text("Player 1 wins", text_font, WHITE, 250, 200 )
        lose= True
        pygame.time.wait(1000)
    #end if
    pygame.draw.rect(screen, WHITE, [x_val_ball, y_val_ball, 20,20] )
    pygame.draw.rect(screen, WHITE, [p2_x_val_rect,p2_y_val_rect, 20, 100])        
    pygame.draw.rect(screen, WHITE, [p1_x_val_rect,p1_y_val_rect, 20, 100])      
    pygame.display.flip()
            
    clock.tick(60)
#end while