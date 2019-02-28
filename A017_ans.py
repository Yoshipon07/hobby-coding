H, W, N = map(int, input().split(" "))  # 縦、横、ブロックの数取得
# ブロックの情報取得(縦、横、左端のx座標)
block = [list(map(int, input().split(" "))) for i in range(N)]
# フィールドを生成
field = [["." for i in range(W)] for j in range(H)]


# フィールドにブロックを埋め込む関数
# 左端のx座標をもとに#を埋め込んでいく
def create(field, m):
    for i in range(block[k][0]):
        for j in range(block[k][2], block[k][2] + block[k][1]):
            field[m - i][j] = "#"


# ブロックの数だけループ
# 他のブロックに当たると、その上の座標をmに格納しcreateを実行
for k in range(N):
    cnt = 0  # 他のブロックに当たらなかった回数
    for i in range(H):
        for j in range(block[k][2], block[k][2] + block[k][1]):
            if field[i][j] == "#":
                m = i - 1
                create(field, m)  # createを実行した後はbreak
                break
        else:
            cnt += 1  # breakしてなかったら(他のブロックに当たってなかったら)インクリメント
            continue
        break  # 二重ループを抜けるためのbreak
    # 一回も他のブロックに当たっていなければ、フィールドの一番下にcreate
    if cnt == H:
        m = H - 1
        create(field, m)
# joinを用いて出力
for i in range(H):
    print("".join(field[i]))
