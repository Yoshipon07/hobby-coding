N, M = map(int, input().split(" "))  # 学生の数N, 合格点M取得
student_array = [list(map(int, input().split(" "))) for i in range(N)]  # 生徒のデータ取得
# 生徒のデータとインデックス(インデックスの初期値1)を同時に取り出す
# ※maxを用いているのは生徒の成績が0を下回った場合に対応するため
# 条件を満たせばそのインデックス(生徒の番号)を出力
for i, student in enumerate(student_array, 1):
    if max(0, student[0] - student[1] * 5) >= M:
        print(i)
