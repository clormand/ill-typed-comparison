module Main where

import Data.Char

-- Problem: x should be [x]
split xs = case xs of                                               
    [] -> ([],[])
    [x] -> (x,[])
    (x:y:zs) -> let (xs, ys) = split zs
                in (x:xs, y:ys)

main :: IO ()
main = putStrLn "hello world"