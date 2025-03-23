# print n natural numbers in reverse order

def f(n):
    if n > 0:
        print(n, end=" ")
        f(n-1)


# f(5)


# print n odd numbers

def odd_num(n):
    if n > 0:
        odd_num(n-1)
        print(2*n - 1, end=" ")


# odd_num(10)


def even_num(n):
    if n > 0:
        even_num(n-1)
        print(2*n, end=" ")


# even_num(10)


# print n odd numbers in reverse

def odd_num_rev(n):
    if n > 0:
        print(2*n - 1, end=" ")
        odd_num_rev(n-1)


# odd_num_rev(10)

def even_num_rev(n):
    if n > 0:
        print(2*n, end=" ")
        even_num_rev(n-1)


even_num_rev(10)
