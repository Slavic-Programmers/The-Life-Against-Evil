import pygame
import sys
from settings import *
from level import Level
from player import Player
from zombie import Zombie

class Game:
    def __init__(self) -> None:
        self.player = Player()
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('Arial', 24)
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), FLAGS, BITS_PER_PIXEL)
        pygame.display.set_caption('The Life Against Evil')
        self.clock = pygame.time.Clock()
    
        self.level = Level()

        self.day = 1    
    
    def run(self) -> None:
        self.background = pygame.transform.scale(pygame.image.load('./graphics/background/background.png'), (WIDTH, HEIGHT))
        pygame.mouse.set_visible(False)
        cursor_image = pygame.transform.scale(pygame.image.load('./graphics/cursor/grabbing.png').convert_alpha(), (50, 50))
        cursor_image_rect = cursor_image.get_rect()
        
        while True:
            for event in pygame.event.get():
                if pygame.QUIT == event.type:
                    pygame.quit()
                    sys.exit()
                
            self.screen.blit(self.background, (0, 0))
            
            self.__render_player_inventory()
            
            cursor_image_rect.center = pygame.mouse.get_pos()
            self.screen.blit(cursor_image, cursor_image_rect)
            
            self.level.run()
            
            pygame.display.update()
            self.clock.tick(FPS)


    def __render_player_inventory(self) -> None:
        self.font.set_bold(True)
        text_surface = self.font.render(f"DAY: {self.day}", True, WHITE)
        self.screen.blit(text_surface, (10, 10))
        food_color = WHITE if self.player.food > 5 else (ORANGE if 3 <= self.player.food <= 5 else RED)
        text_surface = self.font.render(f"FOOD: {self.player.food}", True, food_color)
        self.screen.blit(text_surface, (10, 50))
        water_color = WHITE if self.player.water > 5 else (ORANGE if 3 <= self.player.food <= 5 else RED)
        text_surface = self.font.render(f"WATER: {self.player.water}", True, water_color)
        self.screen.blit(text_surface, (10, 90))
        self.font.set_bold(False)