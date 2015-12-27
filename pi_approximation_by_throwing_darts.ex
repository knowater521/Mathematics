defmodule PiApproximationByThrowingDarts do
  def pi_approx(sampling) do
    :random.seed(:erlang.now)
    dart = fn(n) ->
      [x, y] = [:random.uniform, :random.uniform]
      if :math.pow(x, 2) + :math.pow(y, 2) < 1 do 1 else 0 end
    end
    count = 1..sampling |> Enum.map(dart) |> Enum.sum
    count / sampling * 4
  end
end

sampling = if length(System.argv) == 1 do
  System.argv |> List.first |> String.to_integer
else
  1000000
end
IO.puts "π ≒ #{PiApproximationByThrowingDarts.pi_approx(sampling)}"
