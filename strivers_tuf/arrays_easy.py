arr = [1, 2, 4, 0, 0]


def check_sorted_array(arr):
    i = 0
    j = i + 1

    while j < len(arr):
        if arr[i] > arr[j]:
            return False
        i, j = i + 1, j + 1
    return True


# print(check_sorted_array(arr))


def remove_duplicate_from_array(arr):
    d = {}
    l = len(arr)
    i = 0
    while i < l:
        if arr[i] in d:
            d[arr[i]] += 1
            if d[arr[i]] > 1:
                arr.remove(arr[i])
                l -= 1
        else:
            d[arr[i]] = 1
        i += 1
    return arr


def remove_duplicate_from_array_optimized(arr):
    seen = set()
    result = []
    for i in arr:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result


def remove_duplicate_from_sorted_array(arr):
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            result.append(arr[i])
    return result


check = [1, 0, 0, 3, 9, 0, 0]
# print(remove_duplicate_from_sorted_array(arr=check))


def remove_duplicates(arr):
    """
    Array needs to be sorted for this algo
    """
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return arr[:i+1]


# print(remove_duplicates(arr=check))


def shift_zeroes_to_end_order_not_preserved(arr):
    j = len(arr) - 1
    i = len(arr) - 1
    while j >= 0:
        if arr[j] == 0:
            arr[j], arr[i] = arr[i], arr[j]
            i -= 1
        j -= 1
    return arr


check0 = [0, 0, 0, 5, 2, 0]
# print(shift_zeroes_to_end_order_not_preserved(arr=check0))


def shift_zeroes_to_end_order_preserved(arr):
    i = 0
    j = 0
    while j < len(arr):
        if arr[j] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
        j += 1
    return arr


check1 = [0, 0, 0, 3, 0, 4, 5, 7]
# print(shift_zeroes_to_end_order_preserved(arr=check1))


def missing_number(arr, N):
    total = (N * (N + 1)) // 2
    diff = int(total - sum(arr))

    if diff != 0:
        return diff
    return "All elements are present"


check_123 = [1, 2, 3, 4, 5, 6, 7, 8]
# print(missing_number(arr=check_123, N=9))


def union_or_array(arr1, arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]
# result = union_or_array(arr1=arr1, arr2=arr2)
# print(remove_duplicate_from_array_optimized(arr=result))


def longest_subarray_sum(arr, k):
    length = 0
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            if total == k:
                length = max(length, j - i + 1)
    return length


check_0 = [2, 3, 5]
# print(longest_subarray_sum(arr=check_0, k=52))


def longest_subarray_sum_two_pointer(arr, k):
    l = 0
    r = 0
    total = arr[0]
    length = 0

    for _ in range(len(arr)):
        if total == k:
            length = max(length, r - l + 1)

        while l <= r and total > k:
            total -= arr[l]
            l += 1

        r += 1
        if r < len(arr):
            total += arr[r]
    return length


print(longest_subarray_sum_two_pointer(arr=check_0, k=10))
