import sys
import pygame

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init();
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    bg_color = (230, 230, 230)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        for even in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();

        screen.fill(bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()
run_game()