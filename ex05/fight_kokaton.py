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


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, img_path, ratio, xy):
        self.sfc = pg.image.load(img_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]  
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)                    


class Bomb:
    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


def check_bound(obj_rct, scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    clock =pg.time.Clock()
    cnt = 0
    time_cnt = 10
    
    fonto = pg.font.Font(None,100)
    fonto.set_bold
    
    gc_txt = fonto.render("GAME CLEAR!", True, (255,0,0))
    go_txt = fonto.render("GAME OVER...", True, (255,0,0))
    

    scr = Screen("負けるな！こうかとん", (1600,900), "ex05/fig/pg_bg.jpg")
    
    kkt = Bird("ex05/fig/6.png", 2.0, (900,400))
    kkt.update(scr)
    
    bombs = []
    colors = ["red","blue","yellow","green"]
    for color in colors:
        vx = random.choice([-1, +1])
        vy = random.choice([-1, +1])
        bombs.append(Bomb(color, 10, (vx, vy), scr))

    while True:        
        scr.blit()
        cnt += 1
        t_txt = fonto.render(f"Remaining Time:{time_cnt}", True, (255,0,0))
        scr.sfc.blit(t_txt,(0,0))
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.update(scr)
        
        if cnt % 500 == 1:
            time_cnt -= 1
            if random.randint(1,5) <= 3:
                vx = random.choice([-1, +1])
                vy = random.choice([-1, +1])
                bombs.append(Bomb((random.randint(0,255), random.randint(0,255), random.randint(0,255)), 10, (vx, vy), scr))
        
        for bkd in bombs:
            bkd.update(scr)
            if kkt.rct.colliderect(bkd.rct):
                bombs.remove(bkd)
            
            if len(bombs) == 0:
                scr.sfc.blit(gc_txt,(550,400))
                pg.display.update()
                pg.time.wait(500)
                return
        
        if time_cnt == 0:
            scr.sfc.blit(go_txt,(550,400))
            pg.time.wait(500)
            return

        pg.display.update()
        clock.tick(500)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()