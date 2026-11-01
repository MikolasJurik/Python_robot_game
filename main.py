import pygame
import random

import sys
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Ostrava:

    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont("Arial", 30)
        pygame.display.set_caption("Ostrava")
        self.screen = pygame.display.set_mode((1000, 480))
        self.clock = pygame.time.Clock()
        self.load_images()
        self.coins = 0
        self.old_coins = self.coins
        self.lives = 25




#ROBOT MOVEMENT
        self.x = 856/2
        self.y = 480/2
        self.left = False
        self.right = False
        self.Upp = False
        self.Down = False

# MONSTERS
#M1
        self.m1_x = 50
        self.m1_y = 50
        self.speed_m1_x = 1
        self.speed_m1_y = 2
#M2      

        self.m2_x = 500
        self.m2_y = 200
        self.speed_m2_x = 2
        self.speed_m2_y = 1
#M3

        self.m3_x = random.choice([0,1000-self.images[2].get_width()])
        self.m3_y = random.choice([0,480-self.images[2].get_height()])
        self.speed_m3_x = 2
        self.speed_m3_y = 3
#M4

        self.m4_x = random.choice([0,1000-self.images[2].get_width()])
        self.m4_y = random.choice([0,480-self.images[2].get_height()])
        self.speed_m4_x = 2
        self.speed_m4_y = 5
#M5

        self.m5_x = random.choice([0,1000-self.images[2].get_width()])
        self.m5_y = random.choice([0,480-self.images[2].get_height()])
        self.speed_m5_x = 2
        self.speed_m5_y = 5

# COiNS 
        self.c_x = random.randint(0+self.images[2].get_width(),1000-self.images[2].get_width()) 
        self.c_y = random.randint(0,450-self.images[2].get_width())

        self.end = False
        self.main_loop()



    def load_images(self):
        self.images = []
        for i in ["coin", "door", "monster", "robot"]:
            self.images.append(
                pygame.image.load(resource_path(i + ".png"))
            )

    def main_loop(self):
        while True:
            self.draw_screen()
            self.monsters()
            self.handle_events()
            self.movement()
            self.end_game()


    def handle_events(self):
        for event in pygame.event.get():
        # KEYBOARD
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.left = True
                if event.key == pygame.K_RIGHT:
                    self.right = True
                if event.key == pygame.K_DOWN:
                    self.Down = True
                if event.key == pygame.K_UP:
                    self.Upp = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.left = False
                if event.key == pygame.K_RIGHT:
                    self.right = False
                if event.key == pygame.K_DOWN:
                    self.Down = False
                if event.key == pygame.K_UP:
                    self.Upp = False
            if event.type == pygame.QUIT:
                sys.exit()
            
    def movement(self):
        if self.coins < 10:
            robots_speed = 2
        elif self.coins < 20:
            robots_speed = 3
        elif self.coins < 30:
            robots_speed = 4
        elif self.coins < 40:
            robots_speed = 5
        elif self.coins < 50:
            robots_speed = 6
        elif self.coins < 60:
            robots_speed = 7
        else: 
            robots_speed = 10
        if self.left and self.x >= 0:
            self.x -= robots_speed
        if self.right and self.x + self.images[3].get_width()<= 1000:
            self.x += robots_speed
        if self.Upp and  self.y >= 0:
            self.y -= robots_speed
        if self.Down and self.y + self.images[3].get_height()<= 480:
            self.y += robots_speed

    def monsters(self):
# MONSTER n.1
        self.m1_x += self.speed_m1_x
        self.m1_y += self.speed_m1_y
        if self.m1_y + self.images[2].get_height() >=480:
            self.speed_m1_y = -2
        if self.m1_y <= 0:
            self.speed_m1_y =2
        if self.m1_x + self.images[2].get_width() >= 1000:
            self.speed_m1_x = -1
        if self.m1_x <= 0:
            self.speed_m1_x = 1

#Monster n.2
        self.m2_x += self.speed_m2_x
        self.m2_y += self.speed_m2_y
        if self.m2_y + self.images[2].get_height() >=480:
            self.speed_m2_y = -2
        if self.m2_y <= 0:
            self.speed_m2_y =2
        if self.m2_x + self.images[2].get_width() >= 1000:
            self.speed_m2_x = -1
        if self.m2_x <= 0:
            self.speed_m2_x = 1

# MONSTER 3
        if self.coins > 10:
            self.m3_x += self.speed_m3_x
            self.m3_y += self.speed_m3_y
            if self.m3_y + self.images[2].get_height() >=480:
                self.speed_m3_y = -2
            if self.m3_y <= 0:
                self.speed_m3_y = 2
            if self.m3_x + self.images[2].get_width() >= 1000:
                self.speed_m3_x = -2
            if self.m3_x <= 0:
                self.speed_m3_x = 2

# Monster 4 
        if self.coins>20:
            self.m4_x += self.speed_m4_x
            self.m4_y += self.speed_m4_y
            if self.m4_y + self.images[2].get_height() >=480:
                self.speed_m4_y = -3
            if self.m4_y <= 0:
                self.speed_m4_y = 3
            if self.m4_x + self.images[2].get_width() >= 1000:
                self.speed_m4_x = -2
            if self.m4_x <= 0:
                self.speed_m4_x = 2
# Monster 5
        if self.coins > 30:
            self.m5_x += self.speed_m5_x
            self.m5_y += self.speed_m5_y
            if self.m5_y + self.images[2].get_height() >=480:
                self.speed_m5_y = -random.randint(-2,6)
            if self.m5_y <= 0:
                self.speed_m5_y = random.randint(-2,2)
            if self.m5_x + self.images[2].get_width() >= 1000:
                self.speed_m5_x = -random.randint(-2,6)
            if self.m5_x <= 0:
                self.speed_m5_x = random.randint(-2,6)


    def end_game(self):
        if self.lives <=0:
            self.end = True

        if self.m1_x - self.images[2].get_width() < self.x < self.m1_x+ self.images[2].get_width() and self.m1_y - self.images[2].get_height() < self.y < self.m1_y+ self.images[2].get_height() or self.end == True:
            self.lives -=1
            if self.lives <=0:
                self.end = True
                self.screen.fill((0, 0, 0))
                text1 = "You DIED!"
                text2 = f"You managed to collect {self.coins} coins"
                text3 = "REPLAY"
                text4 = "QUIT"
                render1_x,render1_y = self.font.size(text1)
                render2_x,render2_y = self.font.size(text2)
                render3_x,render3_y = self.font.size(text3)
                render4_x,render4_y = self.font.size(text4)


                died = self.font.render(f"YOU DIED!", True,(255,0,0))
                if self.coins == 1:
                    final_score = self.font.render(f"You managed to collect {self.coins} coin",True,(255,0,0))
                else :
                    final_score = self.font.render(f"You managed to collect {self.coins} coins",True,(255,0,0))
                replay = self.font.render("REPLAY", True,(255,247,0) )
                push_button_replay = replay.get_rect(topleft=((1000-render3_x)//2, (600-render3_y)//2))

                quit = self.font.render("QUIT", True,(255,247,0) )
                push_button_quit = replay.get_rect(topleft=((1000-render4_x)//2, (700-render4_y)//2))

                self.screen.blit(died,((1000-render1_x)//2, (380-render1_y)//2))
                self.screen.blit(final_score,((1000-render2_x)//2, (480-render2_y)//2))
                self.screen.blit(replay,((1000-render3_x)//2, (600-render3_y)//2))
                self.screen.blit(quit,((1000-render4_x)//2, (700-render4_y)//2))


                pygame.display.flip()
                while True:
                    for i in pygame.event.get():
                        if i.type == pygame.MOUSEBUTTONDOWN:
                            if push_button_replay.collidepoint(i.pos):
                                Ostrava()
                            elif push_button_quit.collidepoint(i.pos):
                               sys.exit()
                        if i.type == pygame.QUIT:
                                        sys.exit()



        if self.m2_x - self.images[2].get_width() < self.x < self.m2_x+ self.images[2].get_width() and self.m2_y - self.images[2].get_height() < self.y < self.m2_y+ self.images[2].get_height():
            self.lives -= 1
        if self.coins > 10:
            if self.m3_x - self.images[2].get_width() < self.x < self.m3_x+ self.images[2].get_width() and self.m3_y - self.images[2].get_height() < self.y < self.m3_y+ self.images[2].get_height():
                    self.lives -=1
        if self.coins>20:
            if self.m4_x - self.images[2].get_width() < self.x < self.m4_x+ self.images[2].get_width() and self.m4_y - self.images[2].get_height() < self.y < self.m4_y+ self.images[2].get_height():
                    self.lives -=1
        if self.coins > 30:
            if self.m5_x - self.images[2].get_width() < self.x < self.m5_x+ self.images[2].get_width() and self.m5_y - self.images[2].get_height() < self.y < self.m5_y+ self.images[2].get_height():
                    self.lives -=1
    

    def draw_screen(self):
        if self.end == False:
            if self.coins <= 10:
                self.screen.fill((252, 252, 252))
            elif self.coins <= 20:
                self.screen.fill((107, 255, 255))
            elif self.coins <= 30:
                self.screen.fill((235,235,235))
            elif self.coins <= 40:
                self.screen.fill((255,57,57)) 
            else:        
                self.screen.fill((0, 0, 0))


            
            self.screen.blit(self.images[3], (self.x, self.y))
            self.screen.blit(self.images[2], (self.m1_x,self.m1_y))
            self.screen.blit(self.images[2], (self.m2_x,self.m2_y))
            if self.coins > 10:
                self.screen.blit(self.images[2], (self.m3_x,self.m3_y))
            if self.coins > 20:
                self.screen.blit(self.images[2], (self.m4_x,self.m4_y))
            if self.coins > 30:
                self.screen.blit(self.images[2], (self.m5_x,self.m5_y))
                
            current_score = self.font.render(f"Coins: {self.coins}",True,(0,0,0))

            current_lives = self.font.render(f"Lives: {self.lives}", True,(0,0,0))
            if self.coins>40:
                current_lives = self.font.render(f"Lives: {self.lives}", True,(255,0,0))
                current_score = self.font.render(f"Coins: {self.coins}",True,(255,0,0))
            self.screen.blit(current_lives, (0,50))
            self.screen.blit(current_score,(0,0))


# COINS RE-SPAWN
            if not (self.c_x - self.images[2].get_width() < self.x < self.c_x+ self.images[2].get_width() and self.c_y - self.images[2].get_height() < self.y < self.c_y+ self.images[2].get_height()):
                self.screen.blit(self.images[0], (self.c_x,self.c_y))
            if self.c_x - self.images[2].get_width() < self.x < self.c_x+ self.images[2].get_width() and self.c_y - self.images[2].get_height() < self.y < self.c_y+ self.images[2].get_height():
                self.coins +=1
                self.c_x = random.randint(0+self.images[2].get_width(),1000-self.images[2].get_width())
                self.c_y = random.randint(0,450-self.images[2].get_width()) 
                self.screen.blit(self.images[0], (self.c_x, self.c_y))



        

        self.clock.tick(100)
        pygame.display.flip()



Ostrava()

        















    
