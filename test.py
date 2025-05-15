arr = [5, 3, 2, 1, 5, 0, 0, 0]


def bubble(arr):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# print(bubble(arr=arr))


def selection(arr):
    for i in range(len(arr)):
        index = i
        for j in range(i+1, len(arr)):
            if arr[index] > arr[j]:
                index = j

        arr[index], arr[i] = arr[i], arr[index]
    return arr


# print(selection(arr=arr))


def insertion(arr):
    for i in range(1, len(arr) + 1):
        j = i - 1

        while j > 0:
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr

# print(insertion(arr=arr))


def merge(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge(arr[:mid])
    right = merge(arr[mid:])

    return m(left, right)


def m(left, right):
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result.extend(left[l:])
    result.extend(right[r:])
    return result


# print(merge(arr))


def quick(arr):
    if len(arr) <= 1:
        return arr
    left, right = [], []
    pivot = arr[-1]
    for i in arr[:-1]:
        if pivot < i:
            right.append(i)
        else:
            left.append(i)

    return quick(left) + [pivot] + quick(right)


# print(quick(arr))
