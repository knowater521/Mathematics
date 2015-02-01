# アルキメデスの円周率近似値計算
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

from copy import copy
from decimal import Decimal, getcontext


class PiApproximation():
    __slots__ = ["__n", "__p"]

    def __init__(self, prec=28):
        # 計算精度
        getcontext().prec = prec

        # 正多角形の辺の数
        self.__n = 6

        # 円の中心から内接正n角形の1辺へ下ろした垂線の長さ
        # 半径1の円の内接正6角形の場合、sqrt(3)/2
        self.__p = Decimal(3).sqrt() / 2

    def __iter__(self):
        return self

    def __next__(self):
        curr = copy(self)
        self.__n *= 2
        self.__p = self.__q()
        return curr

    def print_result(self):
        print("n = {0}のとき".format(self.__n))
        print("  {0} < π < {1}".format(self.l(), self.m()))

    @property
    def n(self):
        return self.__n

    # 内接正n角形の周りの長さの1/2
    # = an
    def l(self):
        return self.__a() * self.__n

    # 外接正n角形の周りの長さの1/2
    # = bn
    def m(self):
        return self.__b() * self.__n

    # 内接正n角形の1辺の長さの1/2
    # = sqrt(1 - p^2)
    def __a(self):
        return (1 - self.__p ** 2).sqrt()

    # 外接正n角形の1辺の長さの1/2
    # = a/p
    def __b(self):
        return self.__a() / self.__p

    # 円の中心から内接正2n角形の1辺へ下ろした垂線の長さ
    # = sqrt((1 + p)/2)
    def __q(self):
        return ((1 + self.__p) / 2).sqrt()


if __name__ == "__main__":
    # 利用例
    pa = PiApproximation(30)
    for pi in pa:
        pi.print_result()
        if pi.n > 10000000:
            break
