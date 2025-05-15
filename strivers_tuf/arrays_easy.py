arr = [1, 2, 4, 0, 0]


def check_sorted_array(arr):
    i = 0
    j = i + 1

    while j < len(arr):
        if arr[i] > arr[j]:
            return False
        i, j = i + 1, j + 1
    return True


print(check_sorted_array(arr))



