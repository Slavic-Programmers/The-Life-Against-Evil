import pygame
import sys
from settings import *
from player import Player

class Game:
    def __init__(self) -> None:
        self.player = Player()
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), FLAGS, BITS_PER_PIXEL)
        pygame.display.set_caption('The Life Against Evil')
        self.clock = pygame.time.Clock()
        
    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if pygame.QUIT == event.type:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
            self.clock.tick(FPS)
