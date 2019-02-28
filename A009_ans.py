H, W = map(int, input().split(" "))  # 箱の高さと幅を取得
box = [input() for i in range(H)]  # 箱の状態を取得
lazer = 1  # レーザーの方向 右：1 左：-1 上：2 下：-2
cnt = 0  # 区画を通過する回数
i = 0  # 初期区画の位置(x座標)
j = 0  # 初期区画の位置(y座標)


# レーザーが右の場合に呼び出す関数
# 鏡の向きでレーザーの方向、区画を変更させる
# カウントも進める
def reflect_1(box):
    global i, j, lazer, cnt
    cnt += 1
    if box[i][j] == "_":
        j += 1
    elif box[i][j] == "\\":
        lazer = -2
        i += 1
    elif box[i][j] == "/":
        lazer = 2
        i -= 1


# レーザーが左の場合に呼び出す関数
# 鏡の向きでレーザーの方向、区画を変更させる
# カウントも進める
def reflect_2(box):
    global i, j, lazer, cnt
    cnt += 1
    if box[i][j] == "_":
        j -= 1
    elif box[i][j] == "\\":
        lazer = 2
        i -= 1
    elif box[i][j] == "/":
        lazer = -2
        i += 1


# レーザーが上の場合に呼び出す関数
# 鏡の向きでレーザーの方向、区画を変更させる
# カウントも進める
def reflect_3(box):
    global i, j, lazer, cnt
    cnt += 1
    if box[i][j] == "_":
        i -= 1
    elif box[i][j] == "\\":
        lazer = -1
        j -= 1
    elif box[i][j] == "/":
        lazer = 1
        j += 1


# レーザーが下の場合に呼び出す関数
# 鏡の向きでレーザーの方向、区画を変更させる
# カウントも進める
def reflect_4(box):
    global i, j, lazer, cnt
    cnt += 1
    if box[i][j] == "_":
        i += 1
    elif box[i][j] == "\\":
        lazer = 1
        j += 1
    elif box[i][j] == "/":
        lazer = -1
        j -= 1


# レーザーの方向によって呼び出す関数を変える
# x,y座標のどちらかが範囲外に出るとループを抜ける
while True:
    if lazer == 1:
        reflect_1(box)
        if i == -1 or i == H or j == W:
            break
    elif lazer == -1:
        reflect_2(box)
        if i == -1 or i == H or j == -1:
            break
    elif lazer == 2:
        reflect_3(box)
        if i == -1 or j == -1 or j == W:
            break
    elif lazer == -2:
        reflect_4(box)
        if i == H or j == -1 or j == W:
            break
print(cnt)  # 通過した区画の数を出力
