def majority_element(arr):
    count1, count2 = 0, 0
    ele1, ele2 = float("-inf"), float("-inf")

    for i in range(len(arr)):
        if count1 == 0 and ele2 != arr[i]:
            count1 = 1
            ele1 = arr[i]

        elif count2 == 0 and ele1 != arr[i]:
            count2 = 1
            ele2 = arr[i]

        elif ele1 == arr[i]:
            count1 += 1

        elif ele2 == arr[i]:
            count2 += 1

        else:
            count1 -= 1
            count2 -= 1

    result = []

    count1, count2 = 0, 0
    for i in arr:
        if i == ele1:
            count1 += 1

        if i == ele2:
            count2 += 1

    if count1 > int(len(arr)/3) + 1:
        result.append(ele1)

    if count2 > int(len(arr)/3) + 1:
        result.append(ele2)

    return result


check1 = [1, 1, 1, 2, 2, 2, 2, 1, 3, ]
print(majority_element(check1))
