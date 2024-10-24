def positive_div(n, divisor=1):
    if divisor > n:
        return 0
    if n % divisor == 0:
        return 1 + positive_div(n, divisor + 1)
    else:
        return positive_div(n, divisor + 1)

n = 12
print(positive_div(n))
