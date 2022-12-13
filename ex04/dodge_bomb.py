import pygame as pg
import sys

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    bg_sfc = pg.image.load("ex04/fig/pg_bg.jpg")