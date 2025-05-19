arr = [2, 3, 6, 0, 0, 6,9,0]


def zeroes_to_last(arr):
    i = 0
    j = 0
    while j < len(arr):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    return arr


print(zeroes_to_last(arr=arr))
