import pygame
pygame.init()
done = False
import random
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
#Set screen and caption
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
#To see if game is over
lose = False
#x y values for pong ball
x_val_ball = 350
y_val_ball = 250
#offset for the pong ball
x_offset = random.choice([4, -4])
y_offset = random.choice([4, -4])
#Lives and x y values for the two players
p1_lives = 5
p1_x_val_rect = 600
p1_y_val_rect = 300
p2_lives = 5
p2_x_val_rect = 100
p2_y_val_rect = 300
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
   #Make the pong ball move
    x_val_ball += x_offset
    y_val_ball += y_offset
    #Make it bounce off bottom
    if (y_val_ball >= 480):
        y_offset = -1 * y_offset
    #end if
    #Resets positions and reduces p1 lives if p1 misses ball
    if (x_val_ball >= 680 ):
        p1_lives -= 1
        x_val_ball = 350
        y_val_ball = 250
        p1_x_val_rect = 600
        p1_y_val_rect = 250
        p2_x_val_rect = 100
        p2_y_val_rect = 250
        #Make the ball start off by moving in random direction
        x_offset = random.choice([4, -4])
        y_offset = random.choice([4, -4])
        pygame.time.wait(500)
    #end if
    #Make it bounce off top
    if (y_val_ball <= 0):
        y_offset = -1 * y_offset
    #end if
    #Resets positions and reduces p1 lives if p2 misses ball
    if (x_val_ball <= 0):
        p2_lives -= 1
        x_val_ball = 350
        y_val_ball = 250
        p1_x_val_rect = 600
        p1_y_val_rect = 250
        p2_x_val_rect = 100
        p2_y_val_rect = 250
        x_offset = random.choice([4, -4])
        y_offset = random.choice([4, -4])
        pygame.time.wait(500)
    #end if
    #Check to see if keys are pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        move_up = True
    if keys[pygame.K_DOWN]:
        move_down = True
    if keys[pygame.K_w]:
        move_W = True
    if keys[pygame.K_s]:
        move_S = True
        #end if     
    #Check to see if key is released
    if not keys[pygame.K_UP]:
        move_up = False
    if not keys[pygame.K_DOWN]:
        move_down = False
    if not keys[pygame.K_w]:
         move_W = False
    if not keys[pygame.K_s]:
        move_S = False
        #end if
    #movement
    if move_up and p1_y_val_rect >= 0:
        p1_y_val_rect -= 5
    elif move_down and p1_y_val_rect <= 400:
        p1_y_val_rect += 5
    #Turbo mode
    if move_up and p1_y_val_rect >= 0 and keys[pygame.K_RSHIFT]:
        p1_y_val_rect -= 7
    elif move_down and p1_y_val_rect <= 400 and keys[pygame.K_RSHIFT]:
        p1_y_val_rect += 7
    #end if
    if move_W and p2_y_val_rect >= 0:
        p2_y_val_rect -= 5
    elif move_S and p2_y_val_rect <= 400:
        p2_y_val_rect += 5
    #Turbo mode
    if move_W and p2_y_val_rect >= 0 and keys[pygame.K_LSHIFT]:
        p2_y_val_rect -= 7
    elif move_S and p2_y_val_rect <= 400 and keys[pygame.K_LSHIFT]:
        p2_y_val_rect += 7
    #Set variable for the objects
    ball = pygame.Rect([x_val_ball, y_val_ball, 20,20] )
    player2 = pygame.Rect([p2_x_val_rect,p2_y_val_rect, 20, 100])
    player1 = pygame.Rect([p1_x_val_rect,p1_y_val_rect, 20, 100])
    #Collision
    collide1 = pygame.Rect.colliderect(player1,ball)
    collide2 = pygame.Rect.colliderect(player2,ball)
    if collide1:
        x_offset = -1.1 * x_offset
    #end if
    if collide2:
        x_offset = -1.1 * x_offset
    #end if
    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)        
    #Draw here
    draw_text("P1 Lives: " + str(p1_lives), text_font, WHITE, 350, 10 )
    draw_text("Hold shift for turbo", text_font, WHITE, 150, 400 )
    draw_text("P2 Lives: " + str(p2_lives), text_font, WHITE, 50, 10 )
    #To draw on screen the winner then end the program
    if lose:
        done = True
    #end if
    if (p1_lives == 0):
        draw_text("Player 2 wins", text_font, WHITE, 250, 200 )
        lose= True
        pygame.time.wait(1000)
    #end if
    if (p2_lives == 0):
        draw_text("Player 1 wins", text_font, WHITE, 250, 200 )
        lose= True
        pygame.time.wait(1000)
    #end if
    #Pong ball
    pygame.draw.rect(screen, WHITE, [x_val_ball, y_val_ball, 20,20] )
    #Player 2
    pygame.draw.rect(screen, WHITE, [p2_x_val_rect,p2_y_val_rect, 20, 100])        
    #Player 1
    pygame.draw.rect(screen, WHITE, [p1_x_val_rect,p1_y_val_rect, 20, 100])      
    #Update screen
    pygame.display.flip()  
    #Framerate
    clock.tick(60)
#end while