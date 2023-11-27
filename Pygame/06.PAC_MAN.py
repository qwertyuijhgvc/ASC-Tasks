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
class PAC_MAN(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length, s_radius):
        super().__init__()
        self.image = pygame.Surface([s_width,s_length])
        self.image.fill(YELLOW)
        self.x = 350
        self.y = 450
        self.radius = s_radius
        direction = "E"
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= 2
        if keys[pygame.K_d]:
            self.x += 2
        if keys[pygame.K_w]:
            self.y -= 2
        if keys[pygame.K_s]:
            self.y += 2
        pygame.draw.circle(screen, YELLOW, (self.x // 2, self.y // 2), self.radius)
    #end procedure
#end class
class Block(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 20
        self.height = 20

#Variables
done = False
all_sprites_list = pygame.sprite.Group()
wall_hit_list = pygame.sprite.Group()
player = PAC_MAN(20,20,20)    
all_sprites_list.add(player)
    
    
    

#end class
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            
            
            
    #Drawing objects on screen       
    screen.fill(BLACK)  
    all_sprites_list.update()  
    pygame.display.flip()     
pygame.quit