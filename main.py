import pygame
import math
import globals as g
import cloth_demo
import pendulum_demo


pygame.init()
g.display = pygame.display.set_mode((g.WIDTH,g.HEIGHT))
pygame.display.set_caption("Fisiks")
g.clock = pygame.Clock()




demo = pendulum_demo


demo.init()

is_running = True
while is_running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            is_running = False
            break
    
    g.dt =  g.clock.tick(g.FPS) / (1000 / g.FPS) 

    demo.run()