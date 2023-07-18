import pygame as pg
from pygame import image #追加背景
import random
import sys

# ゲームウィンドウの幅
WIDTH = 800
# ゲームウィンドウの高さ
HEIGHT = 600

def main():

    # 色の設定
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLUE = (0 ,0 ,255)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)

    # ウィンドウを作る
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    # ゲームの名前
    pg.display.set_caption("coin getter")
    #追加機能　背景画像読み込み
    background_image = image.load('ex05/haikei1.jpg')

    # player初期位置
    # playerの初期位置と大きさ
    player_x = 400
    player_y = 500
    # commit 2

    #player 画像に変更
    player = pg.image.load("ex05/usi.png")
    player_rect = player.get_rect()
    player_rect.center = (player_x, player_y)

    # コインを作る
    coins = []

    # スーパーコインを作る
    super_coins=[]

    # 防壁の初期状態（初めは存在しない）
    wall = None
    # 防壁の存在状態
    wall_exists = False

    # コインを10個入れる
    for i in range(10):
        # コインの生成位置をランダムにする
        # コインを画面の上端で生成する
        x = random.randint(0, WIDTH - 50)
        y = random.randint(-HEIGHT, -50)
        coin = pg.Rect(x, y, 50, 50)
        coins.append(coin)

    #スーパーコインを3個を入れる
    for j in range(3):
        # スーパーコインの生成位置をランダムにする
        # スーパーコインを上から降ろすにする
        x = random.randint(0, WIDTH - 50)
        y = random.randint(-HEIGHT, -50)
        super_coin = pg.Rect(x, y, 25, 25)
        super_coins.append(super_coin)

    # スコア初期値
    score = 0

    # main循環
    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
            
            # Tabを押すと防壁の存在状態をスウィッチする
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_TAB:
                    if wall_exists:
                        wall_exists = False
                    else:
                        # 防壁の形とplayerに対する位置
                        wall = pg.Rect(player_rect.left, player_rect.top - 25, player_rect.width, 25)
                        wall_exists = True

        # player移動 壁を通り過ぎないように
        # playerの移動と移動速度
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
            # コインを上から落ちることにする
            coin.y += 1
            pg.draw.ellipse(screen, YELLOW, coin)

            # 衝突検出
            if player_rect.colliderect(coin):
            # playerと重なったら、コインが消えて、スコアを1点クラス
                coins.remove(coin)
                score += 1

            # コインの再生位置
            # コインが画面外に出たら（playerと重なってない）、コインを画面の上端に再生成する
            if coin.y > HEIGHT:
                coin.x = random.randint(0, WIDTH - 50)
                coin.y = random.randint(-HEIGHT, -50)

        # playerをウィンドウに描画
        screen.blit(player,player_rect)
        
        # スコア
        # スーパーコインの位置の更新
        for super_coin in super_coins:
            # スーパーコインを上から落ちることにする
            # コインの2倍の速さで落ちることにする
            super_coin.y += 2
            pg.draw.ellipse(screen, BLUE, super_coin)

            #　衝突検出
            # playerと重なったら、スーパーコインが消えて、スコアを2点クラス
            if player_rect.colliderect(super_coin):
                super_coins.remove(super_coin)
                score += 2

            # スーパーコインの再生位置
            if super_coin.y > HEIGHT:
                # コインが画面外に出たら（playerと重なってない）、スーパーコインを画面の上端に再生成する
                super_coin.x = random.randint(0, WIDTH - 50)
                super_coin.y = random.randint(-HEIGHT, -50)

        # 防壁に色をつけて画面に表示する
        if wall_exists:
            pg.draw.rect(screen, RED, wall)

        # コインが防壁と重なったら、コインが消える
            for coin in coins[:]:
                if wall.colliderect(coin):
                    coins.remove(coin)

        # スコアの表示
        font = pg.font.Font(None, 36)
        text = font.render("Score: " + str(score), True, BLACK)
        screen.blit(text, (10, 10))

        # 新しいコインを生成
        if len(coins) < 10:  # 生成されたコインの数が10未満の場合に新しいコインを生成
            x = random.randint(0, WIDTH - 50)
            y = random.randint(-HEIGHT, -50)
            coin = pg.Rect(x, y, 50, 50)
            coins.append(coin)
        
        # super_coinも以上と同様にする
        if len(super_coins) < 3:
            x = random.randint(0, WIDTH - 50)# 生成されたコインの数が3未満の場合に新しいコインを生成
            y = random.randint(-HEIGHT, -50)
            super_coin = pg.Rect(x, y, 25, 25)
            super_coins.append(super_coin)

        pg.display.flip()

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()