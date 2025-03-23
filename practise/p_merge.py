def merge(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge(arr[:mid])
    right = merge(arr[mid:])

    return sort(left, right)


def sort(left_arr, right_arr):
    _arr = []
    i, j = 0, 0


    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            _arr.append(left_arr[i])
            i += 1

        else:
            _arr.append(right_arr[j])
            j += 1

    _arr.extend(right_arr[j:])
    _arr.extend(left_arr[i:])
    return _arr


if __name__ == '__main__':
    result = merge(arr=[4, 3, 1, 6, 2, 5, 0])
    print(result)
