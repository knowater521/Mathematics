# アルキメデスの円周率近似値計算2
#
# [方法]
# 半径1の円に内接する正n角形の周りの長さ: 2l
# 半径1の円に外接する正n角形の周りの長さ: 2m
# とする。
#
# 半径rの円の円周は2πrなので、r = 1のとき
# 2l < 2π < 2m
#  l <  π <  m
#
# n = 6, 12, 24, 48, 96, ...のときのl, mを計算することで
# 円周率πの近似値を求めることができる。

from decimal import Decimal, getcontext


def pi_approximation(prec=28):
    # 計算精度
    getcontext().prec = prec

    # 正多角形の辺の数
    n = 6

    # 円の中心から内接正n角形の1辺へ下ろした垂線の長さ
    # 半径1の円の内接正6角形の場合、sqrt(3)/2
    p = Decimal(3).sqrt() / 2

    # 内接正n角形の周りの長さの1/2
    # = an
    def l():
        return a() * n

    # 外接正n角形の周りの長さの1/2
    # = bn
    def m():
        return b() * n

    # 内接正n角形の1辺の長さの1/2
    # = sqrt(1 - p^2)
    def a():
        return (1 - p ** 2).sqrt()

    # 外接正n角形の1辺の長さの1/2
    # = a/p
    def b():
        return a() / p

    # 円の中心から内接正2n角形の1辺へ下ろした垂線の長さ
    # = sqrt((1 + p)/2)
    def q():
        return ((1 + p) / 2).sqrt()

    while True:
        yield {"n": n, "l": l(), "m": m()}
        n *= 2
        p = q()


def print_result(result):
    print("n = {n}のとき".format(**result))
    print("  {l} < π < {m}".format(**result))


if __name__ == "__main__":
    # 利用例
    pa = pi_approximation(30)
    for res in pa:
        print_result(res)
        if res["n"] > 10000000:
            break
