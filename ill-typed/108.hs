module Main where

import Data.Char

-- Problem: ++ should be +
f4 [] = []                                              
f4 (0 : t) = f4 t
f4 (h : t) = h/2.0 ++ f4 t

main :: IO ()
main = putStrLn "hello world"