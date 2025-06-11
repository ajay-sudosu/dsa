def present(arr, num):
    return num in arr


def check(arr):
    max_seq_count = 1
    for i in arr:
        count = 1
        while present(arr, i+1):
            i = i + 1
            count += 1
            max_seq_count = max(max_seq_count, count)

    return max_seq_count


# arr = [3, 2, 1, 5, 6]
arr = [4, 7, 1, 3, 2, ]
print(check(arr))
