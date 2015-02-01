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

require "bigdecimal"

class PiApproximation
  attr_reader :n

  def initialize(prec = 28)
    # 計算精度
    BigDecimal.limit(prec)

    # 正多角形の辺の数
    @n = 6

    # 円の中心から内接正n角形の1辺へ下ろした垂線の長さ
    # 半径1の円の内接正6角形の場合、sqrt(3)/2
    @p = BigDecimal.new("3").sqrt(prec) / 2
  end

  def each
    loop do
      yield self
      @n *= 2
      @p = q
    end
  end

  def print_result
    puts "n = #{@n}のとき"
    puts "  #{l.to_s("f")} < π < #{m.to_s("f")}"
  end

  # 内接正n角形の周りの長さの1/2
  # = an
  def l
    a * @n
  end

  # 外接正n角形の周りの長さの1/2
  # = bn
  def m
    b * @n
  end

  private

  attr_writer :n
  attr_accessor :p

  # 内接正n角形の1辺の長さの1/2
  # = sqrt(1 - p^2)
  def a
    (1 - @p ** 2).sqrt(0)
  end

  # 外接正n角形の1辺の長さの1/2
  # = a/p
  def b
    a / @p
  end

  # 円の中心から内接正2n角形の1辺へ下ろした垂線の長さ
  # = sqrt((1 + p)/2)
  def q
    ((1 + @p) / 2).sqrt(0)
  end
end

if __FILE__ == $0
  # 利用例
  pa = PiApproximation.new(30)
  pa.each do |pi|
    pi.print_result
    if pi.n > 50000
      break
    end
  end
end
