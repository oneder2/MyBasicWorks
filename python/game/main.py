import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口大小
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("简单的 Pygame 示例")

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 矩形的初始位置
rect_x = width // 2
rect_y = height // 2
rect_width = 50
rect_height = 50
speed = 5

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 获取按键状态
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= speed
    if keys[pygame.K_RIGHT]:
        rect_x += speed
    if keys[pygame.K_UP]:
        rect_y -= speed
    if keys[pygame.K_DOWN]:
        rect_y += speed

    # 填充背景
    screen.fill(WHITE)

    # 绘制矩形
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(60)

