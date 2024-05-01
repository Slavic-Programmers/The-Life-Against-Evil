from settings import *
from utils import *

class Zombie:
    def __init__(self) -> None:
        self.hp = 1

        self.animations = {
            "walk" : [],
        }
        
        for animation in self.animations.keys():
            self.animations[animation] = import_folder('./graphics/zombie_walk')
