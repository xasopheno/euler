x_is_divisible_by_y :: Integer -> Integer -> Bool
x_is_divisible_by_y x y = x `mod` y == 0

main = print (x_is_divisible_by_y 4 3)
