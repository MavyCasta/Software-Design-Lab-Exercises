def multi(m, n):
    result = sum(m for _ in range(abs(n)))
    if n < 0:
        return -result
    else:
        return result

m = int(input("Please enter the first positive integer: "))
n = int(input("Please enter the second positive integer: "))
print(multi(m, n))
