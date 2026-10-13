import math

def digit_sum(n):
    a = len(str(abs(n)))
    b = abs(n)
    if n==0:
        return 0
    else:
        total = 0
        for i in range(a+1):
            total += b % 10
            b = b // 10
        return total