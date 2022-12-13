import pygame as pg
import sys
import random


def check_bound(obj_rct,scr_rct):
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko,tate

def bombs(scrn_rct):
    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255,0,0),(10,10),10)
    pg.draw.circle(bomb_sfc, (255,0,0),(10,10),10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    return bomb_sfc,bomb_rct

def main():        
    clock = pg.time.Clock()
    vx1, vy1 = +1, +1
    vx2, vy2 = +1, +1
    vx3, vy3 = +1, +1
    vx4, vy4 = +1, +1
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()
    bg_sfc = pg.image.load("ex04/fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()
    
    tori_sfc = pg.image.load("ex04/fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    
    bomb_sfc,bomb_rct_1 = bombs(scrn_rct)
    bomb_sfc,bomb_rct_2 = bombs(scrn_rct)
    bomb_sfc,bomb_rct_3 = bombs(scrn_rct)
    bomb_sfc,bomb_rct_4 = bombs(scrn_rct)
    
    fonto = pg.font.Font(None,100)
    fonto.set_bold
    txt = fonto.render("GAME OVER", True, (255,255,255))
    while True:
        scrn_sfc.blit(bg_sfc,bg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        key_dct = pg.key.get_pressed()
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        
        if check_bound(tori_rct,scrn_rct) != (+1, +1):
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1
        scrn_sfc.blit(tori_sfc,tori_rct)
        
        bomb_rct_1.move_ip(vx1, vy1)
        bomb_rct_2.move_ip(vx2, vy2)
        bomb_rct_3.move_ip(vx3, vy3)
        bomb_rct_4.move_ip(vx4, vy4)
        scrn_sfc.blit(bomb_sfc,bomb_rct_1)
        scrn_sfc.blit(bomb_sfc,bomb_rct_2)
        scrn_sfc.blit(bomb_sfc,bomb_rct_3)
        scrn_sfc.blit(bomb_sfc,bomb_rct_4)
        yoko1, tate1 = check_bound(bomb_rct_1,scrn_rct)
        yoko2, tate2 = check_bound(bomb_rct_2,scrn_rct)
        yoko3, tate3 = check_bound(bomb_rct_3,scrn_rct)
        yoko4, tate4 = check_bound(bomb_rct_4,scrn_rct)
        vx1 *= yoko1
        vy1 *= tate1
        vx2 *= yoko2
        vy2 *= tate2
        vx3 *= yoko3
        vy3 *= tate3
        vx4 *= yoko4
        vy4 *= tate4
        if tori_rct.colliderect(bomb_rct_1) or tori_rct.colliderect(bomb_rct_2) or tori_rct.colliderect(bomb_rct_3) or tori_rct.colliderect(bomb_rct_4):
            scrn_sfc.blit(txt,scrn_rct.center)
            pg.display.update()
            pg.time.wait(3000)
            return
            
        
        pg.display.update()
        clock.tick(1000)
            
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()