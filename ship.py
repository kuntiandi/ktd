import sys

import pygame

class Ship:
    def __init__(self,ai_game):
        self.screen=ai_game.screen              #获取屏幕位置
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        self.image=pygame.image.load('images/ship.bmp')         #加载图像
        self.rect=self.image.get_rect()             #获得飞船的位置矩阵

        self.rect.midbottom=self.screen_rect.midbottom              #设置飞船位置

        self.x=float(self.rect.x)
        self.y=float(self.rect.y)                            #为属性设置一个浮点数
                            #通过设置标签来方便进行移动
        self.moving_right=False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def blitme(self):#画飞船

        self.screen.blit(self.image,self.rect)

    def update(self):               #更新飞船位置(通过修改x的值，避开rect的值不能为浮点数这个漏洞)，并且为飞船设定飞行的边界
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.ship_speed
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.ship_speed
        if self.moving_up                   :
            self.y-=self.settings.ship_speed
        if self.moving_down                 :
            self.y+=self.settings.ship_speed

        self.rect.x=self.x
        self.rect.y=self.y




