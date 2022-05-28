# 02-06

# 1
import math

sideA = int(input("Length of side A? "))
sideB = int(input("Length of side B? "))
hypo = int(math.sqrt(sideA ** 2 + sideB ** 2))
print(f"빗변의 길이 = {hypo}")
print()

# 2
import math

sideA = float(input("Length of side A? "))
sideB = float(input("Length of side B? "))
hypo = math.sqrt(sideA ** 2 + sideB ** 2)
print(f"빗변의 길이 = {hypo}")
print()

# 3
mph = 7.74193548387
elapsed_min = 46
elapsed_sec = 30
print("Your speed is " + str(mph) + " mph")
print(
    "Your total elapsed time is "
    + str(elapsed_min)
    + " minutes, "
    + str(elapsed_sec)
    + " seconds"
)
print()

# 4
decToBin = bin(int(input("10진수 = ")))
print(f"2진수 = {decToBin}")
print()

# 5
plain = int(input("Your number = "))
key = 0x55555555
cipher = plain ^ key
print(f"My number = {cipher}")
print()
