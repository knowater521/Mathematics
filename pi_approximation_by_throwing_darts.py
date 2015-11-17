import sys
from random import random


# [メモ]
# 単位円の方程式:
#   x^2 + y^2 = 1
# 単位円の面積:
#   π(1/2)^2 = π/4
# 単位円に外接する正方形の面積:
#   1^2 = 1
def pi_approx(sampling):
    def dart():
        x, y = random(), random()
        return 1 if x ** 2 + y ** 2 < 1 else 0
    count = sum(dart() for n in range(1, sampling))
    return count / sampling * 4


if __name__ == '__main__':
    sampling = 10000
    if len(sys.argv) == 2:
        sampling = int(sys.argv[1])
    print('π ≒ {0}'.format(pi_approx(sampling)))
