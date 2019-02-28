N = int(input())  # 文字列の数を取得
G = input()  # 抽出する文字列を取得
moji = [input() for i in range(N)]  # 文字列を取得
flag = 0  # フラグの初期化

# 抽出する文字列があればそれを表示(フラグを1にする)
for i in range(N):
    if G in moji[i]:
        flag = 1
        print(moji[i])

# フラグが0なら(該当する文字列がなければ)"None"を表示
if flag == 0:
    print("None")
