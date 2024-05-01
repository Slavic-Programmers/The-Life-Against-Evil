import pygame
from settings import *
from player import Player
from zombie import Zombie

class Level:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        
        self.visible_sprites = pygame.sprite.Group()

        Zombie([self.visible_sprites], (100, 350))
    
    
    def run(self) -> None:
        for visible_sprite in self.visible_sprites:
            self.display_surface.blit(visible_sprite.image, visible_sprite.rect.topleft)
        self.visible_sprites.update()