import pygame
import sys
from settings import *
from player import Player

class Game:
    def __init__(self) -> None:
        self.player = Player()
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 24)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), FLAGS, BITS_PER_PIXEL)
        pygame.display.set_caption('The Life Against Evil')
        self.clock = pygame.time.Clock()
        
        self.day = 1
        
    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if pygame.QUIT == event.type:
                    pygame.quit()
                    sys.exit()
                    
            text_surface = self.font.render(f"DAY: {self.day}", True, (255, 255, 255))
            self.screen.blit(text_surface, (10, 10))
            text_surface = self.font.render(f"FOOD: {self.player.food}", True, (255, 255, 255))
            self.screen.blit(text_surface, (10, 50))
            text_surface = self.font.render(f"WATER: {self.player.water}", True, (255, 255, 255))
            self.screen.blit(text_surface, (10, 90))
            
            pygame.display.update()
            self.clock.tick(FPS)
