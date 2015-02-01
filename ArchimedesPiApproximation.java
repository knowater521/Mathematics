/*
 * アルキメデスの円周率近似値計算
 *
 * [方法]
 * 半径1の円に内接する正n角形の周りの長さ: 2l
 * 半径1の円に外接する正n角形の周りの長さ: 2m
 * とする。
 *
 * 半径rの円の円周は2πrなので、r = 1のとき
 * 2l < 2π < 2m
 *  l <  π <  m
 *
 * n = 6, 12, 24, 48, 96, ...のときのl, mを計算することで
 * 円周率πの近似値を求めることができる。
 */

import static java.lang.Math.pow;
import static java.lang.Math.sqrt;

import java.util.Iterator;

public class ArchimedesPiApproximation implements Iterable<ArchimedesPiApproximation.PiApproximation> {
  @Override
  public Iterator<ArchimedesPiApproximation.PiApproximation> iterator() {
    return new PiApproximation();
  }

  public class PiApproximation implements Iterator<PiApproximation>, Cloneable {
    // 正多角形の辺の数
    private long n = 6L;

    // 円の中心から内接正n角形の1辺へ下ろした垂線の長さ
    // 半径1の円の内接正6角形の場合、sqrt(3)/2
    private double p = sqrt(3) / 2;

    @Override
    public boolean hasNext() {
      return true;
    }

    @Override
    public PiApproximation next() {
      PiApproximation curr = this.clone();
      n *= 2;
      p = q();
      return curr;
    }

    @Override
    public PiApproximation clone() {
      try {
        return (PiApproximation) super.clone();
      } catch (CloneNotSupportedException e) {
        e.printStackTrace();
        return null;
      }
    }

    public void printResult() {
      System.out.printf("n = %sのとき%n", n);
      System.out.printf("  %s < π < %s%n", l(), m());
    }

    public long getN() {
      return n;
    }

    // 内接正n角形の周りの長さの1/2
    // = an
    public double l() {
      return a() * n;
    }

    // 外接正n角形の周りの長さの1/2
    // = bn
    public double m() {
      return b() * n;
    }

    // 内接正n角形の1辺の長さの1/2
    // = sqrt(1 - p^2)
    private double a() {
      return sqrt(1 - pow(p, 2));
    }

    // 外接正n角形の1辺の長さの1/2
    // = a/p
    private double b() {
      return a() / p;
    }

    // 円の中心から内接正2n角形の1辺へ下ろした垂線の長さ
    // = sqrt((1 + p)/2)
    private double q() {
      return sqrt((1 + p) / 2);
    }
  }

  public static void main(String[] args) {
    // 利用例
    ArchimedesPiApproximation pa = new ArchimedesPiApproximation();
    for (ArchimedesPiApproximation.PiApproximation pi : pa) {
      pi.printResult();
      if (pi.getN() > 25000L) {
        break;
      }
    }
  }
}
