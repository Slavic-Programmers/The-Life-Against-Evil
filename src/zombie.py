import pygame
from settings import *
from utils import *

class Zombie(pygame.sprite.Sprite):
    def __init__(self, groups, position: tuple) -> None:
        super().__init__(groups)
        
        self.hp = 1

        self.animations = {
            "walk" : [],
        }

        for animation in self.animations.keys():
            animation_path = './graphics/zombie/'+animation
            self.animations[animation] = import_folder(animation_path)

        self.frame_index = 0
        self.status = 'walk'
        self.animation_speed = 0.05
        
        self.image = self.animations[self.status][int(self.frame_index)]
        self.rect = self.image.get_rect(topleft = position)
        self.hitbox = self.rect.inflate(-10, -20)        
        
    
    def animate(self) -> None:
        animation = self.animations[self.status]

        self.frame_index += 1
        self.frame_index += self.animation_speed
        
        if self.frame_index >= len(animation):
            self.frame_index = 0
            
        self.image = self.animations[self.status][int(self.frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
    
    
    def update(self) -> None:
        self.animate()