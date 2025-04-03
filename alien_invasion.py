import sys
#调用库
from settings import Settings
import pygame
from ship import Ship
from bullet import Bullet
from alien import  ALien
class AlienInvasion:            #对游戏设置类
    def __init__(self):         #进行各项基础设置的设定
        pygame.init()       #对pygame的各个值初始化

        self.clock=pygame.time.Clock()      #获得时钟，用于调整帧率
        self.settings=Settings()        #获取设置

        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))       #根据设定调整屏幕大小
        pygame.display.set_caption("Alien Invasion")            #更改标题

        self.ship=Ship(self)            #创建飞船属性
        self.bullets=pygame.sprite.Group()          #储存子弹
        self.aliens=pygame.sprite.Group()              #创建外星人编组

        self._create_fleet()


    def _fire_bullet(self):#创建一个子弹，并加入编组group
        if len(self.bullets)<self.settings.bullets_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)


    def _check_keydown_events(self,event):#相应按键按下
        print(f"Key pressed: {event.key}")
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up=True
        elif event.key ==pygame.K_DOWN:
            self.ship.moving_down=True
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):#相应按键离开
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key ==pygame.K_UP:
            self.ship.moving_up =False
        elif event.key ==pygame.K_DOWN:
            self.ship.moving_down=False


    def _check_events(self):              #完成飞船运行设置
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)


    def _update_bullets(self):
        #更新子弹位置并删除已消失的子弹
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_alien(self,x_position):
        new_alien=ALien(self)
        new_alien.x=x_position
        new_alien.rect.x=x_position
        self.aliens.add(new_alien)


    def _create_fleet(self):#创建一个外星人，再不断添加，直到没有空间

        alien=ALien(self)
        alien_width=alien.rect.width

        current_x=alien_width
        while current_x<(self.settings.screen_width-2*alien_width):
            self._create_alien(current_x)
            current_x+=2*alien_width

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()


    def run_game(self):             #定义运行游戏
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)                 #设定帧率


if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()