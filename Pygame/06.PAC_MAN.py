import pygame
pygame.init()
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 153,   0,   0)
BLUE    =   (0,   0, 255)
YELLOW = (255, 255, 0)
BROWN = (102, 51, 0)
#Creating PACMAN class
class PAC_MAN(pygame.sprite.Sprite):
    def __init__(self, s_width, s_length, s_radius):
        super().__init__()
        self.image = pygame.Surface([s_width,s_length])
        self.image.fill(YELLOW)
        pygame.draw.circle(self.image, YELLOW, (s_width // 2, s_length // 2), s_radius)

    #end procedure
#end class