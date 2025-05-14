def count(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count


def fact(num):
    if num == 1 or num == 0:
        return 1
    return num * fact(num-1)


def prime(num):
    import math
    count = 0
    rnge = int(math.sqrt(num))
    start = 2
    if num == 1:
        return False
    while start < rnge:
        if num % start == 0:
            return False
        start += 1
    return True


def gcd(num1, num2):
    result = 1
    for i in range(1, num1+1):
        if num1 % i == 0 and num2 % i == 0:
            result = i
    return result


def gcd_better(num1, num2):
    minimum = min(num1, num2)
    for i in range(minimum, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1


def reverse_array(arr):
    if len(arr) == 1:
        return arr
    i = 0
    j = len(arr) - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i, j = i + 1, j - 1
    return arr


def fibo(n):
    a = 0
    b = 1

    for i in range(n):
        yield a
        a, b = b, a + b


result = fibo(5)
for i in result:
    print(i)
