import pygame
from defs import * 
from pipe import PipeCollection

def update_label(data,title,font,x,y,gameDisplay):
    label=font.render('{} {}'.format(title,data),1,DATA_FONT_COLOR) #1 - anti-aliasing
    gameDisplay.blit(label,(x,y))
    return y 

def update_data_labels(gameDisplay,dt,game_time,font):
    y_pos=20
    gap=20
    x_pos=10
    y_pos=update_label(round(1000/dt,2),'FPS',font,x_pos,y_pos+gap,gameDisplay)
    y_pos=update_label(round(game_time/1000,2),'Game time',font,x_pos,y_pos+gap,gameDisplay)


def run_game():
    pygame.init()
    gameDisplay=pygame.display.set_mode((DISPLAY_W,DISPLAY_H))
    pygame.display.set_caption("FLAPPY AI")

    running=True
    bgImg=pygame.image.load(r'C:\Program Files\Python310\1_Python_programmes\neuro\Flappybirdai\BG.png') 
    label_font=pygame.font.SysFont('monospace', DATA_FONT_SIZE)
    pipes=PipeCollection(gameDisplay)
    pipes.create_new_set()

    clock=pygame.time.Clock()
    dt=0
    game_time=0   

    while running:
        
        dt=clock.tick(FPS)
        game_time+=dt

        gameDisplay.blit(bgImg,(0,0))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.KEYDOWN:
                running=False
        update_data_labels(gameDisplay,dt,game_time,label_font)
        pipes.update(dt)

        pygame.display.update()

if __name__=='__main__':
    run_game()