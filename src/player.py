from settings import *

class Player:
    def __init__(self) -> None:
        self.hp = 100
        self.food = 5
        self.water = 5
        self.ammo = {
            '9mm' : 20,
        }
        self.weapon = PISTOL