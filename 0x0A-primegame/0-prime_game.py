#!/usr/bin/python3


def isPrime(n):
    """ method to check if a number is prime """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def game(n):
    """ method to simulate a single game """
    arr = [i for i in range(2, n + 1)]
    who = True
    for n in arr:
        if isPrime(n):
            who = not who
    if who:
        return 'Ben'
    else:
        return 'Maria'


def isWinner(x, nums: list):
    """ method to find the winner of x games between maria and ben
    """
    count = 1
    b = 0
    m = 0
    for n in nums:
        if count > x:
            break
        if game(n) == 'Ben':
            b += 1
        else:
            m += 1
        count += 1
    if b > m:
        winner = 'Ben'
    elif m > b:
        winner = 'Maria'
    else:
        winner = None
    return winner
