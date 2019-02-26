Q = int(input())  # 判定したい整数の数取得
num_array = [int(input()) for i in range(Q)]  # 判定する整数をリストに格納
# 判定する整数を取り出す
# リスト内包表記を使って約数を格納
# sum,absを用いて各条件ごとに出力する
for num in num_array:
    divisor = [i for i in range(1, num) if num % i == 0]
    if sum(divisor) == num:
        print("perfect")
    elif abs(sum(divisor) - num) == 1:
        print("nearly")
    else:
        print("neither")
