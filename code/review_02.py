# 35-a
pattern = 0b01001011
mask = 0b11110000
print(bin(pattern | mask))

# 35-b
pattern = 0b01001011
mask = 0b10000000
print(bin(pattern ^ mask))

# 35-c
pattern = 0b01001011
mask = 0b11111111
print(bin(pattern ^ mask))

# 35-d
pattern = 0b01001011
mask = 0b11111110
print(bin(pattern & mask))

# 35-e
pattern = 0b01001011
mask = 0b01111111
print(bin(pattern | mask))

# 35-f
pattern = 0b111111111111111111111111
mask = 0b111111110000000011111111
print(bin(pattern & mask))

# 35-g
pattern = 0b010101110101101001101100
mask = 0b111111111111111111111111
print(bin(pattern ^ mask))

# 35-h
pattern = 0b010101110101101001101100
mask = 0b111111111111111111111111
print(bin(pattern | mask))
print()

# 37
pattern = 0b10000001
mask = 0b10000001
print(bin(pattern ^ mask))

# 38
pattern = 0b10110101
mask1 = 0b10000001
pattern = pattern ^ mask1
mask2 = 0b10000001
print(bin(pattern & mask2))
print()

# 57
import math

rad = float(input("원의 반지름 = "))
len = 2 * math.pi * rad
area = math.pi * (rad ** 2)
print(f"원의 둘레 = {len}")
print(f"원의 넓이 = {area}")
print()

# 58
str = input("문자열 = ")
times = int(input("횟수 = "))
print(str * times)
print()

# 59
import math

side1 = float(input("Side 1 = "))
side2 = float(input("Side 2 = "))
hypo = math.sqrt(side1 ** 2 + side2 ** 2)
len = side1 + side2 + hypo
area = side1 * side2 / 2
print(f"빗변 = {hypo}")
print(f"둘레 = {len}")
print(f"넓이 = {area}")
