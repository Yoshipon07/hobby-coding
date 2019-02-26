# SETが命令されたときに実行する関数：引数(ミニコンピューターのリスト, ミニコンピューターの番号, 格納する数字)
def Set(num_array, i, a):
    num_array[i - 1] = a


# ADDが命令されたときに実行する関数：引数(ミニコンピューターのリスト, 計算する数字)
def Add(num_array, a):
    num_array[1] = num_array[0] + a


# SUBが命令されたときに実行する関数：引数(ミニコンピューターのリスト, 計算する数字)
def Sub(num_array, a):
    num_array[1] = num_array[0] - a


N = int(input())  # 命令の数取得
command_array = [input().split(" ") for i in range(N)]  # 命令を取得
num_array = [0, 0]  # ミニコンピューターの初期化
# 命令を取り出す
# 命令の文言ごとに関数を実行
for command in command_array:
    if command[0] == "SET":
        Set(num_array, int(command[1]), int(command[2]))
    elif command[0] == "ADD":
        Add(num_array, int(command[1]))
    else:
        Sub(num_array, int(command[1]))
print(" ".join(map(str, num_array)))  # joinを用いて空白区切りで出力
