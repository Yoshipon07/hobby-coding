N = int(input())  # 投球数取得
throw_array = [input() for i in range(N)]  # 審判の判定をリストに格納
strike = 0  # ストライク数
ball = 0  # ボール数

# リストから判定を取り出す
# ストライクならストライク数をインクリメントし、"3"になるとアウト
# ボールならボール数をインクリメントし、"4"になるとフォアボール
for throw in throw_array:
    if throw == "strike":
        strike += 1
        if strike == 3:
            print("out!")
            break
        else:
            print(throw + "!")
    else:
        ball += 1
        if ball == 4:
            print("fourball!")
            break
        else:
            print(throw + "!")
