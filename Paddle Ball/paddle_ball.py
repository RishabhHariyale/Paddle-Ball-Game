from playsound import playsound
import pygame as pg
import sys
import time
import random

pg.init()
width=800
height=800
win=pg.display.set_mode((width,height))
clock=pg.time.Clock()
paddle=pg.rect.Rect((width/2-50,height-20,100,10))
ball=pg.Vector2((paddle.x+50,height-30))
ball_speed=pg.Vector2((10,10))
font=pg.font.Font("arial.ttf",24)
label_text=font.render("SCORE : 0",(0,0,0),(255,255,0))
label_rect=label_text.get_rect()
label_rect.center=(70,10)

font2=pg.font.Font("arial.ttf",72)
over_text=font2.render("GAME OVER",(0,0,0),(0,255,255))
over_rect=over_text.get_rect()
over_rect.center=(400,400)

speed=10
target_fps=60

def playSound():
    playsound("C:\\Users\\asus\\Downloads\Python Course with Notes\\gameover.wav")
    

def gameOver():
    win.blit(over_text,over_rect)
    pg.display.update()
    
def checkBallCollision(ball):
    global label_text,game_lost,game_score,game_started
    if ball.y<=0:
        ball_speed.y=-ball_speed.y
    if ball.x<=0 or ball.x>=width:
        ball_speed.x=-ball_speed.x
    if (ball.x>=paddle.x and ball.x<=paddle.x+100) and (ball.y>paddle.y-10):
        ball_speed.y=-ball_speed.y
    
        if game_started==True:
            game_score+=1
            label_text=font.render(f"SCORE : {game_score}",(0,0,0),(255,255,0))
            
    if ball.y+10>=height:
        game_lost=True
        gameOver()
        playSound()

last_time=time.time()
dt=0
game_started=False
game_lost=False
game_score=0


while True:
    if game_lost==True:
        pg.time.delay(3000)
        break
    new_time=time.time()
    dt=new_time-last_time
    last_time=new_time
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE and game_started==False:
                game_started=True
                ball_speed.y=-ball_speed.y
                flag=random.randint(0,1)
                ball_speed.x=random.randint(5,10)
                if flag==0:
                    ball_speed.x=-ball_speed.x

    keys=pg.key.get_pressed()
    

    if keys[pg.K_RIGHT]:
        if paddle.x+100<width:
            paddle.x+=speed*dt*target_fps
    if keys[pg.K_LEFT]:
        if paddle.x>0:
            paddle.x-=speed*dt*target_fps
    if game_started==False:
        ball.x=paddle.x+50
    else:
        ball.y+=ball_speed.y*dt*target_fps
        ball.x+=ball_speed.x*dt*target_fps

    win.fill((0,0,0))
    win.blit(label_text,label_rect)
    pg.draw.circle(win,(255,255,255),ball,10)
    pg.draw.rect(win,(255,255,255),paddle)
    checkBallCollision(ball)
    
    pg.display.update()
    clock.tick(60)
