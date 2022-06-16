#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [4, 5, 2, 3, 1])))
print("Winner: {}".format(isWinner(4, [4, 5, 1, 5])))
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 6, 7, 8, 9, 3])))
