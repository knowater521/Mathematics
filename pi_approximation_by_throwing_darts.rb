module PiApproximationByThrowingDarts
  module_function

  def pi_approx(sampling)
    dart = lambda do |n|
      x, y = Random.rand(1.0), Random.rand(1.0)
      x ** 2 + y ** 2 < 1 ? 1 : 0
    end
    count = (1..sampling).collect(&dart).inject(:+)
    count.to_f / sampling * 4
  end
end

if __FILE__ == $0
  sampling = ARGV.length == 1 ? ARGV[0].to_i : 1000000
  puts "π ≒ #{PiApproximationByThrowingDarts.pi_approx(sampling)}"
end
