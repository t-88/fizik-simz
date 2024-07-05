import pygame
import math
import globals as g

class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__



player = dotdict({
    "r" : 20,
    "color": (255,255,255),
    "pos": dotdict({"x": 100,"y":100}),
    "ppos": dotdict({"x": 100,"y":100}),
    "acc": dotdict({"x": 0,"y":0}),
})


anchor = dotdict({"pos":dotdict({"x": 200, "y" : 50})})

def init():
    pass
def run():
    if pygame.mouse.get_pressed()[0]:
        anchor.pos.x = pygame.mouse.get_pos()[0]
        anchor.pos.y = pygame.mouse.get_pos()[1]

    player.acc.y = 0 
    player.acc.y = 1 

    if math.sqrt((player.pos.x - anchor.pos.x) ** 2 + (player.pos.y - anchor.pos.y) ** 2) > 200:
        offset = math.sqrt((player.pos.x - anchor.pos.x) ** 2 + (player.pos.y - anchor.pos.y) ** 2) - 200 
        dir =  pygame.Vector2(player.pos.x - anchor.pos.x,player.pos.y - anchor.pos.y).normalize()
        player.pos.x -= dir.x * offset
        player.pos.y -= dir.y * offset

    ppos = dotdict({"x":player.pos.x,"y":player.pos.y})

    player.pos.x += player.pos.x - player.ppos.x + player.acc.x 
    player.pos.y += player.pos.y - player.ppos.y + player.acc.y 

    player.ppos.x = ppos.x    
    player.ppos.y = ppos.y   



    g.display.fill((18,18,18,18))
    pygame.draw.circle(g.display,player.color,(player.pos.x,player.pos.y),player.r)
    pygame.draw.circle(g.display,(255,0,255),(anchor.pos.x,anchor.pos.y),5)
    pygame.draw.line(g.display,(255,0,255),(player.pos.x,player.pos.y),(anchor.pos.x,anchor.pos.y),5)
    
    pygame.display.flip()
