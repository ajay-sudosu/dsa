def arrange_array_element_by_sign_brute_force(arr):
    pos = [i for i in arr if i > 0]
    neg = [i for i in arr if i < 0]
    result = []
    for i in range(len(pos)):
        result.append(pos[i])
        result.append(neg[i])
    return result


check10 = [1, -1, 2, -3]
print(arrange_array_element_by_sign_brute_force(check10))
