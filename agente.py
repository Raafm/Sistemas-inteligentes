import pygame,time,math,random
from colors import *


def contar(screen, Contador,color_square = Light_grey, color_number = Black):
    pygame.draw.rect(screen, color_square, (1170,145 ,80, 60))   
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render(str(Contador) ,True, color_number)                      
    screen.blit(text,text.get_rect(center = (1210,180)))
    pygame.display.update()


def mark(screen,node_center,color,radius=8,show=True,Time = 0):

    pygame.draw.circle(screen, color, node_center , radius)

    if show:
        pygame.display.update()
        if Time: time.sleep(Time)



def arrow(screen, start, end, lcolor = Flame, tricolor = Dark_red,  trirad= 4, thickness=3):
    pygame.draw.line(screen, lcolor, start, end, thickness)
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi/2
    rad = 180/math.pi
    pygame.draw.polygon(screen, tricolor, (
            (end[0] + trirad * math.sin(      rotation    ), end[1] + trirad * math.cos(     rotation     )),                    
            (end[0] + trirad * math.sin(rotation - 120*rad), end[1] + trirad * math.cos(rotation - 120*rad)),
            (end[0] + trirad * math.sin(rotation + 120*rad), end[1] + trirad * math.cos(rotation + 120*rad))
        )
    )
    pygame.display.update()


def distance(pos1,pos2):
    return math.hypot(pos1[0]-pos2[0], pos1[1]-pos2[1])

def versor(pos1,pos2):
    modulo = distance(pos1,pos2)
    return (pos2[0] - pos1[0])/modulo, (pos2[1] - pos1[1])/modulo

def same_pos(pos1,pos2):
    deltaX = pos1[0] - pos2[0]
    deltaY = pos1[1] - pos2[1]

    return math.hypot(deltaX, deltaY) < 10
    



step = 5

class Agent:
    

    def __init__(self, pos0 , screen, color_tail = Flame, color_head = Dark_red, step = 5):
        self.pos = pos0
        self.color_tail = color_tail
        self.color_head = color_head
        self.step = step
        self.screen = screen

    def move(self,food_pos):
        pos_antiga = self.pos
             
        Versor = versor(self.pos,food_pos) 

        self.pos = self.step * Versor[0] + pos_antiga[0] , self.step * Versor[1] + pos_antiga[1]

        arrow(self.screen, pos_antiga, self.pos,self.color_tail,self.color_head)
        time.sleep(0.001)
        
        
    


        

