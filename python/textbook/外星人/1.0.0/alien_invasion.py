import pygame
from pygame.sprite import Group

from settings import Settings   
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

from ship import Ship
from alien import Alien
from bullet import Bullet


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于储存游戏储存信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船，一个子弹编组，一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建一个外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # print("doing")
        gf.check_events(ai_settings, screen, stats, sb, play_button, 
                        ship, aliens, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, 
                              ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, 
                             ship, aliens, bullets)
        
        gf.update_screen(ai_settings, screen, stats, sb, 
                         ship, aliens, bullets, play_button)        
        

run_game()