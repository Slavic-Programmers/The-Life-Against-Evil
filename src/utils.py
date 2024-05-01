import pygame
from settings import *
from os import walk, chdir
import os.path

def import_folder(path: str) -> list:
    surfaces_list = []

    file_names = next(walk(path), (None, None, []))[2]  # [] if no file
    for file_name in file_names:
        full_path = path + SLASH + file_name
        print(full_path)
        image_surface = pygame.image.load(full_path).convert_alpha()
        surfaces_list.append(image_surface)

    return surfaces_list