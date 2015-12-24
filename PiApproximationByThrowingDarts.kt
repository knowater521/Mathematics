import java.lang.Math.pow
import java.lang.Math.random

class PiApproximationByThrowingDarts {
  companion object {
    fun piApprox(sampling: Int): Double {
      val dart =  { n: Int ->
        val x = random()
        val y = random()
        if (pow(x, 2.0) + pow(y, 2.0) < 1) 1 else 0
      }
      val count = (1..sampling).map(dart).fold(0) { a, b -> a + b }
      return count.toDouble() / sampling * 4
    }
  }
}

fun main(args: Array<String>): Unit {
  val sampling = if (args.size() == 1) args[0].toInt() else 1000000
  println("π ≒ ${PiApproximationByThrowingDarts.piApprox(sampling)}")
}
