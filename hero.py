import pygame
pygame.init()

# 创建游戏的窗口 480*700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 加载图像的数据
bg = pygame.image.load("./images/background.png")
# 将图像绘制到指定位置
screen.blit(bg, (0, 0))
# 更新整个屏幕的显示
pygame.display.update()

# 绘制英雄图像
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 500))
pygame.display.update()

while True:
    pass

pygame.quit()
