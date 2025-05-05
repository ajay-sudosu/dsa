def power(num):
    n = len(str(num)) - 1
    return 10 ** n


def calculate_rever(temp):
    num = 0
    while temp > 0:
        remainder = temp % 10
        num += remainder * power(temp)
        temp = temp // 10
    return num


def reverse(x: int) -> int:
    if x == 0:
        return 0
    us = 2147483647
    s = 2147483648
    temp = x
    if x > 0:
        num = calculate_rever(temp)
        if num > us:
            return 0
        else:
            return num
    else:
        temp = int(str(temp)[1:])
        num = calculate_rever(temp)
        if num > s:
            return 0
        else:
            return int("-"+(str(num)))


print(reverse(-1234))
