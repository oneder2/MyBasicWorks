import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

class Bullet(Sprite):
    """一个对被发射子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship, aliens):
        """在飞船所处的位置船舰一个子弹对象"""
        super(Bullet, self).__init__()
        
        self.screen = screen

        self.prep_ship_bullets(ai_settings, ship)
        # self.prep_alien_bullets(ai_settings, aliens)


    def prep_ship_bullets(self, ai_settings, ship):
        """飞船部分子弹准备"""
        # 在(0, 0)处创造一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示子弹的位置
        self.y = float(self.rect.y)
        
        # 子弹的数值
        self.ship_color = ai_settings.ship_bullet_color
        self.ship_bullet_speed = ai_settings.ship_bullet_speed


    def prep_alien_bullets(self, ai_settings, alien):
        """外星人部分子弹准备"""
        # 在(0, 0)处创造一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom

        # 存储用小数表示子弹的位置
        self.y = float(self.rect.y)
        
        # 子弹的数值
        self.alien_color = ai_settings.aliens_bullet_color
        self.aliens_bullet_speed = ai_settings.aliens_bullet_speed


    def update_ship(self):
        """向上移动飞船子弹"""
        # 更新表示子弹位置的小数值
        self.y -= self.ship_bullet_speed
        # 更新表示子弹位置的rect位置
        self.rect.y = self.y
    

    def update_aliens(self):
        """向下移动外星人子弹"""
        # 更新表示子弹位置的小数值
        self.y += self.aliens_bullet_speed
        # 更新表示子弹位置的rect位置
        self.rect.y = self.y
    

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        # 飞船部分
        pygame.draw.rect(self.screen, self.ship_color, self.rect)
        
        # # 外星人部分
        # pygame.draw.rect(self.screen, self.alien_color, self.rect)


