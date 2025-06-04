def maj(arr, n):
    count = 0
    element = arr[0]
    for i in arr:
        if count == 0:
            element = i
            count = 1
        elif i == element:
            count += 1
        else:
            count -= 1
    return element


arr = [0, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1]
print(maj(arr=arr, n=4))
