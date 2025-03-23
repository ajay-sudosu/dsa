def merge(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = merge(arr[:mid])
    right_arr = merge(arr[mid:])
    return m(left_arr, right_arr)


def m(left_arr, right_arr):

    sort_arr = []
    l = r = 0
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] < right_arr[r]:
            sort_arr.append(left_arr[l])
            l += 1
        else:
            sort_arr.append(right_arr[r])
            r += 1
    sort_arr.extend(left_arr[l:])
    sort_arr.extend(right_arr[r:])
    return sort_arr


if __name__ == "__main__":
    result = merge(arr=[4, 3, 1, 6, 2, 5])
    print(result)
