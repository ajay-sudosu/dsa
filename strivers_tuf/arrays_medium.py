def two_sum_op(arr, k):
    save = {}

    for i in arr:
        rem = k - i
        if i in save:
            return [i, save[i]]
        else:
            save[rem] = i


check0 = [1, 2, 3, 4, 5, 7]
# print(two_sum_op(arr=check0, k=9))


def two_sum(arr, k):
    """
    O(n^2)
    """
    for i in arr:
        for j in range(1, len(arr)):
            if i + arr[j] == k:
                return [i, arr[j]]


check1 = [1, 1, 3, 4, 5, 7]
# print(two_sum(arr=check1, k=9))


def sort0_1_2(arr):
    """
        Dutch National flag algo
    """
    mid = 0
    left = 0
    right = len(arr) - 1

    while mid <= right:  # mid is checked for <= because of last element to process, try with (arr = [0,1, 2])
        if arr[mid] == 0:
            arr[left], arr[mid] = arr[mid], arr[left]
            mid += 1
            left += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[right], arr[mid] = arr[mid], arr[right]
            right -= 1
    return arr


check2 = [0, 1, 2, 1, 0, 2, 0, 1]
# print(sort0_1_2(arr=check2))


def majority_element(arr):
    save = {}
    n = len(arr) // 2
    element = arr[0]
    max_num = 0
    for i in arr:
        if i in save:
            save[i] += 1
            max_num = max(save[i], max_num)
        else:
            save[i] = 1
    for i, j in save.items():
        if j > n:
            element = i
            break
    return element


check3 = [3, 4, 5, 5, 1, 1, 1, 1, 1]
# print(majority_element(arr=check3))


def majority_element_moores_voting_algo(arr, n):
    # if the question states that the array has majority element that is present greater than n // 2 times
    element = None
    count = 0

    for i in arr:
        if count == 0:
            element = i
            count += 1

        elif i == element:
            count += 1

        else:
            count -= 1

    # if question does not guarantee majority element is present it could be None below is the another check
    # Checking if the stored element is the majority element
    check = 0
    for i in arr:
        if i == element:
            check += 1

    if check > (n / 2):
        return element
    return -1


check4 = [3, 4, 5, ]
# print(majority_element_moores_voting_algo(check4, n=4))


def maximum_subarray_sum(arr):
    """
    This is a brute force approach
    """
    max_sum = arr[0]
    for i in range(len(arr)):
        sub_total = 0
        for j in range(i, len(arr)):
            sub_total = sub_total + arr[j]
            max_sum = max(max_sum, sub_total)
    return max_sum


check5 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(maximum_subarray_sum(arr=check5))


def maximum_subarray_sum_kandane_algo_1(arr):
    max_sum = sub_total = arr[0]

    for i in arr[1:]:
        sub_total = max(i, sub_total+i)
        max_sum = max(sub_total, max_sum)
    return max_sum


check6 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(maximum_subarray_sum_kandane_algo_1(arr=check6))


def maximum_subarray_sum_kandane_algo_2(arr):
    max_sum = sub_total = arr[0]

    for i in arr:
        sub_total += i
        if sub_total > max_sum:
            max_sum = sub_total
        if sub_total < 0:
            sub_total = 0

    return max_sum


check7 = [-2, -1, -2]
# print(maximum_subarray_sum_kandane_algo_2(arr=check7))


def maximum_subarray_sum_with_subarry(arr):
    max_sum = arr[0]
    sub_total = 0
    start = 0
    end = 0
    begin = 0
    for i in range(len(arr)):
        if sub_total == 0:
            start = i
        sub_total += arr[i]
        if sub_total > max_sum:
            max_sum = sub_total
            begin = start
            end = i
        if sub_total < 0:
            sub_total = 0

    return arr[begin: end+1], max_sum


# check8 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
check8 = [-2,]
# print(maximum_subarray_sum_with_subarry(check8))


def buy_and_sell(arr):
    minimum = float("inf")
    max_sum = 0
    for i in arr:
        minimum = min(i, minimum)
        max_sum = max(max_sum, i-minimum)
    return max_sum


# check9 = [7, 1, 5, 3, 6, 4]
check9 = [3, 8, 2, 5, 1, 7]
# print(buy_and_sell(check9))

