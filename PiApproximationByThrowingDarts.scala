import Math.pow
import scala.util.Random.nextDouble

object PiApproximationByThrowingDarts {
  def piApprox(sampling: Int): Double = {
    val dart = (n: Int) => {
      val (x, y) = (nextDouble, nextDouble)
      if (pow(x, 2) + pow(y, 2) < 1) 1 else 0
    }
    val count = (1 to sampling).map(dart).sum
    count.toDouble / sampling * 4
  }

  def main(args: Array[String]): Unit = {
    val sampling =
      if (args.length == 1) args(0).toInt
      else 1000000
    println(s"π ≒ ${piApprox(sampling)}")
  }
}
