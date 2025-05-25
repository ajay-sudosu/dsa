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
    mid = 0
    left = 0
    right = len(arr) - 1

    while mid <= right:
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
print(sort0_1_2(arr=check2))
