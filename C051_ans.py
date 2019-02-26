import itertools as it  # 順列生成のためにitertoolsをimport

tranp = list(map(int, input().split(" ")))  # トランプの数字をリストに格納
num_array = [10 * v[0] + v[1] + 10 * v[2] + v[3] for v in it.permutations(tranp)]  # 内包表記を用いて全部の計算結果を格納
print(max(num_array))  # 最大の計算結果を出力
