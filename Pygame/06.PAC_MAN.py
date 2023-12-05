import pygame
pygame.init()
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 153,   0,   0)
BLUE    =   (0,   0, 255)
YELLOW = (255, 255, 0)
BROWN = (102, 51, 0)
#Creating Classes
#Creating PACMAN class
size = (700, 500)
screen = pygame.display.set_mode(size)
class pac_man(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length, s_radius):
        super().__init__()
        self.image = pygame.Surface([s_width,s_length])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = 350
        self.y = 450
        self.radius = s_radius
        self.direction = "E"
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
                self.rect.x -= 1
                self.x -= 1
        elif self.direction == "N":
                self.rect.y -= 1
                self.y -= 1
        elif self.direction == "E":
                self.rect.x += 1
                self.x += 1
        elif self.direction == "S":
                self.rect.y += 1
                self.y += 1
        pygame.draw.circle(screen, YELLOW, (self.x // 2, self.y // 2), self.radius)
    #end procedure
#end class
class Block(pygame.sprite.Sprite):
    def __init__(self,x_cord,y_cord):
        super().__init__()
        self.image = pygame.Surface([20,20])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_cord
        self.rect.y = y_cord


#Variables
done = False
all_sprites_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
player = pac_man(20,20,20)    
player_list.add(player)
all_sprites_list.add(player)
wall_list = pygame.sprite.Group()   
for _ in range(35):
    wall_segment = Block(20*_,0)
    wall_list.add(wall_segment)
all_sprites_list.add(wall_list)


#end class
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

            
            
    #Drawing objects on screen       
    screen.fill(BLACK)  
    wall_list.draw(screen)
    all_sprites_list.update() 
    pygame.display.flip()     
pygame.quit