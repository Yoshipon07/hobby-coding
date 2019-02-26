dic = {"A": 4, "E": 3, "G": 6, "I": 1, "O": 0, "S": 5, "Z": 2}  # Leet変換用のハッシュ用意
moji = input()  # 文字列取得
# 1文字ずつ取り出す
# ハッシュに存在する文字なら変換して出力、存在しないならそのまま出力
for s in moji:
    if s in dic:
        print(str(dic[s]), end="")
    else:
        print(s, end="")
print()  # 最後は改行
