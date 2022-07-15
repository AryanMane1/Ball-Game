import pygame
from pygame.locals import *
import sys
import pygame.display
import pygame.event
import pygame.time
import pygame.draw
import pygame.font
import pygame.mixer
import pygame.image
import pygame.mouse
import pygame.key
import pygame.transform
import random
import os
import tkinter 
import tkinter.messagebox

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class Set:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT))
        pygame.display.set_caption("Ball game by Aryan")

    def text(self,text,font_size,colour,x,y):
        '''
        text,font_size,colour,x,y
        '''
        font = font = pygame.font.SysFont(None, font_size)
        TEXT = font.render(text,True,colour)
        self.screen.blit(TEXT,[x,y])

    def read_file(self):
        global high_score
        if os.path.exists("game_info.txt") == False:
            with open("game_info.txt",'w') as f:
                f.write("0")

        with open("game_info.txt",'r') as f:
            high_score = int(f.readline())
            
    def main_game(self):
        global heart_num,Score,heart_num,high_score

        all_coin = []
        all_coin_bag = []
        all_nail = []
        all_fires = []
        all_hearts=[]
        Player_x = 0
        Player_y = SCREEN_HIGHT-100
        img_Y = 0
        time_cut = 0
        bounce_time = 0
        bounce = False
        Score = 0
        player_H = Player_img.get_height()
        player_W = Player_img.get_width()

        coin_H = get_coin_img.get_height()
        coin_W = get_coin_img.get_width()

        bag_H = coin_bag_img.get_height()
        bag_W = coin_bag_img.get_width()

        nail_H = nail_img.get_height()
        nail_W = nail_img.get_width()

        fire_H = fire_img.get_height()
        fire_W = fire_img.get_width()
        accL = 0
        accR = 0
        heart_num = 3

        self.read_file()

        while True:
            if heart_num == 0:
                Game.game_over()
            else:
                Game.screen.blit(back_img,(0,0))
                for env in pygame.event.get():
                    if env.type == QUIT:
                        pygame.quit()
                        sys.exit()
                Key = pygame.key.get_pressed()
                if Key[K_LEFT]:
                    if 0< Player_x <5:
                        Player_x+=20
                    if Player_x>5:
                        accR=0
                        Player_x-=7+accL
                        accL+=0.4
                elif Key[K_RIGHT]:
                    if SCREEN_WIDTH-5 < Player_x < SCREEN_WIDTH:
                        Player_x-=20
                    if Player_x<SCREEN_WIDTH-80:
                        accL=0
                        Player_x+=7+accR
                        accR+=0.4
                elif Player_y+Player_img.get_height()<SCREEN_HIGHT: 
                        Player_y+=10
                #------------------  
                if time_cut%37 == 0 or time_cut%30 == 0: 
                    all_coin.append([random.randint(40,SCREEN_WIDTH-40),0])
                if time_cut%73 == 0 or time_cut%89 == 0: 
                    all_coin_bag.append([random.randint(40,SCREEN_WIDTH-40),0])
                if time_cut%246 == 0 or time_cut%186 == 0: 
                    all_nail.append([random.randint(40,SCREEN_WIDTH-40),0])
                if time_cut%288 == 0 or time_cut%303 == 0: 
                    all_fires.append([random.randint(40,SCREEN_WIDTH-40),0])
                if time_cut%1000 == 0 and time_cut!=0: 
                    all_hearts.append([random.randint(40,SCREEN_WIDTH-40),0])
                Speed_Y = 5
                Extra_x = 30
                # Placing coins,coins_bag,nail
                for c in all_hearts:
                    Game.screen.blit(heart_img,(c[0],c[1]))
                    c[1]+=Speed_Y
                    if c[1] > SCREEN_HIGHT:
                        all_hearts.remove(c)
                    Check_Y = Player_y+10 < ( c[1]+heart_img.get_height() ) < Player_y + player_H
                    Check_X = Player_x+10 < (c[0]+heart_img.get_width()) < Player_x + player_W+Extra_x
                    if Check_X and Check_Y:
                        all_hearts.remove(c)
                        heart_num+=1
                for c in all_coin:
                    Game.screen.blit(get_coin_img,(c[0],c[1]))
                    c[1]+=Speed_Y
                    if c[1] > SCREEN_HIGHT:
                        all_coin.remove(c)
                    Check_Y = Player_y+10 < ( c[1]+coin_H ) < Player_y + player_H
                    Check_X = Player_x+10 < (c[0]+coin_W) < Player_x + player_W+Extra_x
                    if Check_X and Check_Y:
                        all_coin.remove(c)
                        Score+=10
                        get_coin_sound.set_volume(0.5)
                        get_coin_sound.play()

                for c in all_coin_bag:
                    Game.screen.blit(coin_bag_img,(c[0],c[1]))
                    c[1]+=Speed_Y
                    if c[1] > SCREEN_HIGHT:
                        all_coin_bag.remove(c)
                    Check_Y = Player_y-10 < ( c[1]+bag_H ) < Player_y + player_H
                    Check_X = Player_x-10 < (c[0]+bag_W) < Player_x + player_W+Extra_x
                    if Check_X and Check_Y:
                        all_coin_bag.remove(c)
                        Score+=100
                        get_coin_sound.set_volume(0.5)
                        get_coin_sound.play()

                for c in all_nail:
                    Game.screen.blit(nail_img,(c[0],c[1]))
                    c[1]+=Speed_Y
                    if c[1] > SCREEN_HIGHT:
                        all_nail.remove(c)
                    Check_Y = Player_y+10 < ( c[1]+nail_H) < Player_y + player_H
                    Check_X = Player_x+10 < (c[0]+nail_W) < Player_x + player_W+Extra_x
                    if Check_X and Check_Y:
                        all_nail.remove(c)
                        heart_num-=1
                        lose_heart_sound.set_volume(1)
                        lose_heart_sound.play()
                for c in all_fires:
                    Game.screen.blit(fire_img,(c[0],c[1]))
                    c[1]+=Speed_Y
                    if c[1] > SCREEN_HIGHT:
                        all_fires.remove(c)
                    Check_Y = Player_y+10 < ( c[1]+fire_H) < Player_y + player_H
                    Check_X = Player_x+10 < (c[0]+fire_W) < Player_x + player_W+Extra_x
                    if Check_X and Check_Y:
                        all_fires.remove(c)
                        heart_num-=1
                        lose_heart_sound.set_volume(1)
                        lose_heart_sound.play()
                heart_X = 0
                for i in range(1,heart_num+1):
                    Game.screen.blit(heart_img,(heart_X,0))
                    heart_X+=30
                Game.text(f"Score: {Score}",30,black,SCREEN_WIDTH-130,10)
                Game.text(f"High Score: {high_score}",30,black,SCREEN_WIDTH-150,35)

                if Score >= high_score:
                    high_score = Score
            
                time_cut+=1
                Game.screen.blit(Player_img,(Player_x,Player_y))
                pygame.display.update()
                CLOCK.tick(fps)

    def game_over(self):
        continue_Y = 450
        Message_UP = True
        Message_DOWN = True
        game_over_sound.play()
        with open("game_info.txt",'r') as f:
                real_high = int(f.readline())
        with open("game_info.txt",'w') as f:
            if Score > real_high:
                f.write(str(Score))
            else:
                f.write(str(high_score))

        self.read_file()

        while True:
            self.screen.blit(back_img,(0,0))

            for env in pygame.event.get():
                if env.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if env.type == MOUSEBUTTONDOWN:
                    self.main_game()

            self.text(f"Your Score: {Score}",40,black,50,150)
            self.text(f"High Score: {high_score}",40,black,50,210)

            if continue_Y >= 470:
                Message_UP = True
                Message_DOWN = False
                
            if continue_Y <= 400:
                Message_UP = False
                Message_DOWN = True

            if Message_UP:continue_Y-=3

            elif Message_DOWN:continue_Y+=3

            else:continue_Y+=3

            self.text(f"!! Click here to continue !!",45,black,10,continue_Y)
            self.screen.blit(gameover_img,(50,0))
            pygame.display.update()
            CLOCK.tick(fps)
            


if __name__ == '__main__':
    SCREEN_WIDTH = 400  
    SCREEN_HIGHT = 500
    
    Game = Set()
    # Sounds
    get_coin_sound = pygame.mixer.Sound('sounds/getcoin.mp3')
    lose_heart_sound = pygame.mixer.Sound('sounds/loseheart.mp3')
    game_over_sound = pygame.mixer.Sound('sounds/gameover.mp3')
    # Images
    ball2 = pygame.transform.scale(pygame.image.load("images/smily.png").convert_alpha(),(80,80))
    ball3 = pygame.transform.scale(pygame.image.load("images/ball3.png").convert_alpha(),(70,70))
    ball4 = pygame.transform.scale(pygame.image.load("images/ball4.png").convert_alpha(),(70,70))
    ball5 = pygame.transform.scale(pygame.image.load("images/football.png").convert_alpha(),(70,70))
    
    back_img = pygame.transform.scale(pygame.image.load("images/back.jpg").convert_alpha(),(SCREEN_WIDTH,SCREEN_HIGHT))

    get_coin_img = pygame.transform.scale(pygame.image.load("images/coin2.png").convert_alpha(),(30,30))
    coin_bag_img = pygame.transform.scale(pygame.image.load("images/coins.png").convert_alpha(),(50,50))
    fire_img = pygame.transform.scale(pygame.image.load("images/fireball.png").convert_alpha(),(30,40))
    nail_img = pygame.transform.scale(pygame.image.load("images/nail.png").convert_alpha(),(15,40))
    heart_img = pygame.transform.scale(pygame.image.load("images/heart.png").convert_alpha(),(30,30))
    gameover_img = pygame.transform.scale(pygame.image.load("images/gameover.png").convert_alpha(),(300,100))

    Player_img = random.choice([ball2,ball3,ball4,ball5])
    heart_num = 3
    fps = 30
    CLOCK = pygame.time.Clock()

    Game.main_game()