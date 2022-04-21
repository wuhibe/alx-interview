def minOperations(n):
    if n <= 0:
        return 0
    x = factorize(n)
    sum = 0
    for i in x:
        sum += i
    return sum

def factorize(n):
    temp = n
    x = 2
    li = []
    while x <= n:
        while x <= temp:
            if temp % x == 0:
                temp = temp / x
                if (is_prime(x)):
                    li.append(x)
            else:
                break
        x += 1
        temp = n
    return li

def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True