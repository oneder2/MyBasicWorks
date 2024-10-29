class Settings():
    """储存《外星人入侵》当中所有的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 500
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
    
        # 飞船的设置
        self.ship_speed_factor = 0.7
        self.ship_limit = 3

        # 子弹的设置
        self.bullet_width = 5
        self.bullet_height = 30
        self.ship_bullet_color = 60, 60, 60
        self.alien_bullet_color = 255, 0, 0
        self.bullet_allowed = 2

        # 外星人设置
        self.fleet_drop_speed = 10

        # 游戏节奏加快的速度
        self.speedup_scale = 1.05
        # 外星人点数获得提高的速度
        self.score_scale = 1.1

        self.initialize_dynamic_settings()
    

    def initialize_dynamic_settings(self):
        """初始化随游戏进行不断更新的变量设置"""
        self.ship_speed_factor = 1
        self.ship_bullet_speed = 1.2
        self.alien_bullet_speed = 3
        self.alien_speed_factor = 0.5
        # self.bullet_allowed = 2
        
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50
    
    
    def increase_speed(self):
        """提高速度设置_和_外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.ship_bullet_speed *= self.speedup_scale
        self.alien_bullet_speed *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_allowed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)