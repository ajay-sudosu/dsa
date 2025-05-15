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


check = [1, 1, 2, 2]
print(remove_duplicate_from_sorted_array(arr=check))
