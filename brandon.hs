import System.Environment
import System.IO


r_i :: Double -> Double
r_i x = exp((-1)*x*87600)

r_ges' :: [Double] -> [Double]
r_ges' xs = [1 - r_i(y) | y <- xs]

r_ges :: [Double] -> Double
r_ges xs = 1 - product (r_ges' xs)

s_conv :: [String] -> [Double]
s_conv [] = []
s_conv (x:xs) = (read x :: Double) : s_conv xs


main = do
    a <- getArgs
    print $ r_ges $ s_conv a
    return $ r_ges $ s_conv $ a
