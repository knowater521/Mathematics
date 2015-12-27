"use strict"

piApprox = (sampling) ->
  dart = () ->
    [x, y] = [Math.random(), Math.random()]
    if x ** 2 + y ** 2 < 1 then 1 else 0
  count = [1..sampling].map(dart).reduce((a, b) -> a + b)
  count / sampling * 4

module.exports =
  piApprox: piApprox

if process.argv[1] == __filename
  sampling = if process.argv.length == 3 then parseInt(process.argv[2], 10) else 1000000
  console.log "π ≒ #{piApprox(sampling)}"
