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
print(shift_zeroes_to_end_order_preserved(arr=check1))
