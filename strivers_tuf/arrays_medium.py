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

    # if question does not guarantee majority element is present or it could be None below is the another check
    # Checking if the stored element is the majority element
    check = 0
    for i in arr:
        if i == element:
            check += 1

    if check > (n / 2):
        return element
    return -1


check4 = [3, 4, 5, ]
print(majority_element_moores_voting_algo(check4, n=4))
