module PiApproximationByThrowingDarts where

import System.Environment (getArgs)
import System.Random (randomRIO)

piApprox :: (Fractional a, Enum a) => a -> IO a
piApprox sampling = do
  count <- mapM dart [1..sampling]
  return $ fromIntegral (sum count) / sampling * 4
    where
      dart _ = do
        x <- randomRIO (0, 1) :: IO Double
        y <- randomRIO (0, 1) :: IO Double
        if x ^ 2 + y ^ 2 < 1
          then return 1
          else  return 0

main :: IO ()
main = do
  args <- getArgs
  let sampling = if length args == 1
                   then read $ head args :: Double
                   else 1000000
  piApprox sampling >>= print
