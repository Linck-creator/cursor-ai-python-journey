import math

def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    limit = math.isqrt(n)

    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False

    return True
print(is_prime(2))
print(is_prime(4))
print(is_prime(7))
print(is_prime(97))
print(is_prime(100))
print(is_prime(101))