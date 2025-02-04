import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen=screen
        #   在（0,0）处差创建一个子弹的矩形，在设置位置
        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        # self.rect=pygame.Rect(0,0,3,20)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        # 存储小数表示子弹位置
        self.y=float(self.rect.y)
        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor


    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y

    def draw_bullet(self):
        #在银屏上的子弹
        pygame.draw.rect(self.screen,self.color,self.rect) 



