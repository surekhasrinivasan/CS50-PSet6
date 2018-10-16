# Problem 3 - program that calculates the minimum number of coins required to give a user change

from cs50 import get_float

# prompt the user for valid input that is positive number
while True:
    Amount = get_float("Change owed: ")
    if Amount > 0:
        break

# Convert dollar to cents $1 = 1 * 100 = 100cents and round it to whole integer
change = int(round(Amount * 100))
coin_count = 0

coin_count += change // 25
change %= 25

coin_count += change // 10
change %= 10

coin_count += change // 5
change %= 5

coin_count += change

print(f"{coin_count}")