module Main where

import Data.Char

-- Problem: x in condition should be even x or odd x.            
v17 = (\x -> x + (if x then 1 else 2))                

main :: IO ()
main = putStrLn "hello world"