import static java.lang.Math.pow;
import static java.lang.Math.random;

import java.util.function.IntUnaryOperator;
import java.util.stream.IntStream;

public class PiApproximationByThrowingDarts {
  public static double piApprox(int sampling) {
    final IntUnaryOperator dart = n -> {
      final double x = random();
      final double y = random();
      return pow(x, 2) + pow(y, 2) < 1 ? 1 : 0;
    };
    final int count = IntStream.rangeClosed(1, sampling).map(dart).sum();
    return (double) count / sampling * 4;
  }

  public static void main(String[] args) {
    final int sampling = args.length == 1 ? Integer.parseInt(args[0]) : 1000000;
    System.out.println(String.format("π ≒ %s", piApprox(sampling)));
  }
}
