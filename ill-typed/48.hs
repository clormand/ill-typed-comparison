module Main where

import Data.Char

-- Problem: [1,n] and (^2) should be swapped
squareList n = map [1, n] (^2)             

main :: IO ()
main = putStrLn "hello world"