import pygame as pg
import random
import sys

class Screen:
    def __init__(self, title, wh, img_path):
        pg.display.set_caption(title) 
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(img_path)
        self.bgi_rct = self.bgi_sfc.get_rect() 

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class character:
    def __init__(self, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, (255,0,0), (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = 80
        self.rct.centery = 700
        # self.rct.centerx = random.randint(0, scr.rct.width)
        # self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)
        
class Boss:
    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen):
        self.blit(scr)  


def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    # if obj_rct.left < boss_rct.left or boss_rct.right < obj_rct.right:
    #     yoko = -1
    # if obj_rct.top < boss_rct.top or boss_rct.bottom < obj_rct.bottom:
    #     tate = -1
    
    return yoko, tate

def main():
    clock = pg.time.Clock()

    # タイトルの設定
    scr = Screen("test game", (500,900), "groupe/fig/pg_bg.jpg")
    vx = random.choice([-1, +1])
    vy = random.choice([-1, +1])
    chara = character(20, (vx, vy), scr)
    boss = Boss("groupe/fig/boss.png", 0.4, (250,200))
    
    while True:        
        scr.blit()
        boss.update(scr)
        chara.update(scr)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # if chara.rct.colliderect(boss.rct):
        #     chara.update(boss, scr)
            
        
        pg.display.update()
        clock.tick(500)
        
        
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()