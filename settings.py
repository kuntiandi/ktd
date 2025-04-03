class Settings:
    def __init__(self):
        self.screen_width=1200          #屏幕长宽
        self.screen_height=800
        self.bg_color=(105,105,105)    #屏幕颜色
        self.ship_speed = 1.5


        #初始化子弹的设置
        self.bullet_speed=2.0
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullets_allowed=3