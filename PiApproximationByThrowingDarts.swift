class PiApproximationByThrowingDarts {
  static func piApprox(sampling: Int) -> Double {
    let dart = { (n: Int) -> Int in
      let (x, y) = (drand48(), drand48())
      return pow(x, 2) + pow(y, 2) < 1 ? 1 : 0
    }
    let count = (1...sampling).map(dart).reduce(0, combine: +)
    return Double(count) / Double(sampling) * 4
  }
}

let sampling = 1000000
print("π ≒ \(PiApproximationByThrowingDarts.piApprox(sampling))")
