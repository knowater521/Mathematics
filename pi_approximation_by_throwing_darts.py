# モンテカルロ法による円周率近似値計算
#
# [メモ]
# 単位円のx>=0, y>=0の範囲A(中心角π/4の扇形)の面積:
#   π/4
# 単位円に外接する正方形のx>=0, y>=0の範囲Bの面積:
#   1
# 範囲Bにランダムに投げたダーツが範囲Aに入る確率:
#   (範囲Aに入った本数)/(範囲Bに投げた本数) ≒ (π/4)/1 = π/4
# 点(x, y)が単位円の内側にある条件:
#   x^2 + y^2 < 1

import sys
from random import random


def pi_approx(sampling):
    def dart():
        x, y = random(), random()
        return 1 if x ** 2 + y ** 2 < 1 else 0
    count = sum(dart() for n in range(sampling))
    return count / sampling * 4


if __name__ == '__main__':
    sampling = 1000000
    if len(sys.argv) == 2:
        sampling = int(sys.argv[1])
    print('π ≒ {0}'.format(pi_approx(sampling)))
