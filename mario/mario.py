# Problem 2 - Program that prints a half-pyramid of a specified height using hashes (#) for blocks

from cs50 import get_int

# prompt the user for valid input that is positive number and no greater than 23
while True:
    height = get_int("Height: ")
    if height >= 0 and height <= 23:
        break

# Print out that many bricks
for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(i + 2):
        print("#", end="")
    print()