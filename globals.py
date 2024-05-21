import pygame


display = None
keys = []
FPS = 60
WIDTH = 800
HEIGHT = 600
dt = 0
dt_factor = 100

def update():
    global keys
    keys = pygame.key.get_pressed()