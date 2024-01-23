import math

def zeros(n):
    sum = 0
    if n != 0:
        k_max = int(math.log(n, 5))
        for k in range(k_max):
            sum += int(n / 5 ** (k + 1))

    return sum
