def consecutive_seq_optimal(arr):
    last_min = float("-inf")
    count = 0
    max_count = 1
    arr.sort()
    for i in arr:
        if i-1 == last_min:
            count += 1
            last_min = i

        elif i != last_min:
            last_min = i
            count = 1
        max_count = max(max_count, count)
    return max_count


check16 = [4, 7, 1, 1, 1, 3, 2, 5]
print(consecutive_seq_optimal(check16))




