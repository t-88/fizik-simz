import pygame
import math
import globals as g

pygame.init()
g.display = pygame.display.set_mode((g.WIDTH,g.HEIGHT))
pygame.display.set_caption("Fighters")
g.clock = pygame.Clock()


class Point:
    def __init__(self,x,y,pin = False):
        self.pos = pygame.Vector2(x,y)
        self.prev_pos = pygame.Vector2(x,y)
        self.pin = pin
        self.is_selected = False
        self.dead = False
    def render(self):
        if self.pin:
            pygame.draw.circle(g.display,0xFF00FF,self.pos,2)
        else:
            if self.is_selected:
                pygame.draw.circle(g.display,0xFF0000,self.pos,2)
            else:
                pygame.draw.circle(g.display,0xFFFFFF,self.pos,2)
                
                            

class Stick:
    def __init__(self,p1,p2,length):
        self.p1 = p1
        self.p2 = p2
        self.length = length
    def render(self):
        # self.p1.render()
        # self.p2.render()
        if self.p1.is_selected or self.p2.is_selected:
            pygame.draw.line(g.display,0xFF0000,self.p1.pos,self.p2.pos)
        else:
            pygame.draw.line(g.display,0xFFFFFF,self.p1.pos,self.p2.pos)



points = [
]
sticks = [ 
]


spacing = 20
for y in range(32,g.HEIGHT // 2,spacing):
    for x in range(32,g.WIDTH - 32,spacing):
            points.append(Point(x,y,y == 32))
            if x != 32:
                sticks.append(Stick(points[-1],points[-2],spacing))
            if y != 32:
                sticks.append(Stick(points[-1],points[-38],spacing))


MOUSE_RADUIS = 50
is_running = True
while is_running:
    mouse_prev = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            is_running = False
            break
    
    g.dt =  g.clock.tick(g.FPS) * (g.dt_factor / 1000)
    g.update()
    
    
    force = pygame.Vector2(0,0.2)
    acc = force
    
    
    for i in range(len(points) - 1, -1, -1):
        points[i].is_selected = points[i].pos.distance_to(pygame.mouse.get_pos()) < MOUSE_RADUIS
        if pygame.mouse.get_pressed(3)[2] and points[i].is_selected:
            points[i].dead = True
            points.pop(i)
    
    for point in points:
        if point.pin: continue
        if point.dead: continue
        
        if pygame.mouse.get_pressed(3)[0] and point.is_selected:
            diff = pygame.Vector2(pygame.mouse.get_pos()[0] - mouse_prev[0],pygame.mouse.get_pos()[1] - mouse_prev[1])
            # if diff.x > 5: diff.x = 5
            # if diff.y > 5: diff.y = 5
            # if diff.x < -5:  diff.x = -5
            # if diff.y < -5:  diff.y = -5            
            
            point.prev_pos = point.pos - diff            

        
        prev_pos = point.pos.copy()
        
        
        
        point.pos.x = 2 * point.pos.x - point.prev_pos.x + acc.x * g.dt**2  
        point.pos.y = 2 * point.pos.y - point.prev_pos.y + acc.y * g.dt**2  
        point.prev_pos = prev_pos

        if point.pos.x > g.WIDTH - 6:
            point.pos.x = g.WIDTH - 6
        elif point.pos.x < 0:
            point.pos.x = 0

        if point.pos.y > g.HEIGHT - 6:
            point.pos.y = g.HEIGHT - 6
        elif point.pos.y < 0:
            point.pos.y = 0

        
            
    for stick in sticks:
        if stick.p1.dead or stick.p2.dead: continue
        diff = stick.p1.pos - stick.p2.pos
        diff_factor = (stick.length - stick.p1.pos.distance_to(stick.p2.pos)) / stick.p1.pos.distance_to(stick.p2.pos) * 0.5
        offset = pygame.Vector2(diff.x * diff_factor,diff.y * diff_factor)
        
        if stick.p1.pin:
            stick.p2.pos.x -= offset.x * 2
            stick.p2.pos.y -= offset.y * 2
        elif stick.p2.pin:
            stick.p1.pos.x += offset.x * 2
            stick.p1.pos.y += offset.y * 2
        else:
            stick.p1.pos.x += offset.x
            stick.p1.pos.y += offset.y
            stick.p2.pos.x -= offset.x 
            stick.p2.pos.y -= offset.y 
            
        
    
    
    for stick in sticks:
        if stick.p1.dead or stick.p2.dead: continue
        
        stick.render()
    
        
    pygame.display.flip()                 
    g.display.fill(0x181818)

pygame.quit()