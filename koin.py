import pygame as pg
import random
import sys

WIDTH = 800  # ゲームウィンドウの幅
HEIGHT = 600  # ゲームウィンドウの高さ


def main():

    # 色
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    RED = (255,0,0)

    # ウィンドウを作る
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("coin getter")

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

   # 爆弾を作る 
    bombs = []
    for i in range(4):
        x = random.randint(0, WIDTH - 50)
        y = random.randint(-HEIGHT, -50)
        bomb = pg.Rect(x, y, 30, 30)
        bombs.append(bomb)

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

        # ウィンドウ更新
        screen.fill(WHITE)
        pg.draw.rect(screen, YELLOW, player)

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
        
        for bomb in bombs:
            bomb.y += 1
            pg.draw.ellipse(screen, RED, bomb)

            # 衝突検出
            if player.colliderect(bomb):
                bombs.remove(bomb)
                pg.quit()

            # 爆弾を再生する
            if bomb.y > HEIGHT:
                bomb.x = random.randint(0, WIDTH - 50)
                bomb.y = random.randint(-HEIGHT, -50)

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