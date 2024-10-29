import sys
import pygame

from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from settings import Settings

import random
import json
from time import sleep


"""
————————————————————按键检测——————————————————————
"""

def check_keydown_events(event, ai_settings, screen, stats, sb, 
                         ship, aliens, bullets):
    """相应按键"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # 向上移动飞船
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # 向下移动飞船
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # 开火
        fire_bullet_ship(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        # 退出游戏快捷键
        exit()
    elif event.key == pygame.K_p:
        # 开始游戏快捷键
        start_game(ai_settings, screen, stats, sb, ship, aliens,bullets)


def check_keyup_events(event, ai_settings, screen, ship, bullets):
    """相应松开"""
    if event.key == pygame.K_RIGHT:
        # 停止向右移动飞船
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 停止向左移动飞船
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        # 停止向左移动飞船
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        # 停止向左移动飞船
        ship.moving_down = False


def check_events(ai_settings, screen, stats, sb, play_button, 
                 ship, aliens, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb,
                                 ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, 
                              ship, aliens, bullets, mouse_x, mouse_y)


"""
————————————————————游戏状态检测——————————————————————
"""


def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """开始游戏"""
    # 隐藏光标
    pygame.mouse.set_visible(False)

    # 重置游戏统计信息
    stats.reset_stats()
    stats.game_active = True

    # 重置记分牌图像
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    # 清空子弹和外星人列表
    aliens.empty()
    bullets.empty()

    # 创建一群新的外星人，并让飞船居中
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()


def check_play_button(ai_settings, screen, stats, sb, play_button, 
                      ship, aliens, bullets, mouse_x, mouse_y):
    """在玩家单击Play按钮时开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)



"""
————————————————————状态更新——————————————————————
"""

"""
————————————————屏幕——————————————————
"""

def update_screen(ai_settings, screen, stats, sb, 
                  ship, aliens, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重新绘制所有子弹
    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    sb.show_score()

    # 如果游戏处于非活动状态，绘制Play按钮
    if not stats.game_active:
        play_button.drow_button()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()


"""
————————————————计分——————————————————
"""


def check_high_score(stats, sb):
    """检测是否产生了新的最高分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


"""
————————————————子弹——————————————————
"""


def fire_bullet_ship(ai_settings, screen, ship, bullets):
    """如果还没有达到限制，发射一颗子弹"""
    # 创建一颗子弹，并将其添加到分组Group中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, 
                                  ship, aliens, bullets):
    # 响应子弹与外星人的碰撞
    # 如果有子弹击中了敌人，就消灭子弹与敌人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliengroup in collisions.values():
            stats.score += ai_settings.alien_points * len(aliengroup)
            sb.prep_score()
        check_high_score(stats, sb)
    
    if len(aliens) == 0:
        # 删除现有子弹，加快游戏节奏，并生成一群新敌人
        bullets.empty()
        ai_settings.increase_speed()

        # 提高一个等级
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def check_bullet_ship_collisions(ai_settings, screen, stats, sb, 
                                  ship, aliens, bullets):
    # 响应子弹与玩家飞船的碰撞
    # 如果有子弹击中了玩家，就触发与飞船撞击外星人一样的结果
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    


def update_bullets(ai_settings, screen, stats, sb, 
                   ship, aliens, bullets):
    """更新子弹位置，并删除已经消失的子弹"""
    # 更新子弹位置
    for bullet in bullets:
        bullet.update_ship()

    # 让离开屏幕的飞船子弹消失
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        
    # 让离开屏幕的外星人子弹消失
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


    check_bullet_alien_collisions(ai_settings, screen, stats, sb, 
                                  ship, aliens, bullets)
    check_bullet_ship_collisions(ai_settings, screen, stats, sb, 
                                 ship, aliens, bullets)


"""
————————————————外星人——————————————————
"""


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可以容纳多少个外星人"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width # 外星人宽度为外星人图片宽度
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    # alien.rect.x = random.randint(0,800)
    # alien.rect.y = random.randint(0,600)
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行能容纳多少外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)  
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)


    # 创建第一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变平移方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, sb, 
             ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left -= 1
        stats.ships_left -= 1
        # 更新记分牌
        sb.prep_ships()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        bullets.empty()
        # 创建一群新的外星人，并将飞船置于屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    
    else:
        if stats.score == stats.high_score:
            # print("yes")
            with open("high_score.json", "w", encoding = "utf-8") as fp:
                json.dump(stats.score, fp, ensure_ascii = False)
        # print("no")
        stats.game_active = False
        stats.score = 0
        pygame.mouse.set_visible(True)


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    检测外星人是否到达边缘
    更新外星人群中所有外星人的位置
    """ 
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人与飞船的链接
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
    # 检测有无外星人到达底端
    check_aliens_bottom(ai_settings, screen, stats, sb, 
                        ship, aliens, bullets)


def check_aliens_bottom(ai_settings, screen, stats, sb, 
                        ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break

