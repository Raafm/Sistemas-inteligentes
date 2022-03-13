import pygame,time,random
from color import *
#from graph.points import pointsMany as points
from twoD_tree import points,root
import math

screen_width,screen_height = 1200,700
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill(Black)
if __name__ == "__main__":
    pygame.init()

    N = 50
    Max_width  = screen_width  - 100
    Max_height = screen_height - 100

#points = list( (random.randint(50,Max_width),random.randint(50,Max_height)) for _ in range(N))


def print_point(position, color= White,radius = 4, index=-1,show = True):
    pygame.draw.circle(screen,color,position,radius)
    if index > -1:
        font = pygame.font.Font('freesansbold.ttf',14)
        text = font.render( str(index),True, White)    
        screen.blit(text,text.get_rect(center = position))
    
    if show: pygame.display.update()


def print_lines(pos,orientation,X0 = 10,Y0 = 10,X1 = screen_width-200,Y1 = screen_height-50,show= True):
    x,y = pos

    if orientation: pygame.draw.line(screen,Cyan,(X0,y),(X1,y))
    else:           pygame.draw.line(screen,Red ,(x,Y0),(x,Y1))
    if show: pygame.display.update()


class rectangle:
    
    def __init__(self,x,y,width=250,height=140):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self,display = True,color = Dark_yellow):
        pygame.draw.rect(screen,color,(1+self.x,1+self.y,self.width,self.height))
        if display: pygame.display.update()

    # left: -1, inside: 0, right: 1,
    # up:   -1, inside: 0, down:  1,
    # orientation == 0: horizontal, 
    # orientation == 1: vertical
    def compare_position(self,point,orientation)->int:
        xP,yP = point
        if orientation == 0:
            return int(self.x < xP) - int(self.x + self.width  > xP ) 
        if orientation == 1:
            return int(self.y < yP) - int(self.y + self.height > yP )    
    
    def extremes(self):

        xL,xR = self.x,self.x + self.width
        yD,yU = self.y,self.y + self.height
        return xL,xR,yU,yD


def arrow(screen, start, end, lcolor = Light_grey, tricolor = Black,  trirad= 4, thickness=2,show = True):
    pygame.draw.line(screen, lcolor, start, end, thickness)
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi/2
    rad = 180/math.pi
    pygame.draw.polygon(screen, tricolor, (
            (end[0] + trirad * math.sin(      rotation    ), end[1] + trirad * math.cos(     rotation     )),                    
            (end[0] + trirad * math.sin(rotation - 120*rad), end[1] + trirad * math.cos(rotation - 120*rad)),
            (end[0] + trirad * math.sin(rotation + 120*rad), end[1] + trirad * math.cos(rotation + 120*rad))
        )
    )
    if show: pygame.display.update()


def range_count(cur,xL,xR,yU,yD,vertical,lines = False,delay=0.2):
    if cur is None: return 0
    if lines: print_lines((cur.x,cur.y),vertical)

    print_point((cur.x,cur.y),color = Lime,radius=9)
    time.sleep(delay)

    if vertical:
        if   cur.y < yD: return range_count(cur.right ,xL,xR,yU,yD,False,delay=delay)
        elif cur.y < yU: 
            if ((xL < cur.x) and (cur.x < xR)) :print_point((cur.x,cur.y),color = Yellow, radius = 10)
            Im_in = int ((xL < cur.x) and (cur.x < xR)) 
            return Im_in + range_count(cur.left  ,xL,xR,yU,yD,False,delay=delay) + range_count(cur.right ,xL,xR,yU,yD,False,delay=delay)
        else:            return range_count(cur.left  ,xL,xR,yU,yD,False,delay=delay)
    else:
        if   cur.x < xL: return range_count(cur.right ,xL,xR,yU,yD,True,delay=delay)
        elif cur.x < xR: 
            if ((yD < cur.y) and (cur.y < yU)):print_point((cur.x,cur.y),color = Yellow, radius = 10)
            Im_in = int((yD < cur.y) and (cur.y < yU))
            return Im_in + range_count(cur.left  ,xL,xR,yU,yD,True,delay=delay) + range_count(cur.right ,xL,xR,yU,yD,True,delay=delay)
        else:            return range_count(cur.left  ,xL,xR,yU,yD,True,delay=delay)
    

##### MAIN #####
