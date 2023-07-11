import pygame
import random

# ゲーム初期化
pygame.init()

# ウィンドウサイズ
screen_width = 800
screen_height = 600

# 色
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# ウィンドウを作る
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("COIN GETTER")

# player初期位置
player_x = 400
player_y = 500

# player
player = pygame.Rect(player_x, player_y, 50, 50)

# コインを作る
coins = []
for i in range(10):
    x = random.randint(0, screen_width - 50)
    y = random.randint(-screen_height, -50)
    coin = pygame.Rect(x, y, 50, 50)
    coins.append(coin)

# スコア初期値
score = 0

# main循環
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # player移動
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # ウィンドウ更新
    screen.fill(WHITE)
    pygame.draw.rect(screen, YELLOW, player)

    # コインの位置を更新
    for coin in coins:
        coin.y += 2
        pygame.draw.ellipse(screen, YELLOW, coin)

        # 衝突検出
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1

        # コインを再生する
        if coin.y > screen_height:
            coin.x = random.randint(0, screen_width - 50)
            coin.y = random.randint(-screen_height, -50)

    # スコア
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, YELLOW)
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()