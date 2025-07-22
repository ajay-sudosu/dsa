def max_sum(arr):
    sub_total = arr[0]
    max_total = arr[0]

    for i in arr[1:]:
        sub_total += i
        sub_total = max(i, sub_total + i)
        max_total = max(sub_total, max_total)
    return max_total


# arr = [1, 2, 0, -1, -5, 6]
arr = [-10, -2, -3]
print(max_sum(arr))
