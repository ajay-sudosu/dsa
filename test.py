def arrange_array_element_by_sign_brute_force(arr):
    pos = [i for i in arr if i > 0]
    neg = [i for i in arr if i < 0]
    for i in range(len(pos)):
        arr[2 * i] = pos[i]
        arr[2 * i + 1] = neg[i]
    return arr


check10 = [-2, 1, -1, 2, -3, 4, ]
print(arrange_array_element_by_sign_brute_force(check10))
