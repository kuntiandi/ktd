import pygame
from pygame.sprite import Sprite

class ALien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen      #初始化外星人，并且设置其位置

        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()     #加载外星人图像，并设置rect属性

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height        #使外星人最初在屏幕左上角附近

        self.x=float(self.rect.x)           #获取位置值


