# sum of first N natural numbers
def sum_n_natural_numbers(n):
    if n == 1:
        return n
    return n + sum_n_natural_numbers(n-1)


# print(sum_n_natural_numbers(5))


# sum of first N odd natural numbers
def first_n_odd_numbers_sum(n):
    if n > 0:
        return (2*n - 1) + first_n_odd_numbers_sum(n-1)
    return 0


# print(first_n_odd_numbers_sum(4))


# sum of first N even natural numbers
def first_n_even_numbers_sum(n):
    if n > 0:
        return (2*n) + first_n_even_numbers_sum(n-1)
    return 0


# print(first_n_even_numbers_sum(3))


# square of first N even natural numbers
def sum_square_first_n_natural(n):
    if n > 0:
        return (n**n) + sum_square_first_n_natural(n-1)
    return 0


print(sum_square_first_n_natural(2))


# factorial of a number
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)


# print(fact(3))
