import pygame

# 游戏的初始化
pygame.init()
# Rect 只封装了数字计算，不需要init,因为不涉及图像绘制、窗口处理

# 创建游戏主窗口
screen = pygame.display.set_mode((480, 700))# flags depth
# 绘制背景图像
# 1>加载图像数据
bg = pygame.image.load("./images/background.png")
# 2>绘制图像
screen.blit(bg, (0, 0))
# 3>更新屏幕
pygame.display.update()

# 绘制英雄图像
hr = pygame.image.load("./images/me1.png")
# png支持透明，透明头像
screen.blit(hr, (150, 500))
pygame.display.update()

# 设置游戏时钟 time.Clock类tick(帧率)方法，根据上次调用时间
clock = pygame.time.Clock()

# 定义rect记录飞机位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 游戏循环->游戏真正开始

while True:
    # 设置刷新帧率
    clock.tick(60)
    # 检测用户交互
    # 事件监听，代码比较固定！
    # 监听事件
    for event in pygame.event.get():
        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出")
            pygame.quit()
            exit()
    # 更新图像位置
    # 修改飞机位置
    hero_rect.y -= 1
    if hero_rect.y < -126:
        hero_rect.y = 700
    # 更新屏幕显示
    # 先绘制背景，再把其他都绘制一遍
    screen.blit(bg, (0, 0))
    screen.blit(hr, hero_rect)

    pygame.display.update()

pygame.quit()