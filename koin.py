import pygame as pg
from pygame import image #追加背景
import random
import sys

WIDTH = 800  # ゲームウィンドウの幅
HEIGHT = 600  # ゲームウィンドウの高さ

def main():
    # 色
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLACK = (0, 0, 0)

    # ウィンドウを作る
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("coin getter")
    #追加機能　背景画像読み込み
    background_image = image.load('ex05/haikei1.jpg')

    
    
    # player初期位置
    player_x = 400
    player_y = 500
    # commit 2

    # player　画像に変更
    player = pg.image.load("ex05/usi.png")
    player_rect = player.get_rect()
    player_rect.center = (player_x,player_y)

    # コインを作る
    coins = []
    for i in range(10):
        x = random.randint(0, WIDTH - 50)
        y = random.randint(-HEIGHT, -50)
        coin = pg.Rect(x, y, 50, 50)
        coins.append(coin)

    # スコア初期値
    score = 0

    # main循環
    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0

        # player移動 壁を通り過ぎないように
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            if player_rect.left > 0:
                player_rect.x -= 2
            else:
                player_rect.x = 0
        if keys[pg.K_RIGHT]:
            if player_rect.right < WIDTH:
                player_rect.x += 2
            else:
                player_rect.x = WIDTH - player_rect.width


        # ウィンドウ更新
        screen.fill(WHITE)
        screen.blit(player,player_rect)

        screen.blit(background_image,(0,0))


        # コインの位置を更新
        for coin in coins:
            coin.y += 1
            pg.draw.ellipse(screen, YELLOW, coin)

            # 衝突検出
            if player_rect.colliderect(coin):
                coins.remove(coin)
                score += 1

            # コインを再生する
            if coin.y > HEIGHT:
                coin.x = random.randint(0, WIDTH - 50)
                coin.y = random.randint(-HEIGHT, -50)

        # playerをウィンドウに描画
        screen.blit(player,player_rect)
        
        # スコア
        font = pg.font.Font(None, 36)
        text = font.render("Score: " + str(score), True, BLACK)
        screen.blit(text, (10, 10))

        pg.display.flip()
        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()