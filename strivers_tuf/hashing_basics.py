def high_low_frequency(arr):
    d = {}
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]] = 1
        else:
            d[arr[i]] += 1

    max = 0
    min = 1
    max_element = 0
    min_element = 0
    for element, count in d.items():
        if count > max:
            max = count
            max_element = element
        if count <= min:
            min = count
            min_element = element
    print(d)
    return max_element, min_element


l = [3, 4, 3, 2, 3, 2, 3, 4, 3, 5]
print(high_low_frequency(l))
