from agente import *
from colors import *
import random,time,pygame



if __name__ == "__main__":

    # animation details:
    pygame.init()

    pygame.display.set_caption("agente simples, sem obstáculos")
    screen_height = 700
    screen_width = 1300
    screen = pygame.display.set_mode((screen_width,screen_height))

    screen.fill(Black)


    # pontos == "alimentos" comidos
    pontos = 0

    food_pos   = random.randint(50, screen_width - 150) , random.randint(50, screen_height - 50)
    food_color = Green

    mark(screen,food_pos,food_color)

    agent = Agent( pos0 = ( screen_width/2 ,  screen_height/2 ),screen = screen)

    contar(screen, pontos)

    #animation loop
    pause = True
    while True:

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                   #exit pygame,
                quit()                          #exit() program


            
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_SPACE:     #press breakspace to pause or play
                    pause = not pause   
                    time.sleep(0.2)
        
        if pause:
            continue

        if same_pos(food_pos , agent.pos):
            pygame.draw.rect(screen,Black,(20,20,screen_width-20,screen_height-20))
            food_pos = random.randint(50, screen_width - 150) , random.randint(50, screen_height - 50)
            mark(screen,food_pos,food_color)
            pontos+=1
            contar(screen, pontos)
           
        
        agent.move(food_pos)