module Main where

import Data.Char

-- Problem: there are several ways to fix the program. No oracle given.            
v24 = \x -> let g = \y -> (y : x) in g 1 ++ g True         

main :: IO ()
main = putStrLn "hello world"