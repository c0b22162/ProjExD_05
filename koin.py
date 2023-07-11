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

    # ウィンドウを作る
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("coin getter")
    #追加機能　背景画像読み込み
    background_image = image.load('ex05/haikei1.jpg')

    
    
    # player初期位置
    player_x = 400
    player_y = 500

    # player
    player = pg.Rect(player_x, player_y, 50, 50)
    

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

        # player移動
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            player.x -= 5
        if keys[pg.K_RIGHT]:
            player.x += 5

         # 追加機能　背景画像をウィンドウに描画
        screen.blit(background_image, (0, 0))
                

        # コインの位置を更新
        for coin in coins:
            coin.y += 1
            pg.draw.ellipse(screen, YELLOW, coin)

            # 衝突検出
            if player.colliderect(coin):
                coins.remove(coin)
                score += 1

            # コインを再生する
            if coin.y > HEIGHT:
                coin.x = random.randint(0, WIDTH - 50)
                coin.y = random.randint(-HEIGHT, -50)

        # playerをウィンドウに描画
        pg.draw.rect(screen, YELLOW, player)
        
        # スコア
        font = pg.font.Font(None, 36)
        text = font.render("Score: " + str(score), True, YELLOW)
        screen.blit(text, (10, 10))

        pg.display.flip()
        

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()