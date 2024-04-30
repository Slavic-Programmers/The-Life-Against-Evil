from settings import *

class Player:
    def __init__(self) -> None:
        self.is_alive = True
        self.food = 2
        self.water = 5
        self.ammo = {
            '9mm' : 20,
        }
        self.weapon = PISTOL